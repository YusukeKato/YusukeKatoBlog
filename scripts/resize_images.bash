#!/usr/bin/env bash
set -euo pipefail

usage() {
    echo "Usage: bash resize_images.bash [--dry-run] YYYYMMDD|--all"
    echo "Convert original images; keep originals and existing outputs on failure."
}

target=''
dry_run=false
for arg in "$@"; do
    case "$arg" in
        --help|-h) usage; exit 0 ;;
        --dry-run) dry_run=true ;;
        --all)
            [[ -z "$target" ]] || { usage >&2; exit 2; }
            target=all
            ;;
        *)
            [[ -z "$target" && "$arg" =~ ^[0-9]{8}$ ]] || { usage >&2; exit 2; }
            target="$arg"
            ;;
    esac
done
[[ -n "$target" ]] || { usage >&2; exit 2; }

script_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
image_dir=$(cd -- "$script_dir/../assets/images" && pwd)
inventory=''
temporary_output=''
cleanup() {
    [[ -z "$inventory" ]] || rm -f -- "$inventory"
    [[ -z "$temporary_output" ]] || rm -f -- "$temporary_output"
    return 0
}
trap cleanup EXIT
trap 'exit 130' INT
trap 'exit 143' TERM

# Freeze the input list before creating outputs, so outputs never become inputs.
inventory=$(mktemp)
find "$image_dir" -type f -path "$image_dir/20*/*" \
    \( -iname '*.png' -o -iname '*.jpg' -o -iname '*.jpeg' -o -iname '*.gif' -o -iname '*.mp4' \) \
    -print0 > "$inventory"
mapfile -d '' sources < "$inventory"

converted=0
skipped=0
planned=0
failed=0
for file in "${sources[@]}"; do
    filename=${file##*/}
    [[ "$target" == all || "$filename" == "$target"* ]] || continue
    [[ "$filename" != .resize-images.* ]] || continue
    # Published URLs use double extensions. Never delete or reconvert these files.
    [[ ! "${filename,,}" =~ \.(png|jpe?g|gif|mp4)\.(png|jpe?g|gif|mp4)$ ]] || continue
    extension=${filename##*.}
    case "${extension,,}" in
        png|jpg|jpeg) output_extension=jpg ;;
        gif) output_extension=gif ;;
        mp4) output_extension=mp4 ;;
    esac
    output="$file.$output_extension"
    if [[ -s "$output" && ! "$file" -nt "$output" ]]; then
        echo "skip: ${output#"$image_dir"/} (up to date)"
        skipped=$((skipped + 1))
        continue
    fi
    if "$dry_run"; then
        echo "would convert: ${file#"$image_dir"/} -> ${output#"$image_dir"/}"
        planned=$((planned + 1))
        continue
    fi

    if ! command -v ffmpeg >/dev/null 2>&1; then
        echo 'error: ffmpeg is required.' >&2
        exit 1
    fi
    if [[ "$output_extension" == gif ]]; then
        if command -v magick >/dev/null 2>&1; then
            imagemagick=magick
        elif command -v convert >/dev/null 2>&1; then
            imagemagick=convert
        else
            echo 'error: ImageMagick (magick or convert) is required for GIFs.' >&2
            exit 1
        fi
    fi
    # The temporary output is on the same filesystem for an atomic replacement.
    temporary_output=$(mktemp "${file%/*}/.resize-images.XXXXXX.$output_extension")
    options=(-nostdin -hide_banner -loglevel error -y -i "$file")
    case "$output_extension" in
        jpg) options+=(-vf scale=1200:-1 -frames:v 1) ;;
        gif) options+=(-r 10 -vf scale=600:-1) ;;
        mp4) options+=(-movflags faststart -r 10 -vf scale=800:-2) ;;
    esac
    succeeded=false
    if ffmpeg "${options[@]}" "$temporary_output"; then
        if [[ "$output_extension" != gif ]] || "$imagemagick" "$temporary_output" -layers Optimize "$temporary_output"; then
            [[ ! -s "$temporary_output" ]] || succeeded=true
        fi
    fi
    if "$succeeded"; then
        chmod 0644 -- "$temporary_output"
        mv -f -- "$temporary_output" "$output"
        echo "converted: ${output#"$image_dir"/}"
        converted=$((converted + 1))
    else
        echo "error: conversion failed: ${file#"$image_dir"/}; existing output kept." >&2
        failed=$((failed + 1))
    fi
    rm -f -- "$temporary_output"
    temporary_output=''
done
echo "finished: converted=$converted skipped=$skipped planned=$planned failed=$failed"
(( failed == 0 ))

#!/usr/bin/env bash
set -euo pipefail

script_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)
fixture=$(mktemp -d)
trap 'rm -rf -- "$fixture"' EXIT
project="$fixture/project with spaces"
images="$project/assets/images/2026"
mkdir -p "$project/scripts" "$images" "$fixture/bin"
cp "$script_dir/resize_images.bash" "$project/scripts/"
script="$project/scripts/resize_images.bash"
export CALL_LOG="$fixture/ffmpeg.log"
original_path="$PATH"
touch "$CALL_LOG"

cat > "$fixture/bin/ffmpeg" <<'MOCK'
#!/usr/bin/env bash
printf 'called\n' >> "$CALL_LOG"
if [[ "${FAIL_FFMPEG:-0}" != 0 ]]; then
    printf 'partial output\n' > "${!#}"
    exit 1
fi
printf 'converted\n' > "${!#}"
MOCK
cat > "$fixture/bin/magick" <<'MOCK'
#!/usr/bin/env bash
if [[ "${FAIL_CONVERT:-0}" != 0 ]]; then
    printf 'broken GIF\n' > "$1"
    exit 1
fi
MOCK
cp "$fixture/bin/magick" "$fixture/bin/convert"
chmod +x "$fixture/bin/"*
export PATH="$fixture/bin:$PATH"

assert_equal() {
    [[ "$1" == "$2" ]] || { echo "FAIL: $3 (expected $1, got $2)" >&2; exit 1; }
}
expect_failure() {
    if "$@" > "$fixture/failure.log" 2>&1; then
        echo "FAIL: command unexpectedly succeeded: $*" >&2
        exit 1
    fi
}

printf 'original\n' > "$images/20260101 photo.png"
printf 'original\n' > "$images/20260102.JPEG"
printf 'original\n' > "$images/20260103.gif"
printf 'original\n' > "$images/20260104.mp4"
printf 'published\n' > "$images/20260105.JPG.JPG"
printf 'published\n' > "$images/20260106.png.jpg"
printf 'metadata\n' > "$images/20260101 photo.png:Zone.Identifier"
cd "$fixture"

expect_failure bash "$script"
expect_failure bash "$script" --all 20260101
bash "$script" --dry-run --all > "$fixture/dry-run.log"
assert_equal 0 "$(wc -l < "$CALL_LOG")" 'dry run must not convert'
assert_equal 7 "$(find "$images" -type f | wc -l)" 'dry run must not modify files'

bash "$script" 20260101 > /dev/null
assert_equal 1 "$(wc -l < "$CALL_LOG")" 'date selection from another working directory'
[[ -s "$images/20260101 photo.png.jpg" && ! -e "$images/20260102.JPEG.jpg" ]]
bash "$script" 20260101 > /dev/null
assert_equal 1 "$(wc -l < "$CALL_LOG")" 'repeat must skip up-to-date output'

bash "$script" --all > /dev/null
assert_equal 4 "$(wc -l < "$CALL_LOG")" 'only original files are converted'
[[ -s "$images/20260102.JPEG.jpg" && -s "$images/20260103.gif.gif" && -s "$images/20260104.mp4.mp4" ]]
for output in "$images/20260101 photo.png.jpg" "$images/20260102.JPEG.jpg" "$images/20260103.gif.gif" "$images/20260104.mp4.mp4"; do
    assert_equal 644 "$(stat -c %a "$output")" 'published output remains readable'
done
assert_equal published "$(cat "$images/20260105.JPG.JPG")" 'published image without original survives'
assert_equal original "$(cat "$images/20260102.JPEG")" 'JPEG original is not renamed or changed'
assert_equal metadata "$(cat "$images/20260101 photo.png:Zone.Identifier")" 'unrelated metadata is preserved'

touch -t 202001010000 "$images/20260101 photo.png.jpg"
expect_failure env FAIL_FFMPEG=1 bash "$script" 20260101
assert_equal converted "$(cat "$images/20260101 photo.png.jpg")" 'ffmpeg failure preserves old output'
touch -t 202001010000 "$images/20260103.gif.gif"
expect_failure env FAIL_CONVERT=1 bash "$script" 20260103
assert_equal converted "$(cat "$images/20260103.gif.gif")" 'GIF optimization failure preserves old output'
assert_equal '' "$(find "$images" -name '.resize-images.*' -print -quit)" 'temporary outputs are cleaned up'

# Exercise actual encoders on generated fixtures when they are installed.
export PATH="$original_path"
if command -v ffmpeg >/dev/null && command -v ffprobe >/dev/null && command -v convert >/dev/null; then
    real_project="$fixture/real"
    real_images="$real_project/assets/images/2026"
    mkdir -p "$real_project/scripts" "$real_images"
    cp "$script" "$real_project/scripts/"
    convert -size 32x24 xc:red "$real_images/20260101.png"
    convert -size 32x24 xc:blue "$real_images/20260102.JPEG"
    convert -delay 10 -size 32x24 xc:red xc:blue -loop 0 "$real_images/20260103.gif"
    ffmpeg -nostdin -hide_banner -loglevel error -f lavfi -i color=c=red:s=32x24:r=10 \
        -t 0.2 -pix_fmt yuv420p "$real_images/20260104.mp4"
    originals=$(sha256sum "$real_images/"*)
    bash "$real_project/scripts/resize_images.bash" --all > /dev/null
    printf '%s\n' "$originals" | sha256sum --check --status
    for output in "$real_images/"*.jpg "$real_images/"*.gif.gif "$real_images/"*.mp4.mp4; do
        ffmpeg -nostdin -hide_banner -loglevel error -i "$output" -f null -
    done
    assert_equal 1200 "$(ffprobe -v error -select_streams v:0 -show_entries stream=width -of csv=p=0 "$real_images/20260101.png.jpg")" 'JPEG width'
    assert_equal 600 "$(ffprobe -v error -select_streams v:0 -show_entries stream=width -of csv=p=0 "$real_images/20260103.gif.gif")" 'GIF width'
    assert_equal 800 "$(ffprobe -v error -select_streams v:0 -show_entries stream=width -of csv=p=0 "$real_images/20260104.mp4.mp4")" 'MP4 width'
    before=$(sha256sum "$real_images/20260101.png.jpg")
    printf 'invalid image\n' > "$real_images/20260101.png"
    touch -t 202001010000 "$real_images/20260101.png.jpg"
    expect_failure bash "$real_project/scripts/resize_images.bash" 20260101
    assert_equal "$before" "$(sha256sum "$real_images/20260101.png.jpg")" 'real conversion failure preserves output'
    echo 'PASS: real PNG/JPEG/GIF/MP4 conversions and failure preservation'
else
    echo 'SKIP: real conversion checks require ffmpeg, ffprobe, and ImageMagick convert'
fi
echo 'PASS: resize_images regression checks'

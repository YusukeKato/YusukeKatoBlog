#!/bin/bash

if [ -z "$1" ]; then
    echo "error: Argument is not specified." >&2
    exit 1
fi

TARGET="$1"
IMG_DIR="../assets/images"

echo "start: resize images"

# delete
find "$IMG_DIR" -type f -path "*/20*/*" -name "*Zone.Identifier" -delete
find "$IMG_DIR" -type f -path "*/20*/*${TARGET}*" \( -name "*.png.png" -o -name "*.jpg.png" -o -name "*.jpg.jpg" -o -name "*.png.jpg" -o -name "*.gif.gif" -o -name "*.mp4.mp4" \) -delete

# rename
find "$IMG_DIR" -type f -path "*/20*/*${TARGET}*" \( -name "*.jpeg" -o -name "*.JPEG" \) -print0 | while IFS= read -r -d '' file; do
    mv "$file" "${file%.*}.jpg"
done

# resize
find "$IMG_DIR" -type f -path "*/20*/*${TARGET}*" \( -iname "*.png" -o -iname "*.jpg" -o -iname "*.gif" -o -iname "*.mp4" \) -print0 | while IFS= read -r -d '' file; do
    ext="${file##*.}"
    ext_lower=$(echo "$ext" | tr '[:upper:]' '[:lower:]')
    case "$ext_lower" in
        png|jpg)
            ffmpeg -y -i "$file" -vf scale=600:-1 "${file}.jpg" </dev/null
            ;;
        gif)
            ffmpeg -y -i "$file" -r 10 -vf scale=400:-1 "${file}.gif" </dev/null
            convert "${file}.gif" -layers Optimize "${file}.gif"
            ;;
        mp4)
            ffmpeg -y -i "$file" -movflags faststart -r 10 -vf scale=600:-1 "${file}.mp4" </dev/null
            ;;
    esac
done

echo "finish: resize images"

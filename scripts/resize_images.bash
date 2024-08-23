echo "start: resize images"

# delete
find ../images | grep "^../images/20.*/" | grep -e "Identifier$" | xargs -I@ rm @
find ../images | grep "^../images/20.*/"$1 | grep -e ".png.png$" -e ".jpg.png$" -e ".jpg.jpg$" -e ".png.jpg$" -e ".gif.gif$" | xargs -I@ rm @

# rename
find ../images | grep "^../images/20.*/"$1 | grep -e ".jpeg$" | sed 's/.jpeg//g' | xargs -I@ mv @".jpeg" @".jpg"
find ../images | grep "^../images/20.*/"$1 | grep -e ".JPEG$" | sed 's/.JPEG//g' | xargs -I@ mv @".JPEG" @".jpg"

# resize
find ../images | grep "^../images/20.*/"$1 | grep -e ".png$" -e ".jpg$" | xargs -I@ ffmpeg -y -i @ -vf scale=600:-1 @".jpg"
find ../images | grep "^../images/20.*/"$1 | grep -e ".gif$" | xargs -I@ ffmpeg -y -i @ -r 10 -vf scale=400:-1 @".gif"

# Optimize
find ../images | grep "^../images/20.*/"$1 | grep -e ".gif.gif$" | xargs -I@ convert @ -layers Optimize @

echo "finish: resize images"

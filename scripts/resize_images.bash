echo "start: resize images"

# delete
find ../images | grep "^../images/20.*/" | grep -e ".png.png$" -e ".jpg.png$" -e ".jpg.jpg$" -e ".png.jpg$" -e ".gif.gif$" | xargs -I@ rm @

# resize
find ../images | grep "^../images/20.*/" | grep -e ".png$" -e ".jpg$" | xargs -I@ ffmpeg -y -i @ -vf scale=600:-1 @".jpg"
find ../images | grep "^../images/20.*/" | grep -e ".gif$" | xargs -I@ ffmpeg -y -i @ -r 10 -vf scale=400:-1 @".gif"
find ../images | grep "^../images/20.*/" | grep -e ".gif.gif$" | xargs -I@ convert @ -layers Optimize @

echo "finish: resize images"

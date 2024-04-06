echo "start: resize images"
find ../images | grep "^../images/20.*/" | grep -e ".png$" -e ".jpg$" | xargs -I@ ffmpeg -y -i @ -vf scale=800:-1 @".png"
echo "finish: resize images"

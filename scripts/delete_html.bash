echo 'start: delete html'
echo 'delete html list'
find ../html | grep '\.html$'
find ../html | grep '\.html$' | xargs -I@ rm @
echo 'finish: delete html'

# generate html_list.txt
find ../html | grep '\.html$' | grep -v 'index' | sed 's/\.\.\///g' | sort -r > html_list.txt
find ../html | grep '\.html$' | sed 's/\.\.\///g' | grep 'html/[0-9][0-9][0-9][0-9]/[0-9][0-9][0-9][0-9].html' | sort -r > html_list2.txt
echo 'output: html_list.txt'
echo 'output: html_list2.txt'

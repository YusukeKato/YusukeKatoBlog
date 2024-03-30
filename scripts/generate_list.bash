# generate markdown_list.txt
find ../markdown | grep '.md$' | grep -v 'index' | sort -r > markdown_list.txt
find ../markdown | grep '.md$' | grep '../markdown/[0-9][0-9][0-9][0-9]/[0-9][0-9][0-9][0-9].md' | sort -r > markdown_list2.txt

# generate html_list.txt
find ../html | grep '\.html$' | grep -v 'index' | sed 's/\.\.\///g' | sort -r > html_list.txt
find ../html | grep '\.html$' | sed 's/\.\.\///g' | grep 'html/[0-9][0-9][0-9][0-9]/[0-9][0-9][0-9][0-9].html' | sort -r > html_list2.txt

# generate markdown_list.txt
find ../markdown | grep '.md$' | grep -v 'index' | sort -r > markdown_list.txt
find ../markdown | grep '.md$' | grep '../markdown/[0-9][0-9][0-9][0-9]/[0-9][0-9][0-9][0-9].md' | sort -r > markdown_list2.txt
echo 'output: markdown_list.txt'
echo 'output: markdown_list2.txt'

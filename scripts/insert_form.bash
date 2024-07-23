a='<h2 id="news">'
b='<div class=\"iframeClass\">\n<iframe class=\"formClass\" src=\"https:\/\/docs.google.com\/forms\/d\/e\/1FAIpQLSefLzdebOIP_14ZVQLnyxOJZz8vPARVgNKyGaFbIY9Va7LG3Q\/viewform\?embedded=true\" frameborder=\"0\" marginheight=\"0\" marginwidth=\"0\">読み込んでいます…<\/iframe>\n<\/div>\n\n'
c="$b$a"
sed -i -e "s/$a/$c/" ../html/form.html

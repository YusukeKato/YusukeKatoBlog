cp ./*.html ../
cp ./*.gif ../
cp ./*.png ../
cp ./*.jpg ../
cp ./style.css ../
echo "cp ./*.html ../"
echo "cp ./*.gif ../"
echo "cp ./*.png ../"
echo "cp ./*.jpg ../"
echo "cp ./style.css ../"

python -c "import os
files = os.listdir('./')
files2 = [filename for filename in files if 'html' in filename]
f = open('sitemap.xml', 'w', encoding='UTF-8')
f.write('<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n')
f.write('<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n')
f.write('<url>\n')
f.write('<loc>https://yusukekato.jp/</loc>\n')
f.write('<priority>1.0</priority>\n')
f.write('</url>\n')
for filename in files2:
  f.write('<url>\n')
  f.write('<loc>https://yusukekato.jp/'+filename+'</loc>\n')
  f.write('<priority>0.8</priority>\n')
  f.write('</url>\n')
f.close()"
echo "create sitemap.xml"

cp ./sitemap.xml ../
echo "cp ./sitemap.xml ../"

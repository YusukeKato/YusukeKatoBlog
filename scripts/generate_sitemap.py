#!/usr/bin/env python3

import os

# htmlのファイル名を全て取得
html_files = []
with open('./html_list.txt', 'r', encoding='UTF-8') as fr:
    html_files = [rl.rstrip() for rl in fr.readlines()]

# サイトマップ生成
print('start: generate sitemap.xml')
f = open('../sitemap.xml', 'w', encoding='UTF-8')
f.write('<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n')
f.write('<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n')
f.write('\n')
f.write('<url>\n')
f.write('<loc>https://yusukekato.jp/</loc>\n')
f.write('<priority>1.0</priority>\n')
f.write('</url>\n')

f.write('<url>\n')
f.write('<loc>https://yusukekato.jp/index.html</loc>\n')
f.write('<priority>1.0</priority>\n')
f.write('</url>\n')
f.write('\n')

for filename in html_files:
  f.write('<url>\n')
  f.write('<loc>https://yusukekato.jp/'+filename+'</loc>\n')
  f.write('<priority>0.8</priority>\n')
  f.write('</url>\n')
  f.write('\n')
f.write('</urlset>\n')
f.write('\n')
f.close()

print('output: ../sitemap.xml')
print('finish: generate sitemap.xml')

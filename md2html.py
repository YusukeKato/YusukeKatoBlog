#!/usr/bin/env python3

import os

# markdownのファイル名を全て取得
all_file = os.listdir('./')
markdown_files = [file for file in all_file if '.md' in file]

print('start: markdown to html')

# markdownファイルを一つずつ処理
for markdown_file in markdown_files:

    print('input: ' + markdown_file)

    # 読み込み用
    read_lines = []

    # 読み込み
    with open(markdown_file, 'r', encoding='UTF-8') as fr:
        read_lines = fr.readlines()

    # 書き込み用
    write_lines = []

    write_lines.append('<!DOCTYPE html>\n')
    write_lines.append('<html lang="ja">\n')
    write_lines.append('<head>\n')
    write_lines.append('<!-- Google tag (gtag.js) -->\n')
    write_lines.append('<script async src="https://www.googletagmanager.com/gtag/js?id=G-W9H7QJT6XG"></script>\n')
    write_lines.append('<script>\n')
    write_lines.append('window.dataLayer = window.dataLayer || [];\n')
    write_lines.append('function gtag(){dataLayer.push(arguments);}\n')
    write_lines.append("gtag('js', new Date());\n")
    write_lines.append("gtag('config', 'G-W9H7QJT6XG');\n")
    write_lines.append('</script>\n')
    write_lines.append('<!-- SNS Card -->\n')
    write_lines.append('<meta property="og:type" content="article" />\n')
    write_lines.append('<meta property="og:site_name" content="加藤祐介ブログ / Yusuke Kato Blog" />\n')
    write_lines.append('<meta property="og:image" content="https://yusukekato.jp/summary.jpg" />\n')
    write_lines.append('<meta name="twitter:card" content="summary_large_image" />\n')
    write_lines.append('<meta name="twitter:site" content="@yusukekato_main" />\n')
    write_lines.append('<meta name="twitter:image" content="https://yusukekato.jp/summary_large_image.png" />\n')
    write_lines.append('<!-- 変更 -->\n')

    # 書き込み
    with open(markdown_file + '.html', 'w', encoding='UTF-8') as fw:
        fw.writelines(write_lines)

    print('output: ' + markdown_file + '.html')

print('finish: markdown to html')

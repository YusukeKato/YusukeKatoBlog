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
        read_lines = [rl.rstrip() for rl in fr.readlines()]

    # 書き込み用
    write_lines = []

    # head生成
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
    write_lines.append('<meta name="twitter:title" content="' + read_lines[0] + ' / Yusuke Kato Blog" />\n')
    write_lines.append('<meta property="og:url" content="https://yusukekato.jp/' + markdown_file + '.html" />\n')
    write_lines.append('<meta property="og:title" content="' + read_lines[0] + ' / Yusuke Kato Blog" />\n')
    write_lines.append('<meta property="og:description" content="' + read_lines[1] + '" />\n')
    write_lines.append('<meta name="twitter:description" content="' + read_lines[1] + '" />\n')
    write_lines.append('<title>' + read_lines[0] + ' / Yusuke Kato Blog</title>\n')
    write_lines.append('<meta name="description" content="' + read_lines[1] + '" />\n')
    write_lines.append('<!-- main -->\n')
    write_lines.append('<meta charset="utf-8">\n')
    write_lines.append('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
    write_lines.append('<link rel="icon" href="./favicon.png">\n')
    write_lines.append('<link rel="stylesheet" href="./style.css">\n')
    write_lines.append('</head>\n')
    write_lines.append('\n')

    write_lines.append('<body>\n')
    write_lines.append('\n')

    # header生成
    write_lines.append('<header>\n')
    write_lines.append('<h1 class="headline">\n')
    write_lines.append('<a>加藤祐介ブログ</a>\n')
    write_lines.append('</h1>\n')
    write_lines.append('<ul class="nav-list">\n')
    write_lines.append('<li class="nav-list-item">\n')
    write_lines.append('<a href="https://yusukekato.jp/" class="bButton">HOME</a>\n')
    write_lines.append('</li>\n')
    write_lines.append('<li class="nav-list-item">\n')
    write_lines.append('<a href="https://yusukekato.jp/about.html" class="bButton">ABOUT</a>\n')
    write_lines.append('</li>\n')
    write_lines.append('<li class="nav-list-item">\n')
    write_lines.append('<a href="https://yusukekato.jp/form.html" class="bButton">CONTACT</a>\n')
    write_lines.append('</li>\n')
    write_lines.append('</ul>\n')
    write_lines.append('</header>\n')

    # 本文の処理

    # footer生成
    write_lines.append('<footer>\n')
    write_lines.append('<hr>\n')
    write_lines.append('<a href="https://yusukekato.jp/" class="aButton">ホームへ戻る</a>\n')
    write_lines.append('<p>　加藤祐介ブログは<a href="https://github.com/YusukeKato/YusukeKatoBlog/blob/main/LICENSE">MIT LICENSE</a> で公開されています。</p>\n')
    write_lines.append('<p>　(c) 2023-2024 Yusuke Kato</p>\n')
    write_lines.append('<div class="img">\n')
    write_lines.append('<img src="https://yusukekato.jp/BlueTreeIcon.jpg">\n')
    write_lines.append('</div>\n')

    write_lines.append('\n')
    write_lines.append('</body>\n')
    write_lines.append('</html>\n')

    # 書き込み
    with open(markdown_file + '.html', 'w', encoding='UTF-8') as fw:
        fw.writelines(write_lines)

    print('output: ' + markdown_file + '.html')

print('finish: markdown to html')

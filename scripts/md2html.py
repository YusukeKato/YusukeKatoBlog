#!/usr/bin/env python3

import os
import re

# markdownのファイル名を全て取得
markdown_files = []
with open('./markdown_list.txt', 'r', encoding='UTF-8') as fr:
    markdown_files = [rl.rstrip() for rl in fr.readlines()]

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

    # メタデータ
    title = read_lines[1][8:]
    description = read_lines[2][14:]
    date = read_lines[3][7:]
    update = read_lines[4][9:]
    math_flag = read_lines[5][7:]

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
    write_lines.append('<meta property="og:image" content="https://yusukekato.jp/images/summary.jpg" />\n')
    write_lines.append('<meta name="twitter:card" content="summary_large_image" />\n')
    write_lines.append('<meta name="twitter:site" content="@yusukekato_main" />\n')
    write_lines.append('<meta name="twitter:image" content="https://yusukekato.jp/images/summary_large_image.png" />\n')
    write_lines.append('<!-- 変更 -->\n')
    write_lines.append('<meta name="twitter:title" content="' + title + ' / Yusuke Kato Blog" />\n')
    write_lines.append('<meta property="og:url" content="https://yusukekato.jp/' + markdown_file.replace('markdown', 'html').replace('.md', '.html') + '" />\n')
    write_lines.append('<meta property="og:title" content="' + title + ' / Yusuke Kato Blog" />\n')
    write_lines.append('<meta property="og:description" content="' + description + '" />\n')
    write_lines.append('<meta name="twitter:description" content="' + description + '" />\n')
    write_lines.append('<title>' + title + ' / Yusuke Kato Blog</title>\n')
    write_lines.append('<meta name="description" content="' + description + '" />\n')
    write_lines.append('<!-- main -->\n')
    write_lines.append('<meta charset="utf-8">\n')
    write_lines.append('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
    write_lines.append('<link rel="icon" href="https://yusukekato.jp/images/favicon.png">\n')
    write_lines.append('<link rel="stylesheet" href="https://yusukekato.jp/css/style.css?version=51">\n')
    write_lines.append('<link rel="preconnect" href="https://fonts.googleapis.com">\n')
    write_lines.append('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n')
    write_lines.append('<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@100..900&display=swap" rel="stylesheet">\n')
    if math_flag == 'true': # 数式を使用する場合
        write_lines.append('<script id="MathJax-script" async\n')
        write_lines.append('  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js">\n')
        write_lines.append('</script>\n')
    write_lines.append('</head>\n')
    write_lines.append('<body>\n')

    # header生成
    # write_lines.append('<header>\n')
    # write_lines.append('<h1 class="headline">\n')
    # write_lines.append('<a>加藤祐介ブログ</a>\n')
    # write_lines.append('</h1>\n')
    write_lines.append('<h1 id="top" class="heading-028" data-label="YUSUKE KATO BLOG">加藤祐介ブログ</h1>\n')
    # write_lines.append('</header>\n')
    write_lines.append('\n')

    # 本文の処理
    write_lines.append('<div class="alldiv">\n')
    write_lines.append('<ul class="nav-list">\n')
    write_lines.append('<li class="nav-list-item">\n')
    write_lines.append('<a href="https://yusukekato.jp/" class="bButton">HOME</a>\n')
    write_lines.append('</li>\n')
    write_lines.append('<li class="nav-list-item">\n')
    write_lines.append('<a href="https://yusukekato.jp/html/about.html" class="bButton">ABOUT</a>\n')
    write_lines.append('</li>\n')
    write_lines.append('<li class="nav-list-item">\n')
    write_lines.append('<a href="https://yusukekato.jp/html/form.html" class="bButton">CONTACT</a>\n')
    write_lines.append('</li>\n')
    write_lines.append('</ul>\n')
    write_lines.append('<h1>' + title + '</h1>\n')
    write_lines.append('<p>記事投稿日: ' + date + '</p>\n')
    write_lines.append('<p>最終更新日: ' + update + '</p>\n')
    i = 0
    h2_id = 0
    h2_arr = []
    while i < len(read_lines):
        i += 1
        if i >= len(read_lines):
            break
        elif i < 6: # メタデータは飛ばす
            continue
        elif read_lines[i] == '': # 空行は飛ばす
            continue
        else: # 見出しを変換
            if re.match('^# .+', read_lines[i]):
                write_lines.append('<h1>' + read_lines[i][2:] + '</h1>\n')
            elif re.match('^## .+', read_lines[i]):
                write_lines.append('<h2 id="' + str(h2_id) + '">' + read_lines[i][3:] + '</h2>\n')
                h2_id += 1
                h2_arr.append(read_lines[i][3:])
            elif re.match('^### .+', read_lines[i]):
                write_lines.append('<h3>' + read_lines[i][4:] + '</h3>\n')
            elif re.match('^#### .+', read_lines[i]):
                write_lines.append('<h4>' + read_lines[i][5:] + '</h4>\n')
            elif re.match('^##### .+', read_lines[i]):
                write_lines.append('<h5>' + read_lines[i][6:] + '</h5>\n')
            heading_loop_flag = True
            while heading_loop_flag: # 見出しの内容を変換するためのループ
                i += 1
                if i >= len(read_lines):
                    heading_loop_flag = False
                elif read_lines[i] == '':
                    continue
                elif re.match('^#.+', read_lines[i]): # 次の見出しが来たら終了
                    i -= 1
                    heading_loop_flag = False
                elif re.match('^-.+', read_lines[i]): # 箇条書きを変換
                    write_lines.append('<div class="main-ul">\n')
                    write_lines.append('<ul>\n')
                    write_lines.append('<li>' + read_lines[i][2:] + '</li>\n')
                    ul_loop_flag = True
                    while ul_loop_flag:
                        i += 1
                        if i >= len(read_lines):
                            ul_loop_flag = False
                        elif read_lines[i] == '' or not '-' in read_lines[i]: # 箇条書きの終了条件は空行か'-'が無いこと
                            i -= 1
                            ul_loop_flag = False
                        elif re.match('^-.+', read_lines[i]):
                            write_lines.append('<li>' + read_lines[i][2:] + '</li>\n')
                    write_lines.append('</ul>\n')
                    write_lines.append('</div>\n')
                elif re.match('^```.*', read_lines[i]): # ソースコードを変換
                    write_lines.append('<div class="codeClass"><pre><code>' + read_lines[i+1].replace('<', '&lt;').replace('>', '&gt;') + '\n')
                    i += 1
                    code_loop_flag = True
                    while code_loop_flag:
                        i += 1
                        if i >= len(read_lines):
                            code_loop_flag = False
                        elif re.match('^```$', read_lines[i]):
                            code_loop_flag = False
                        else:
                            write_lines.append(read_lines[i].replace('<', '&lt;').replace('>', '&gt;') + '\n')
                    write_lines.append('</code></pre></div>\n')
                elif re.match('https://www.youtube.com/embed/.+', read_lines[i]): # YouTubeの埋め込み
                    write_lines.append('<div class="iframeClass">\n')
                    write_lines.append('<iframe width="560" height="315" src="' + read_lines[i] + '" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>')
                    write_lines.append('</div>\n')
                elif re.match('http.*://.+', read_lines[i]): # URLを変換
                    write_lines.append('<a href="' + read_lines[i] + '" class="aButton">' + read_lines[i+2] + '</a>\n')
                    i += 2
                elif re.match('.+\.png', read_lines[i]) or re.match('.+\.jpg', read_lines[i]): # 画像を変換
                    write_lines.append('<div class="img">\n')
                    write_lines.append('<img src="https://yusukekato.jp/images/' + read_lines[i] + '.jpg' + '" alt="' + read_lines[i+2] + '">\n')
                    write_lines.append('</div>\n')
                    i += 2
                elif re.match('.+\.gif', read_lines[i]): # GIF画像を変換
                    write_lines.append('<div class="img">\n')
                    write_lines.append('<img src="https://yusukekato.jp/images/' + read_lines[i] + '.gif' + '" alt="' + read_lines[i+2] + '">\n')
                    write_lines.append('</div>\n')
                    i += 2
                else: # 文章を変換
                    write_lines.append('<p>' + read_lines[i] + '\n')
                    p_loop_flag = True;
                    while p_loop_flag:
                        i += 1
                        if i >= len(read_lines):
                            p_loop_flag = False
                        elif read_lines[i] == '':
                            p_loop_flag = False
                        else:
                            write_lines.append(read_lines[i] + '\n')
                    write_lines.append('</p>\n')

    # お知らせ生成
    write_lines.append('<h2 id="news">お知らせ</h2>\n')
    write_lines.append('<ul>\n')
    write_lines.append('<li>2024/08/01: <a href="https://yusukekato.jp/html/2024/0801.html">れもんが我が家に来て一ヶ月</a></li>\n')
    write_lines.append('<li>2024/06/29: <a href="https://yusukekato.jp/html/2024/0630.html">セキセイインコ「れもん」我が家へ</a></li>\n')
    write_lines.append('<li>2024/05/03: <a href="https://shellgei-online-judge.com/">シェル芸オンラインジャッジ一周年</a></li>\n')
    write_lines.append('</ul>\n')
    write_lines.append('<div class="slide">\n')
    write_lines.append('<img src="https://yusukekato.jp/images/news/news_20240804.jpg" class="slide-img">\n')
    write_lines.append('<img src="https://yusukekato.jp/images/news/news_20240629.jpg" class="slide-img">\n')
    write_lines.append('<img src="https://yusukekato.jp/images/news/news_20240503.jpg" class="slide-img">\n')
    write_lines.append('</div>\n')
    write_lines.append('<details>\n')
    write_lines.append('<summary>過去のお知らせ</summary>\n')
    write_lines.append('<ul>\n')
    write_lines.append('<li>2023/05/03: <a href="https://shellgei-online-judge.com/">シェル芸オンラインジャッジ開始</a></li>\n')
    write_lines.append('<li>2023/04/08: <a href="https://yusukekato.jp/">加藤祐介ブログ開始</a></li>\n')
    write_lines.append('</ul>\n')
    write_lines.append('</details>\n')
    write_lines.append('\n')

    # footer生成
    write_lines.append('<footer>\n')
    write_lines.append('<hr class="BlackLine">\n')
    write_lines.append('<a href="https://yusukekato.jp/html/form.html" class="aButton">お問い合わせフォームへ</a>\n')
    write_lines.append('<a href="#top" class="aButton">ページトップへ</a>\n')
    write_lines.append('<a href="https://yusukekato.jp/" class="aButton">ホームへ戻る</a>\n')
    write_lines.append('<div class="img">\n')
    write_lines.append('<img src="https://yusukekato.jp/images/BlueTreeIcon.jpg">\n')
    write_lines.append('</div>\n')
    write_lines.append('<ul class="nav-list">\n')
    write_lines.append('<li class="nav-list-item">\n')
    write_lines.append('<a href="https://yusukekato.jp/" class="bButton">HOME</a>\n')
    write_lines.append('</li>\n')
    write_lines.append('<li class="nav-list-item">\n')
    write_lines.append('<a href="https://yusukekato.jp/html/about.html" class="bButton">ABOUT</a>\n')
    write_lines.append('</li>\n')
    write_lines.append('<li class="nav-list-item">\n')
    write_lines.append('<a href="https://yusukekato.jp/html/form.html" class="bButton">CONTACT</a>\n')
    write_lines.append('</li>\n')
    write_lines.append('</ul>\n')
    write_lines.append('</footer>\n')

    write_lines.append('</div> <!-- alldiv -->\n')

    write_lines.append('<h1 id="bottom" class="heading-028-2" data-label="" xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/">\n')
    write_lines.append('加藤祐介ブログの著作物はCC BY-NC-ND 4.0で公開されています。<br>\n')
    write_lines.append('加藤祐介ブログのソフトウェアはMITライセンスで公開されています。<br>\n')
    write_lines.append('&copy; 2023 YusukeKato All Rights Reserved.<br><br>\n')
    write_lines.append('<img style="height:22px!important;margin-left:2px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nd.svg?ref=chooser-v1" alt=""><br>\n')
    write_lines.append('</h1>\n')

    write_lines.append('</body>\n')
    write_lines.append('</html>\n')

    # 目次
    index_position = 53
    write_lines.insert(index_position, '\n')
    write_lines.insert(index_position+1, '<h2 id="index">目次</h2>\n')
    write_lines.insert(index_position+2, '<ul>\n')
    for i in range(len(h2_arr)):
        write_lines.insert(index_position+3+i, '<li><a href="#' + str(i) + '">' + h2_arr[i] + '</a></li>\n')
    write_lines.insert(index_position+3+len(h2_arr), '<li><a href="#news">お知らせ</a></li>\n')
    write_lines.insert(index_position+3+len(h2_arr)+1, '</ul>\n')
    write_lines.insert(index_position+3+len(h2_arr)+2, '\n')

    # 書き込み
    with open(markdown_file.replace('markdown', 'html').replace('.md', '.html'), 'w', encoding='UTF-8') as fw:
        fw.writelines(write_lines)

    print('output: ' + markdown_file.replace('markdown', 'html').replace('.md', '.html'))

print('finish: markdown to html')

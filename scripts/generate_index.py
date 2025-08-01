#!/usr/bin/env python3
import os
import re
version="1005"

print('start: generate index.html')

# markdownのファイル名を全て取得
markdown_files = []
with open('./markdown_list2.txt', 'r', encoding='UTF-8') as fr:
    markdown_files = [rl.rstrip() for rl in fr.readlines()]

# htmlのファイル名を全て取得
html_files = []
with open('./html_list2.txt', 'r', encoding='UTF-8') as fr:
    html_files = [rl.rstrip() for rl in fr.readlines()]

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
write_lines.append('<meta property="og:image" content="https://yusukekato.jp/images/summary.jpg" />\n')
write_lines.append('<meta name="twitter:card" content="summary_large_image" />\n')
write_lines.append('<meta name="twitter:site" content="@yusukekato_main" />\n')
write_lines.append('<meta name="twitter:image" content="https://yusukekato.jp/images/summary_large_image.png" />\n')
write_lines.append('<!-- 変更 -->\n')
write_lines.append('<meta name="twitter:title" content="加藤祐介ブログ / Yusuke Kato Blog" />\n')
write_lines.append('<meta property="og:url" content="https://yusukekato.jp/index.html" />\n')
write_lines.append('<meta property="og:title" content="加藤祐介ブログ / Yusuke Kato Blog" />\n')
write_lines.append('<meta property="og:description" content="加藤祐介のブログです。ROS/ROS 2やシェル芸、競技プログラミング、CTF、ゲーム製作などで日々遊んでいます。大学ではロボットについて勉強していました。備忘録的な記事をまとめていくのでよろしくお願いします。ペットの日記も始めました。" />\n')
write_lines.append('<meta name="twitter:description" content="加藤祐介のブログです。ROS/ROS 2やシェル芸、競技プログラミング、CTF、ゲーム製作などで日々遊んでいます。大学ではロボットについて勉強していました。備忘録的な記事をまとめていくのでよろしくお願いします。ペットの日記も始めました。" />\n')
write_lines.append('<title>加藤祐介ブログ / Yusuke Kato Blog</title>\n')
write_lines.append('<meta name="description" content="加藤祐介のブログです。ROS/ROS 2やシェル芸、競技プログラミング、CTF、ゲーム製作などで日々遊んでいます。大学ではロボットについて勉強していました。備忘録的な文章をまとめていくのでよろしくお願いします。ペットの日記も始めました。" />\n')
write_lines.append('<!-- main -->\n')
write_lines.append('<meta charset="utf-8">\n')
write_lines.append('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
write_lines.append('<link rel="icon" href="https://yusukekato.jp/images/favicon.png">\n')
write_lines.append('<link rel="stylesheet" href="https://yusukekato.jp/css/style.css?version='+version+'">\n')
write_lines.append('<link rel="preconnect" href="https://fonts.googleapis.com">\n')
write_lines.append('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n')
write_lines.append('<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@100..900&display=swap" rel="stylesheet">\n')
write_lines.append('</head>\n')
write_lines.append('<body>\n')

# header生成
write_lines.append('<h1 id="top" class="heading-028" data-label="YUSUKE KATO BLOG">加藤祐介ブログ</h1>\n')
write_lines.append('\n')

# 本文生成

# リストボタン生成
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
write_lines.append('\n')

# お知らせ生成
write_lines.append('<h2 id="news">お知らせ</h2>\n')
write_lines.append('<ul>\n')
write_lines.append('<li>2025/01/02: <a href="https://yusukekato.jp/html/2025/0102.html">シェル芸オンラインジャッジの紹介</a></li>\n')
write_lines.append('<li>2024/09/21: <a href="https://yusukekato.jp/html/2024/0921.html">ズグロシロハラインコ「ぐぐ」我が家へ</a></li>\n')
write_lines.append('<li>2024/09/07: <a href="https://yusukekato.jp/html/2024/0907.html">ズグロシロハラインコ「ぽぽ」我が家へ</a></li>\n')
write_lines.append('<li>2024/08/01: <a href="https://yusukekato.jp/html/2024/0801.html">れもんが我が家に来て一ヶ月</a></li>\n')
write_lines.append('<li>2024/06/29: <a href="https://yusukekato.jp/html/2024/0630.html">セキセイインコ「れもん」我が家へ</a></li>\n')
write_lines.append('</ul>\n')
write_lines.append('<div class="slide">\n')
write_lines.append('<img src="https://yusukekato.jp/images/news/news_20250503.jpg" class="slide-img">\n')
write_lines.append('<img src="https://yusukekato.jp/images/news/news_20240921.jpg" class="slide-img">\n')
write_lines.append('<img src="https://yusukekato.jp/images/news/news_20240907.jpg" class="slide-img">\n')
write_lines.append('<img src="https://yusukekato.jp/images/news/news_20240804.jpg" class="slide-img">\n')
write_lines.append('<img src="https://yusukekato.jp/images/news/news_20240629.jpg" class="slide-img">\n')
write_lines.append('</div>\n')
write_lines.append('<details>\n')
write_lines.append('<summary>過去のお知らせ</summary>\n')
write_lines.append('<ul>\n')
write_lines.append('<li>2024/05/03: <a href="https://shellgei-online-judge.com/">シェル芸オンラインジャッジ一周年</a></li>\n')
write_lines.append('<li>2023/05/03: <a href="https://shellgei-online-judge.com/">シェル芸オンラインジャッジ開始</a></li>\n')
write_lines.append('<li>2023/04/08: <a href="https://yusukekato.jp/">加藤祐介ブログ開始</a></li>\n')
write_lines.append('</ul>\n')
write_lines.append('</details>\n')
write_lines.append('\n')

# プロフィール生成
write_lines.append('<h2 id="about-blog">加藤祐介ブログの情報</h2>\n')
write_lines.append('<p>加藤祐介ブログについては下記をご覧ください。</p>\n')
write_lines.append('<a href="https://yusukekato.jp/html/about.html" class="aButton">加藤祐介ブログについて</a>\n')
write_lines.append('<a href="https://yusukekato.jp/html/form.html" class="aButton">加藤祐介ブログのお問い合わせフォーム</a>\n')
write_lines.append('<a href="https://github.com/YusukeKato/YusukeKatoBlog" class="aButton">加藤祐介ブログのGitHubリポジトリ</a>\n')
write_lines.append('\n')

# シリーズ記事一覧
write_lines.append('<h2 id="series">シリーズ記事一覧</h2>\n')
write_lines.append('<p>各シリーズの記事を下記にまとめてあります。</p>\n')
series = ["lemon",
          "alpacahack",
          "shellgei",
          "ros2",
          "tech",
          "elden-ring",
          "nightreign",
          "pokepoke",
          "book",
          "movie",
          "cooking",
          "others"]
series_name = ["我が家のインコ「れもん＆ぽぽ＆ぐぐ&さん」の日記",
               "AlpacaHackで始めるCTF入門",
               "シェル芸",
               "ROS 2",
               "技術ネタ",
               "ELDEN RING BLOG",
               "ELDEN RING NIGHTREIGN BLOG",
               "ポケポケブログ",
               "読書日記",
               "映画日記",
               "料理日記",
               "その他"]
for j in range(len(series)):
    # 一覧作成
    write_lines.append('<details>\n')
    write_lines.append('<summary>' + series_name[j] + '</summary>\n')
    for i in range(len(html_files)):
        # 読み込み用
        read_lines = []
        # 読み込み
        with open(markdown_files[i], 'r', encoding='UTF-8') as fr:
            read_lines = [rl.rstrip() for rl in fr.readlines()]
        if series[j] in read_lines[6]:
            title = read_lines[1][8:]
            write_lines.append('<a href="https://yusukekato.jp/' + html_files[i] + '" class="aButton">' + title + '</a>\n')
    write_lines.append('</details>\n')
    write_lines.append('\n')

# 記事一覧
year_arr = []
year = html_files[0][5:9]
month = html_files[0][10:12]
year_flag = True
month_flag = True
for i in range(len(html_files)):
    # 見出し生成
    if year_flag:
        year_arr.append(year)
        write_lines.append('\n')
        write_lines.append('<h2 id="' + year + '">' + year + '年の記事' + '</h2>\n')
        year_flag = False

    if month_flag:
        write_lines.append('\n')
        write_lines.append('<h3>' + month + '月の記事' + '</h3>\n')
        month_flag = False

    # 読み込み用
    read_lines = []

    # 読み込み
    with open(markdown_files[i], 'r', encoding='UTF-8') as fr:
        read_lines = [rl.rstrip() for rl in fr.readlines()]

    # タイトル取得
    title = read_lines[1][8:]

    # 記事一覧生成
    write_lines.append('<a href="https://yusukekato.jp/' + html_files[i] + '" class="aButton">' + title + '</a>\n')

    # 年月を更新
    if i+1 == len(html_files):
        break
    tmp_year = html_files[i+1][5:9]
    tmp_month = html_files[i+1][10:12]
    if not year == tmp_year:
        year_flag = True
        year = tmp_year
    if not month == tmp_month:
        month_flag = True
        month = tmp_month

# footer生成
write_lines.append('\n')
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
write_lines.append('加藤祐介ブログのソフトウェアはApache License 2.0で公開されています。<br>\n')
write_lines.append('About License: <a href="https://github.com/YusukeKato/YusukeKatoBlog/blob/main/LICENSE" class="white-link">GitHub - YusukeKatoBlog/LICENSE</a><br>\n')
write_lines.append('&copy; 2023 YusukeKato All Rights Reserved.<br><br>\n')
write_lines.append('<img style="height:22px!important;margin-left:2px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nd.svg?ref=chooser-v1" alt=""><br>\n')
write_lines.append('</h1>\n')

write_lines.append('</body>\n')
write_lines.append('</html>\n')

# 目次を追加
index_position = 62
for i in range(len(write_lines)):
    if write_lines[i] == '</details>\n':
        index_position = i+1
        break
write_lines.insert(index_position, '\n')
write_lines.insert(index_position+1, '<h2 id="index">目次</h2>\n')
write_lines.insert(index_position+2, '<ul>\n')
write_lines.insert(index_position+3, '<li><a href="#news">お知らせ</a></li>\n')
write_lines.insert(index_position+4, '<li><a href="#index">目次</a></li>\n')
write_lines.insert(index_position+5, '<li><a href="#about-blog">加藤祐介ブログの情報</a></li>\n')
write_lines.insert(index_position+6, '<li><a href="#series">シリーズ記事一覧</a></li>\n')
for i in range(len(year_arr)):
    write_lines.insert(index_position+7+i, '<li><a href="#' + year_arr[i] + '">' + year_arr[i] + '年の記事</a></li>\n')
write_lines.insert(index_position+7+len(year_arr), '</ul>\n')
write_lines.insert(index_position+7+len(year_arr)+1, '\n')

# 書き込み
with open('../html/index.html', 'w', encoding='UTF-8') as fw:
    fw.writelines(write_lines)

print('output: ../html/index.html')
print('finish: generate index.html')

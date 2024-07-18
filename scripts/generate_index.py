!/usr/bin/env python3

import os
import re

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
write_lines.append('<meta property="og:description" content="加藤祐介のブログです。ROS/ROS 2やシェル芸、競技プログラミング、ゲーム製作などで日々遊んでいます。大学ではロボットについて勉強していました。備忘録的な記事をまとめていくのでよろしくお願いします。ペットの日記も始めました。" />\n')
write_lines.append('<meta name="twitter:description" content="加藤祐介のブログです。ROS/ROS 2やシェル芸、競技プログラミング、ゲーム製作などで日々遊んでいます。大学ではロボットについて勉強していました。備忘録的な記事をまとめていくのでよろしくお願いします。ペットの日記も始めました。" />\n')
write_lines.append('<title>加藤祐介ブログ / Yusuke Kato Blog</title>\n')
write_lines.append('<meta name="description" content="加藤祐介のブログです。ROS/ROS 2やシェル芸、競技プログラミング、ゲーム製作などで日々遊んでいます。大学ではロボットについて勉強していました。備忘録的な文章をまとめていくのでよろしくお願いします。ペットの日記も始めました。" />\n')
write_lines.append('<!-- main -->\n')
write_lines.append('<meta charset="utf-8">\n')
write_lines.append('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
write_lines.append('<link rel="icon" href="https://yusukekato.jp/images/favicon.png">\n')
write_lines.append('<link rel="stylesheet" href="https://yusukekato.jp/css/style.css?version=44">\n')
write_lines.append('<link rel="preconnect" href="https://fonts.googleapis.com">\n')
write_lines.append('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n')
write_lines.append('<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@100..900&display=swap" rel="stylesheet">\n')
write_lines.append('</head>\n')
write_lines.append('<body>\n')

# header生成
# write_lines.append('<header>\n')
# write_lines.append('<h1 class="headline">\n')
# write_lines.append('<a>加藤祐介ブログ</a>\n')
# write_lines.append('</h1>\n')
write_lines.append('<h1 class="heading-028" data-label="YUSUKE KATO BLOG">加藤祐介ブログ</h1>\n')
# write_lines.append('</header>\n')
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
write_lines.append('<h2>お知らせ</h2>\n')
write_lines.append('<ul>\n')
write_lines.append('<li>2024/06/29: セキセイインコ「れもん」が我が家へ</li>\n')
write_lines.append('<li>2024/05/03: シェル芸オンラインジャッジ一周年</li>\n')
write_lines.append('<li>2023/05/03: シェル芸オンラインジャッジサービス開始</li>\n')
write_lines.append('</ul>\n')
write_lines.append('<div class="slide">\n')
write_lines.append('<img src="https://yusukekato.jp/images/news/SOJ_news_20240629_2.jpg" class="slide-img">\n')
write_lines.append('<img src="https://yusukekato.jp/images/news/SOJ_news_20240503_2.jpg" class="slide-img">\n')
write_lines.append('<img src="https://yusukekato.jp/images/news/SOJ_news_20230503_2.jpg" class="slide-img">\n')
write_lines.append('</div>\n')
write_lines.append('<a href="https://yusukekato.jp/html/2024/0630.html" class="aButton">セキセイインコの「れもん」が我が家にやってきました！</a>\n')
write_lines.append('<a href="https://shellgei-online-judge.com/" class="aButton">シェル芸オンラインジャッジ</a>\n')
write_lines.append('\n')

# プロフィール生成
write_lines.append('<h2>このブログについて</h2>\n')
write_lines.append('<a href="https://yusukekato.jp/html/about.html" class="aButton">加藤祐介ブログについて</a>\n')
write_lines.append('<a href="https://yusukekato.jp/html/form.html" class="aButton">加藤祐介ブログのお問い合わせフォーム</a>\n')
write_lines.append('<a href="https://github.com/YusukeKato/YusukeKatoBlog" class="aButton">加藤祐介ブログのリポジトリ</a>\n')
write_lines.append('\n')
write_lines.append('<h2>私について</h2>\n')
write_lines.append('<h3>自己紹介</h3>\n')
write_lines.append('<p>ロボットやシェル芸、競技プログラミング、ゲーム製作などで日々遊んでいます。\n')
write_lines.append('大学ではロボットについて勉強していました。\n')
write_lines.append('現在もロボット開発に携わらせていただいてます。\n')
write_lines.append('備忘録的な記事をまとめていくのでよろしくお願いします。\n')
write_lines.append('最近はペットの日記も始めました。</p>\n')
write_lines.append('\n')
write_lines.append('<h3>開発したサービス</h3>\n')
write_lines.append('<a href="https://shellgei-online-judge.com/" class="aButton">シェル芸オンラインジャッジ</a>\n')
write_lines.append('\n')
write_lines.append('<h3>SNSアカウント</h3>\n')
write_lines.append('<a href="https://github.com/YusukeKato" class="aButton">GitHub : YusukeKato</a>\n')
write_lines.append('<a href="https://twitter.com/y_kato222" class="aButton">X/Twitter : y_kato222</a>\n')
write_lines.append('<a href="https://twitter.com/yusukekato_main" class="aButton">X/Twitter : yusukekato_main</a>\n')
write_lines.append('\n')
write_lines.append('<h3>他のブログ</h3>\n')
write_lines.append('<a href="https://zenn.dev/yusukekato" class="aButton">Zenn : yusukekato</a>\n')
write_lines.append('<a href="https://qiita.com/ykpages" class="aButton">Qiita : ykpages</a>\n')
write_lines.append('<a href="https://kato-robotics.hatenablog.com/" class="aButton">HatenaBlog : YKpages</a>\n')
write_lines.append('<a href="https://shellgei.wiki/" class="aButton">シェル芸の非公式WIKI</a>\n')
write_lines.append('<a href="https://harunachan.com/" class="aButton">ハルナちゃんブログ</a>\n')
write_lines.append('\n')
write_lines.append('<h3>趣味の小説</h3>\n')
write_lines.append('<a href="https://kakuyomu.jp/users/yusuke_kato" class="aButton">カクヨム : yusuke_kato</a>\n')
write_lines.append('<a href="https://note.com/yusuke_kato" class="aButton">note : yusuke_kato</a>\n')
write_lines.append('\n')
write_lines.append('<h3>その他の外部サイト</h3>\n')
write_lines.append('<a href="https://atcoder.jp/users/yusuke_kato" class="aButton">AtCoder : yusuke_kato</a>\n')
write_lines.append('\n')

# 記事一覧
year = html_files[0][5:9]
month = html_files[0][10:12]
year_flag = True
month_flag = True
for i in range(len(html_files)):
    # 見出し生成
    if year_flag:
        write_lines.append('\n')
        write_lines.append('<h2>' + year + '年の記事' + '</h2>\n')
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

write_lines.append('<h1 class="heading-028-2" data-label="" xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/">\n')
write_lines.append('加藤祐介ブログの著作物はCC BY-NC-ND 4.0で公開されています。<br>\n')
write_lines.append('加藤祐介ブログのソフトウェアはMITライセンスで公開されています。<br>\n')
write_lines.append('&copy; 2023 YusukeKato All Rights Reserved.<br><br>\n')
write_lines.append('<img style="height:22px!important;margin-left:2px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nd.svg?ref=chooser-v1" alt=""><br>\n')
write_lines.append('</h1>\n')

write_lines.append('</body>\n')
write_lines.append('</html>\n')

# 書き込み
with open('../html/index.html', 'w', encoding='UTF-8') as fw:
    fw.writelines(write_lines)

print('output: ../html/index.html')
print('finish: generate index.html')

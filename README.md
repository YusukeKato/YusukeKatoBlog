# YusukeKatoBlog
- Blog URL: https://yusukekato.jp/
- LICENSE : https://github.com/YusukeKato/YusukeKatoBlog/blob/main/LICENSE

# License
- code(.py, .bash, .html, .css, .yaml, etc): [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)
- work(images, text, .jpg, .png, .gif, .mp4, .md, etc): [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode.txt)

# ディレクトリ構成
- hugo.toml：サイト設定
- assets：css
- content：記事markdown
- static：画像
- scripts：画像変換スクリプト
- public：ビルド後の公開HTML

# 記事追加方法

## 記事追加
content/postsにmarkdownを追加

## 画像追加

```sh
# install
sudo apt install ffmpeg
sudo apt install imagemagick

cd scripts
# ex: 2024/08/04
bash resize_images.bash 20240804
# ex: ALL
bash resize_images.bash
```

## 動作確認

```sh
hugo server -D --disableFastRender
```

## デプロイ
mainブランチへpushすると自動でデプロイを実行
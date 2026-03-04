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

```sh
hugo new posts/2026/0305.md
```

[0305.md](https://github.com/YusukeKato/YusukeKatoBlog/blob/main/content/posts/2026/0305.md) を参考にしてページを編集

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
# 下書きも表示する
hugo server -D --disableFastRender
# 本番
hugo server
```

## デプロイ
mainブランチへpushすると自動でデプロイを実行
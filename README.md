# YusukeKatoBlog
- Blog URL: https://yusukekato.jp/
- LICENSE : https://github.com/YusukeKato/YusukeKatoBlog/blob/main/LICENSE

# License
- code(.py, .bash, .html, .css, .yaml, etc): [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)
- work(images, text, .jpg, .png, .gif, .mp4, .md, etc): [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode.txt)

# ディレクトリ構成
- hugo.toml：サイト設定
- assets：記事内画像、css
- content：記事markdown
- static：汎用画像
- scripts：画像変換スクリプト
- public：ビルド後の公開HTML

# 環境
- hugo v0.154.5

```sh
sudo apt install hugo
```

# 記事追加方法

## 記事追加
content/postsにmarkdownを追加

```sh
hugo new posts/2026/0305.md
```

[0305.md](https://github.com/YusukeKato/YusukeKatoBlog/blob/main/content/posts/2026/0305.md) を参考にしてページを編集

## 数式

数式を使う記事は、冒頭のフロントマターに `math: true` を設定してください。
`math: false` または未指定の記事では数式表示を有効にしません。
有効な記事だけMathJaxをCDNから読み込みます。

文章中は `\(...\)`、独立した数式は `$$...$$` または `\[...\]` で囲みます。
コードとして扱われるため、数式をバッククォートで囲まないでください。

```markdown
標準化には \( Z = \frac{x - \mu}{\sigma} \) を使います。

$$
S = \sum_{i=1}^{n} x_i^2 - \frac{\left(\sum_{i=1}^{n} x_i\right)^2}{n}
$$
```

設定の参考：[Hugo公式ドキュメント](https://gohugo.io/content-management/mathematics/)

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

初回のみ、PaperModサブモジュールを取得する。

```sh
git submodule update --init --recursive
```

```sh
# 下書きも表示する（ローカル用）
hugo server -D --disableFastRender
# 下書きなし（ローカル用）
hugo server
# 本番環境用
hugo
```

## デプロイ
mainブランチへpushすると自動でデプロイを実行

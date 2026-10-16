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

## 日本語文章のチェック（textlint）

Node.js 22以上とnpmを使います。推奨はNode.js 24です。
nvmを使っている場合は、リポジトリのルートで `nvm install`、`nvm use` を実行すると `.nvmrc` のバージョンを使えます。
WSL上のリポジトリでは、以下のコマンドもWSLのターミナルで実行してください。

```sh
# 初回とpackage-lock.json更新時に依存パッケージをインストール
npm ci

# content以下の全Markdownをチェック（下書きも含む）
npm run lint:text

# 執筆中の記事だけチェック
npm run lint:text:file -- content/posts/2026/0305.md

# 指定した記事の自動修正に対応する指摘を修正
npm run lint:text:fix -- content/posts/2026/0305.md
```

自動修正はファイルを書き換えるので、実行後に `git diff` で内容を確認してください。
自動修正できない指摘は手作業で直します。
指摘が残っている場合、チェックは終了コード1を返します。
既存記事にも指摘があるため、まずは執筆・更新する記事を指定して使います。
デプロイのGitHub Actionsには組み込んでいません。

### チェックする内容

設定は `.textlintrc.json` にあります。

- `preset-ja-technical-writing`：1文90文字以内、読点3個以内、助詞や単語の重複、二重否定、ら抜き言葉、誤用、冗長表現、括弧の対応などをチェックします。
- 本文は「ですます調」、箇条書きは「である調」を基本にします。見出しは文体を指定せず、体言止めも使えます。
- `preset-jtf-style`：全角・半角、句読点、括弧、スペース、助数詞などの表記をチェックします。文体と漢数字の重複ルールは無効にしています。
- 個人ブログの語り口を残すため、「と思います」「かもしれません」と感嘆符・疑問符は許容します。和文の感嘆符・疑問符は全角に統一します。

通常のMarkdown本文が対象です。YAMLフロントマター、コードブロック、インラインコードは文章としてチェックしません。
Hugoのショートコードはタグ部分を除外し、開始タグと終了タグの間にある本文はチェックします。
テーマ、生成物、記事テンプレートなどは `.textlintignore` で除外しています。
文章の事実関係や技術的な正しさは、別途確認してください。

### 意図した表現が指摘された場合

引用、固有名詞、数式などをそのまま残す場合は、理由を添えて必要な範囲・ルールだけ除外します。
ルール名は実行結果に表示される名前を指定し、コメントの前後には空行を入れてください。

```markdown
<!-- 書名の表記をそのまま使うため -->
<!-- textlint-disable ja-technical-writing/max-kanji-continuous-len -->

『情報処理技術者試験』を読みました。

<!-- textlint-enable ja-technical-writing/max-kanji-continuous-len -->
```

設定の参考：

- [textlint公式の導入手順](https://textlint.org/docs/getting-started/)
- [技術文書向けプリセットの設定例・ルール一覧](https://github.com/textlint-ja/textlint-rule-preset-ja-technical-writing)
- [JTF日本語標準スタイルガイドのプリセット](https://github.com/textlint-ja/textlint-rule-preset-JTF-style)
- [コメントによる例外指定](https://github.com/textlint/textlint-filter-rule-comments)

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

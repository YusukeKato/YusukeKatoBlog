# YusukeKatoBlog

[公開ブログ](https://yusukekato.jp/)のHugoリポジトリです。テーマはPaperModを使っています。

## セットアップ

以下のコマンドはリポジトリのルートで実行します。

| ツール | 用途・バージョン |
| --- | --- |
| Hugo extended | 0.154.5。ローカルとGitHub Actionsでそろえます |
| Git | PaperModサブモジュールの取得 |
| Node.js・npm | textlint用。Node.js 22以上、推奨は24（.nvmrc） |
| FFmpeg・ImageMagick | 画像・動画を変換するときに使用 |

Hugoは[0.154.5のリリース](https://github.com/gohugoio/hugo/releases/tag/v0.154.5)からOS・CPUに合うextended版を取得してください。[公式のLinux導入手順](https://gohugo.io/installation/linux/)も参考になります。Ubuntuのパッケージ版は環境によってバージョンが異なるため、インストール後に確認します。

```sh
hugo version
git submodule update --init --recursive

# nvmを使っている場合
nvm install
nvm use

# 初回とpackage-lock.json更新時
npm ci

# 画像変換を使う場合（Ubuntu）
sudo apt install ffmpeg imagemagick
```

## よく使うコマンド

```sh
# 下書きも含めてプレビュー
hugo server -D --disableFastRender

# 公開する記事だけプレビュー
hugo server

# 編集した記事の日本語をチェック
npm run lint:text:file -- content/posts/2026/0305.md

# GitHub Actionsと同じ条件でビルド
hugo --minify --printPathWarnings --panicOnWarning

# 画像変換スクリプトの動作をテスト（変換処理と失敗時の既存ファイル保護を確認）
bash scripts/tests/resize_images.bash

# 変更内容と空白の不備を確認
git diff
git diff --check
```

## フォルダと生成の流れ

| パス | 役割 |
| --- | --- |
| hugo.toml | URL、メニュー、画像配信、数式などのサイト設定 |
| content/posts/YYYY/MMDD.md | 記事のMarkdown。about.mdは固定ページ |
| content/tags/*/_index.md | タグの日本語表示名 |
| content/_index.md・content/archives.md | トップページ・記事一覧の設定 |
| archetypes/default.md | 新しい記事のテンプレート |
| assets/images/YYYY/ | 記事用の画像・動画 |
| assets/css/extended/ | サイト独自のCSS |
| static/images/ | アイコン・SNS用画像などの共通素材 |
| layouts/ | PaperModに追加・上書きするテンプレート |
| themes/PaperMod/ | Gitサブモジュールで固定したテーマ |
| scripts/ | 画像・動画の変換スクリプト |
| public/・resources/ | 公開ファイル・画像処理キャッシュなどの生成物 |

Hugoは記事・設定・テンプレートからHTMLを生成し、公開ファイルを `public/` に出力します。`public/` と `resources/` はGit管理対象外で、直接編集しません。

記事画像は `hugo.toml` のマウント設定でHugoの画像処理と `/images/` の静的配信に共用します。`assets/images/` から `static/images/` への事前コピーは不要です。Markdownの画像には `layouts/_markup/render-image.html` が適用されます。

ブラウザー用の16px・32pxアイコンと180pxのApple Touchアイコンは、`static/images/BlueTreeIcon.jpg` から `layouts/_partials/favicons.html` で生成します。

## 記事の作成・公開

新しい日付のファイルを作成します。以下の日付は執筆日に置き換えてください。

```sh
hugo new content posts/2026/1016.md
```

冒頭のフロントマターを埋め、本文を追加します。[既存記事の例](https://github.com/YusukeKato/YusukeKatoBlog/blob/main/content/posts/2026/0305.md)も参考にしてください。

| 項目 | 設定内容 |
| --- | --- |
| title | 記事のタイトル |
| description | 記事の短い説明。生成時は空欄 |
| date | 公開日時。記事URLの年にも使われます |
| lastmod | 内容を更新した日時 |
| draft | 新規記事はtrue。公開するときにfalseへ変更 |
| tags | タグの識別子。例：["tech", "ros2"] |
| cover.image | 一覧などに使う画像のURL。使わない場合は空欄のまま |
| math | 数式を使う記事だけtrue |

一覧用画像を本文にも載せる場合は、本文にも画像のMarkdownを書きます。既存タグの識別子は `content/tags/` で確認できます。新しいタグに日本語名を付ける場合は `content/tags/識別子/_index.md` を作り、`title` を設定します。

`hugo server -D` で内容を確認し、公開時に `draft: false` に変更して本番用ビルドを確認します。未来の日時を `date` に指定した記事は通常のビルドに含まれません。公開日時に自動でビルドする仕組みはありません。

記事URLは `hugo.toml` の `/html/:year/:contentbasename.html` で決まります。公開済み記事のファイル名や `date` の年を変えるとURLも変わるため、通常の更新では維持して `lastmod` を更新します。`about.md` は独自の `url` を持つ固定ページです。

設定の詳細：[Hugoのフロントマター](https://gohugo.io/content-management/front-matter/)

### 数式

`math: true` の記事だけMathJaxをCDNから読み込みます。`math: false` または未指定の記事では有効にしません。

文章中は `\(...\)`、独立した数式は `$$...$$` または `\[...\]` で囲みます。バッククォートで囲むとコードになるため、数式自体は囲みません。

```markdown
標準化には \( Z = \frac{x - \mu}{\sigma} \) を使います。

$$
S = \sum_{i=1}^{n} x_i^2 - \frac{\left(\sum_{i=1}^{n} x_i\right)^2}{n}
$$
```

設定の参考：[Hugoの数式表示](https://gohugo.io/content-management/mathematics/)

## 画像・動画の追加

原本を `assets/images/YYYY/` に置き、ファイル名を `YYYYMMDD_01.png` など日付で始めます。原本は別途バックアップしてください。`assets/images/` 以下は原本も含めて公開されるので、非公開で保管する原本はリポジトリ外で管理します。

```sh
# 対象と出力先を確認（変換しない）
bash scripts/resize_images.bash --dry-run 20261016

# 指定日の原本を変換
bash scripts/resize_images.bash 20261016

# 保管されているすべての原本を対象にする
bash scripts/resize_images.bash --dry-run --all
bash scripts/resize_images.bash --all
```

スクリプトは実行ディレクトリに依存せず、日付または `--all` の指定が必要です。PNG・JPEGはJPEG、GIFはGIF、MP4はMP4へ変換します。

生成ファイルは `20261016_01.png.jpg`、`20261016_02.gif.gif` のような二重拡張子になります。既存の記事URLとの互換性のため、この命名を維持しています。生成済みの二重拡張子ファイルは入力にせず、変換が成功した場合だけ出力を置き換えます。原本を削除せず、失敗した場合は既存の出力を残します。

原本がない過去の画像は再変換できません。変換後に画像・動画を開いて確認し、記事では生成されたファイル名を指定してください。

```markdown
![画像の説明](/images/2026/20261016_01.png.jpg)
```

## 日本語文章のチェック（textlint）

```sh
# content以下の全Markdownをチェック（下書きも含む）
npm run lint:text

# 執筆中の記事だけチェック
npm run lint:text:file -- content/posts/2026/0305.md

# 指定した記事の自動修正に対応する指摘を修正
npm run lint:text:fix -- content/posts/2026/0305.md
```

自動修正はファイルを書き換えるので、実行後に `git diff` で内容を確認してください。自動修正できない指摘は手作業で直します。

指摘が残る場合は終了コード1を返します。既存記事にも指摘があるため、まずは執筆・更新する記事を指定して使います。GitHub Actionsの必須チェックには組み込んでいません。

### チェックする内容

設定は `.textlintrc.json` にあります。

- `preset-ja-technical-writing`：1文90文字以内、読点3個以内、助詞や単語の重複、二重否定、ら抜き言葉、誤用、冗長表現、括弧の対応など。
- 本文は「ですます調」、箇条書きは「である調」が基本。見出しは文体を指定せず、体言止めも使えます。
- `preset-jtf-style`：全角・半角、句読点、括弧、スペース、助数詞など。文体と漢数字の重複ルールは無効にしています。
- 個人ブログの語り口を残すため、「と思います」「かもしれません」と感嘆符・疑問符を許容。和文の感嘆符・疑問符は全角に統一します。

通常のMarkdown本文が対象です。YAMLフロントマター、コードブロック、インラインコードは文章としてチェックしません。Hugoのショートコードはタグ部分を除外し、開始タグと終了タグの間にある本文をチェックします。テーマ、生成物、記事テンプレートなどは `.textlintignore` で除外しています。

機械的な指摘がすべて文章の誤りとは限りません。意図した表現かどうかを判断し、文章の事実関係や技術的な正しさは別途確認してください。

### 意図した表現を残す場合

引用、固有名詞、数式などをそのまま残す場合は、理由を添えて必要な範囲・ルールだけ除外します。ルール名は実行結果に表示される名前を指定し、コメントの前後には空行を入れてください。

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

## デプロイと保守

GitHub Actionsの設定は `.github/workflows/deploy.yaml` にあります。

- プルリクエストではHugoのビルドと画像変換スクリプトのテストを実行します。
- `main` へのpushでビルド後に `public/` をサーバーへ配信します。
- 手動実行も可能ですが、配信するのは `main` を選んだ場合だけです。

接続先はGitHub ActionsのSecretsに設定します。必要な名前は `SSH_HOST_YUSUKEKATOJP`、`SSH_USERNAME_YUSUKEKATOJP`、`SSH_PRIVATE_KEY_YUSUKEKATOJP`、`SSH_PORT_YUSUKEKATOJP` です。配信はrsyncの `--delete` を使い、サーバーの公開ディレクトリを `public/` に合わせます。

テーマの取得は `git submodule update --init --recursive` でリポジトリが指定するコミットに合わせます。独自変更は `layouts/` と `assets/css/extended/` に置きます。

Hugo・テーマ・npm依存関係を更新した場合は、バージョン設定も合わせて更新し、ビルドと代表的な記事の表示を確認してください。画像の削除や改名は既存URLにも影響するため、記事内参照に加えて外部から使われている可能性も確認します。

### 既存素材の未解決事項

`assets/images/2024/20240831_{1,2,3}.mp4.mp4` と `20241026_{1,2,3,4,5,6}.mp4.mp4` の計9本は0バイトです。`content/posts/2024/0831.md` と `1026.md` から参照されていますが、再生には元データの再取得が必要です。参照が見つからない素材も、外部での利用状況が分からないため保持しています。

PaperModが参照する `safari-pinned-tab.svg` は未配置です。Safariのピン留めタブ用に、サイトアイコンの単色SVGを別途用意する必要があります。

## ライセンス

- コード（.py、.bash、.html、.css、.yamlなど）：[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)
- 文章・画像・動画など（.md、.jpg、.png、.gif、.mp4など）：[CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode.txt)

詳細は [LICENSE](LICENSE) を参照してください。

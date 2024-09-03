# YusukeKatoBlog
- Blog URL: https://yusukekato.jp/
- LICENSE : https://github.com/YusukeKato/YusukeKatoBlog/blob/main/LICENSE

# License
- code(.py, .bash, .html, .css, .yaml, etc): [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)
- work(images, text, .jpg, .png, .gif, .mp4, .md, etc): [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode.txt)

## How to update blog

### Workflows
1. Write articles (ex: [markdown/2024/0403.md](https://github.com/YusukeKato/YusukeKatoBlog/blob/main/markdown/2024/0403.md))
2. Resize images
3. Update remote repository

Automatically deployed with GitHub Actions.

### Resize images
Execute the following command:
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

### Update remote repository
Execute the following command:
```sh
git add -A
git commit -m "update"
git push origin main
```

## Repository info.

### Deploying with GitHub Actions
Setup file: [workflows/deploy.yaml](https://github.com/YusukeKato/YusukeKatoBlog/blob/main/.github/workflows/deploy.yaml)

### Markdown To HTML
Conversion script: [scripts/md2html.py](https://github.com/YusukeKato/YusukeKatoBlog/blob/main/scripts/md2html.py)

### Generate index.html
Python script: [scripts/generate_index.py](https://github.com/YusukeKato/YusukeKatoBlog/blob/main/scripts/generate_index.py)

### Generate sitemap.xml
Python scripts: [scripts/generate_sitemap.py](https://github.com/YusukeKato/YusukeKatoBlog/blob/main/scripts/generate_sitemap.py)

### Update scripts
- Bash scripts:
  - [scripts/local_update.bash](https://github.com/YusukeKato/YusukeKatoBlog/blob/main/scripts/local_update.bash)
  - [scripts/server_update.bash](https://github.com/YusukeKato/YusukeKatoBlog/blob/main/scripts/server_update.bash)

# YusukeKatoBlog
Blog URL: https://yusukekato.jp/

# Deploying with GitHub Actions
Setup File: [workflows/deploy.yaml](https://github.com/YusukeKato/YusukeKatoBlog/blob/main/.github/workflows/deploy.yaml)

# Markdown To HTML
Conversion Script: [scripts/md2html.py](https://github.com/YusukeKato/YusukeKatoBlog/blob/main/scripts/md2html.py)

# Generate index.html
Python Script: [scripts/generate_index.py](https://github.com/YusukeKato/YusukeKatoBlog/blob/main/scripts/generate_index.py)

# Generate sitemap.xml
Python Scripts: [scripts/generate_sitemap.py](https://github.com/YusukeKato/YusukeKatoBlog/blob/main/scripts/generate_sitemap.py)

# Update Scripts
- Bash Scripts:
  - [scripts/local_update.bash](https://github.com/YusukeKato/YusukeKatoBlog/blob/main/scripts/local_update.bash)
  - [scripts/server_update.bash](https://github.com/YusukeKato/YusukeKatoBlog/blob/main/scripts/server_update.bash)

# How To Update Blog
1. Write articles (ex: [markdown/2024/0403.md](https://github.com/YusukeKato/YusukeKatoBlog/blob/main/markdown/2024/0403.md))
2. `git push` remote repository
3. Deploying with GitHub Actions

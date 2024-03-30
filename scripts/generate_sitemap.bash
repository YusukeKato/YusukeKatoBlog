# generate sitemap.xml
if type 'python3' > /dev/null 2>&1; then
	python3 generate_sitemap.py
else
	python generate_sitemap.py
fi

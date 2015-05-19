all:
	cat html.pre > index.html
	cat README.md $(shell ls *.md |grep -v LICENSE |grep -v README |sort) |markdown >> index.html
	cat html.post >> index.html

test:
	python check-all.py

clean:
	rm -f index.html

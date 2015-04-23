all:
	cat README.md $(shell find . -name \*.md |grep -v LICENSE |grep -v README |sort) |markdown > index.html

clean:
	rm -f index.html

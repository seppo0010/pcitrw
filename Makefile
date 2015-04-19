all:
	cat README.md $(shell find . -name \*.md |grep -v LICENSE |grep -v README) |markdown > index.html

clean:
	rm -f index.html

all:
	mkdir -p output
	cat README.md $(shell find . -name \*.md |grep -v LICENSE |grep -v README) |markdown > output/index.html

clean:
	rm -rf output

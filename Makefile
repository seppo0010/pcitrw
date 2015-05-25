all:
	python create-html.py > index.html
	tar -czf tarball.tgz *.{html,jpg,png}

test:
	python check-all.py

clean:
	rm -f index.html

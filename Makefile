.PHONY: test

test:
	nosetests

README.rst: README.md
	pandoc -f markdown -t rst <README.md >README.rst

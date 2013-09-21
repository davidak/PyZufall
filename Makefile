#
# pyzufall Makefile
# -----------------
#

all: test

docs: html pdf

test:
	@(nosetests -v --with-coverage --cover-package=pyzufall)

html:
	@(cd doc; make html)

pdf:
	@(cd doc; make latexpdf)

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +

release:
	python3 setup.py sdist upload

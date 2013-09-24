#
# pyzufall Makefile
# -----------------
#

all: test

docs: html pdf

test:
	@(nosetests)

html:
	@(cd doc; make html)

pdf:
	@(cd doc; make latexpdf)

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	rm -r __pycache__
	rm -r pyzufall/__pycache__

sdist:
	python3 setup.py sdist

release:
	python3 setup.py sdist upload

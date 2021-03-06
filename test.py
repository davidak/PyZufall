#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Unittests für PyZufall.

Ausführen mit::

	make test

oder mit coverage::

	nosetests -v --with-coverage --cover-package=pyzufall --with-doctest
"""

import re
from functools import wraps
from pyzufall.helfer import re_satz, re_frage
from pyzufall.satz import satz, satz_frage
from pyzufall.generator import sprichwort


def multi(fn):
	"""
	Wrapper, um eine Funktion 1000 mal auszuführen.
	"""
	@wraps(fn)
	def wrapper():
		for n in range(0,1000): # Anzahl
			fn()
	return wrapper


@multi
def test_satz():
	s = satz()
	print(s)
	assert re.match(re_satz, s)

@multi
def test_satz_frage():
	s = satz_frage()
	assert re.match(re_frage, s)

@multi
def test_sprichwort():
	s = sprichwort()
	print(s)
	assert re.match(re_satz, s)

def main():
	import nose
	nose.main()

if __name__ == "__main__":
	main()

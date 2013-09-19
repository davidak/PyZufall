#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Unittests für das Modul pyzufall.satz
"""

_multiprocess_can_split_ = True

import re
from functools import wraps
from pyzufall.satz import satz, satz_frage

anzahl = 1000
def multi(fn):
	"""
	Wrapper, um eine Funktion mehrfach auszuführen.
	"""
	@wraps(fn)
	def wrapper():
		for n in range(anzahl):
			fn()
	return wrapper

@multi
def test_satz():
	s = satz()
	print(s)
	assert re.match(r'^[A-ZÄÖÜ]{1}[a-zA-Z0-9éäÄöÖüÜß ,-/.?"()]+[.!?]?$', s)

@multi
def test_satz_frage():
	s = satz_frage()
	assert re.match(r'^[A-ZÄÖÜ]{1}[a-zA-Z0-9éäÄöÖüÜß ,-/"()]+[?]{1}$', s)

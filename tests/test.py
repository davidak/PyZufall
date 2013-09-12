#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Unittests für pyzufall.

nosetests -v --with-coverag
"""

_multiprocess_can_split_ = True

import re
import random
from functools import wraps
from pyzufall.satz import satz, satz_frage
from pyzufall.helfer import lese, erste_gross

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

def test_test():
	assert True

def test_lese():
	liste = lese('baeume')
	assert liste

@multi
def test_satz():
	s = satz()
	print(s)
	assert re.match(r'^[A-ZÄÖÜ]{1}[a-zA-Z0-9éäÄöÖüÜß ,-/.?"()]+[.!?]?$', s)

def test_erste_gross():
	for i in ['das ist ein Test?', 'älter als das Internet!', 'über Stock und Stein.']:
		text = erste_gross(i)
		print(text)
		assert re.match(r'^[A-ZÄÖÜ]{1}[a-zA-Z0-9äÄöÖüÜß ,-/.!?]+?$', text)

@multi
def test_satz_frage():
	s = satz_frage()
	assert re.match(r'^[A-ZÄÖÜ]{1}[a-zA-Z0-9éäÄöÖüÜß ,-/"()]+[?]{1}$', s)
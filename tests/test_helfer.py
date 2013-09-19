#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Unittests für das Modul pyzufall.helfer
"""

import re
from pyzufall.helfer import lese, erste_gross

def test_lese():
	liste = lese('baeume.txt')
	assert liste

def test_erste_gross():
	for i in ['das ist ein Test?', 'älter als das Internet!', 'über Stock und Stein.']:
		text = erste_gross(i)
		print(text)
		assert re.match(r'^[A-ZÄÖÜ]{1}[a-zA-Z0-9äÄöÖüÜß ,-/.!?]+?$', text)

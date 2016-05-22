#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
pyzufall.helfer
---------------

Stellt diverse Hilfsfunktionen bereit.
"""

from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import *

import os, sys
import codecs
import random as r
from datetime import datetime, date

# Regex Pattern
re_wort = r'^[A-Za-zäÄöÖüÜß-]+$'
re_worte = r'^[A-Za-zäÄöÖüÜß -]+$'
re_liste = r'^[A-Za-zäÄöÖüÜß -]+,[A-Za-zäÄöÖüÜß, -]+'
re_datum = r'^(0[1-9]|[12][0-9]|3[01]).(0[1-9]|1[0-2]).(19|20)[0-9]{2}$'
re_email = r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'
re_satz = r'^[A-ZÄÖÜ]{1}[a-zA-Z0-9éäÄöÖüÜß ,-/.?"()]+[.!?]{1}$'
re_frage = r'^[A-ZÄÖÜ]{1}[a-zA-Z0-9éäÄöÖüÜß ,-/"()]+[?]{1}$'


def lese(dateiname):
	"""
	Liest die Textdatei mit dem übergebenen Namen aus data/ zeilenweise ein und gib eine Liste zurück.

	Beispiel:

	>>> liste = lese('baeume.txt')

	`<http://stackoverflow.com/questions/10174211/make-an-always-relative-to-current-module-file-path>`_

	:param dateiname: Dateiname inklusive Endung, z.B. *vornamen.txt*
	:type dateiname: string
	:rtype: list

	.. only:: doctest

		# überprüfe ob liste eine liste ist
		>>> assert isinstance(liste, list)
	"""
	dateipfad = os.path.join(os.path.dirname(__file__), 'data/' + dateiname)
	return codecs.open(dateipfad, 'r', 'utf-8').read().splitlines()


def chance(wahrscheinlichkeit, wert):
	"""
	Der übergebene Wert wird mit der gewählten Wahrscheinlichkeit zurückgegeben.

	.. versionadded:: 0.11
	
	:param wahrscheinlichkeit: int zwischen 1 und 100
	:param wert: string
	"""
	if r.randint(1, 100) <= wahrscheinlichkeit:
		return wert
	else:
		return ''


def erste_gross(s):
	"""
	Macht den ersten Buchstaben gross.

	Beispiele:

	>>> a = erste_gross('das ist ein Beispiel?')

	>>> print(a)
	Das ist ein Beispiel?

	>>> b = erste_gross('über Stock und Stein.')

	>>> print(b)
	Über Stock und Stein.

	>>> c = erste_gross('älter als das Internet!')

	>>> print(c)
	Älter als das Internet!
	"""
	return s[0].upper() + s[1:]


def str_add(wort, string):
	"""
	Fügt einen String ans Ende eines Wortes an, ohne doppelte Buchstaben zu erzeugen.

	Beispiele:

	>>> a = str_add('feige', 'er')

	>>> print(a)
	feiger

	>>> b = str_add('feige', 'e')

	>>> print(b)
	feige

	>>> c = str_add('blöd', 'e')

	>>> print(c)
	blöde

	.. only:: docstest

		>>> a = str_add('unflexibel', 'e')

		>>> print(a)
		unflexible
		>>> b = str_add('unflexibel', 'er')

		>>> print(b)
		unflexibler

	.. versionadded:: 0.11
	"""
	# wenn der letzte Buchstabe des wortes ist gleich der erste des strings
	if wort[-1] == string[0]:
		# gebe wort + alles ohne den ersten des strings zurück
		s = wort + string[1:]
	else:
		s = wort + string

	# behebt Fehler: unflexibele -> unflexible
	if s[-3:] == 'ele':
		s = s[:-3] + 'le'

	# behebt Fehler: unflexibeler -> unflexibler
	if s[-4:] == 'eler':
		s = s[:-4] + 'ler'

	return s


def aufzaehlung(liste):
	"""
	Erzeugt eine grammatikalisch korrekte Aufzählung aus einer Liste.

	Beispiel:

	>>> a = ['lesen', 'reiten', 'Freunde treffen']

	>>> s = aufzaehlung(a)

	>>> print(s)
	lesen, reiten und Freunde treffen

	>>> b = ['Überwachen', 'Strafen']

	>>> s = aufzaehlung(b)

	>>> print(s)
	Überwachen und Strafen

	>>> c = ['schlafen']

	>>> s = aufzaehlung(c)

	>>> print(s)
	schlafen

	:param liste: Eine Liste von Strings.
	:type liste: list
	:rtype: string

	.. versionadded:: 0.12
	"""
	return "{}{}".format(', '.join(liste[:-2]) + ', ' if len(liste) > 2 else '', ' und '.join(liste[-2:]))


def alter(geburtsdatum):
	"""
	Berechnet das Alter in Jahren anhand des Geburtsdatums.

	:rtype: int

	.. only:: doctest

		>>> s = alter("27.10.1988")

		>>> assert s > 24

	.. versionadded:: 0.12
	"""
	_heute = date.today()
	_geburtstag = datetime.strptime(geburtsdatum, "%d.%m.%Y").date()
	_alter = int((_heute - _geburtstag).days / 365.2425)
	return _alter

def uml(s):
	"""
	Ersetzt Umlaute durch die entsprechenden 2 Buchstaben.

	Beispiel:

	>>> a = uml('Käse')

	>>> print(a)
	Kaese
	>>> b = uml('Brötchen')

	>>> print(b)
	Broetchen
	>>> c = uml('Gefühl')

	>>> print(c)
	Gefuehl

	.. versionadded:: 0.13
	"""
	s = s.replace('ä', 'ae')
	s = s.replace('ü', 'ue')
	s = s.replace('ö', 'oe')
	s = s.replace('ß', 'ss')
	return s

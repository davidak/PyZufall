#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
pyzufall.helfer
---------------

Stellt diverse Hilfsfunktionen bereit.
"""

import os
import random as r

# Regex Pattern
re_wort = r'^[A-Za-zäÄöÖüÜß-]+$'
re_worte = r'^[A-Za-zäÄöÖüÜß -]+$'
re_liste = r'^[A-Za-zäÄöÖüÜß -]+,[A-Za-zäÄöÖüÜß, -]+'
re_datum = r'^(0[1-9]|[12][0-9]|3[01]).(0[1-9]|1[0-2]).(19|20)[0-9]{2}$'
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
	return open(dateipfad, 'r').read().splitlines()


def chance(wahrscheinlichkeit, wert):
	"""
	Der übergebene Wert wird mit der gewählten Wahrscheinlichkeit zurückgegeben.

	.. versionadded:: 0.11
	:param wahrscheinlichkeit: int zwischen 1 und 100
	:param wert: string
	"""
	if r.randint(0,99) < wahrscheinlichkeit:
		return wert
	else:
		return ''


def erste_gross(s):
	"""
	Macht den ersten Buchstaben gross.

	Beispiele:

	>>> erste_gross('das ist ein Beispiel?')
	'Das ist ein Beispiel?'

	>>> erste_gross('über Stock und Stein.')
	'Über Stock und Stein.'

	>>> erste_gross('älter als das Internet!')
	'Älter als das Internet!'
	"""
	return s[0].upper() + s[1:]


def str_add(wort, string):
	"""
	Fügt einen String ans Ende eines Wortes an, ohne doppelte Buchstaben zu erzeugen.

	Beispiele:

	>>> str_add('feige', 'er')
	'feiger'

	>>> str_add('feige', 'e')
	'feige'

	>>> str_add('blöd', 'e')
	'blöde'

	.. versionadded:: 0.11
	"""
	# wenn der letzte Buchstabe des wortes ist gleich der erste des strings
	if wort[-1] == string[0]:
		# gebe wort + alles ohne den ersten des strings zurück
		return wort + string[1:]
	else:
		return wort + string


def aufzaehlung(liste):
	"""
	Erzeugt eine grammatikalisch korrekte Aufzählung aus einer Liste.

	Beispiel:

		>>> a = ['lesen', 'reiten', 'Freunde treffen']

		>>> aufzaehlung(a)
		'lesen, reiten und Freunde treffen'

		>>> b = ['Überwachen', 'Strafen']

		>>> aufzaehlung(b)
		'Überwachen und Strafen'

		>>> c = ['schlafen']

		>>> aufzaehlung(c)
		'schlafen'

	:param liste: Eine Liste von Strings.
	:type liste: list
	:rtype: string

	.. versionadded:: 0.12
	"""
	return "{}{}".format(', '.join(liste[:-2]) + ', ' if len(liste) > 2 else '', ' und '.join(liste[-2:]))


def e16(wert):
	"""
	Der übergebene Wert wird mit einer Wahrscheinlichkeit von 16% zurückgegeben.

	.. deprecated:: 0.11
		Wird durch :func:`pyzufall.helfer.chance` ersetzt.
	"""
	if r.randint(0,5) == 1:
		return wert
	else:
		return ''


def e25(wert):
	"""
	Der übergebene Wert wird mit einer Wahrscheinlichkeit von 25% zurückgegeben.

	.. deprecated:: 0.11
		Wird durch :func:`pyzufall.helfer.chance` ersetzt.
	"""
	if r.randint(1,4) == 1:
		return wert
	else:
		return ''


def e50(wert):
	"""
	Der übergebene Wert wird mit einer Wahrscheinlichkeit von 50% zurückgegeben.

	.. deprecated:: 0.11
		Wird durch :func:`pyzufall.helfer.chance` ersetzt.
	"""
	if r.randint(0,1):
		return wert
	else:
		return ''


def e75(wert):
	"""
	Der übergebene Wert wird mit einer Wahrscheinlichkeit von 75% zurückgegeben.

	.. deprecated:: 0.11
		Wird durch :func:`pyzufall.helfer.chance` ersetzt.
	"""
	if r.randint(0,3):
		return wert
	else:
		return ''

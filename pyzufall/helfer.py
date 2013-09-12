#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random as r


def lese(dateiname):
	"""
	Liest die Datei mit dem übergebenen Namen aus data/ zeilenweise ein und gib eine Liste zurück.

	`<http://stackoverflow.com/questions/10174211/make-an-always-relative-to-current-module-file-path>`_
	"""
	dateipfad = os.path.join(os.path.dirname(__file__), 'data/' + dateiname)
	return open(dateipfad, 'r').read().splitlines()


def e16(wert):
	"""
	Der übergebene Wert wird mit einer Wahrscheinlichkeit von 16% zurückgegeben.
	"""
	if r.randint(0,5) == 1:
		return wert
	else:
		return ''


def e25(wert):
	"""
	Der übergebene Wert wird mit einer Wahrscheinlichkeit von 25% zurückgegeben.
	"""
	if r.randint(1,4) == 1:
		return wert
	else:
		return ''


def e50(wert):
	"""
	Der übergebene Wert wird mit einer Wahrscheinlichkeit von 50% zurückgegeben.
	"""
	if r.randint(0,1):
		return wert
	else:
		return ''


def e75(wert):
	"""
	Der übergebene Wert wird mit einer Wahrscheinlichkeit von 75% zurückgegeben.
	"""
	if r.randint(0,3):
		return wert
	else:
		return ''


def erste_gross(s):
	"""
	Macht den ersten Buchstaben gross.
	"""
	return s[0].upper() + s[1:]


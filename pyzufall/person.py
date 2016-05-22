#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
pyzufall.person
---------------

Stellt die Klasse Person zur Verfügung. Mit ihr kann man ein Objekt erzeugen, dass eine Person mit zufällig generierten Daten darstellt.

Es kann auf jedes Attribut einzeln zugegriffen werden oder mit print(person) alle aufeinmal ausgeben werden.

Die generierten Daten basieren teilweise auf statistischen Werten und versuchen möglichst authentisch zu sein.

Quellen für Statistiken:

- https://www.destatis.de/
- http://de.statista.com/
- https://www.zensus2011.de/
- http://www.statistik2013.de/
"""

from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import *
from future.utils import python_2_unicode_compatible

import random as r

from .helfer import chance, alter
from .generator import geschlecht, geburtsdatum, vorname_m, vorname_w, nachname, nickname, email, homepage, url, stadt, farbe, essen, beilage, sprichwort, beruf_m, beruf_w

# Daten
from .generator import interessen

@python_2_unicode_compatible
class Person(object):
	"""
	Generiert Daten einer zufälligen und fiktiven Person.

	.. versionadded:: 0.9
	"""
	anzahl = 0
	debug = 0 # extern auf 1 setzen

	def __init__(self):
		self.geschlecht = geschlecht()
		if self.geschlecht:
			self.vorname = vorname_m() + chance(10, '-' + vorname_m()) # mit 10%iger Chance ein Doppelname
		else:
			self.vorname = vorname_w() + chance(10, '-' + vorname_w()) # mit 10%iger Chance ein Doppelname

		self.nachname = nachname()
		self.name = self.vorname + ' ' + self.nachname
		self.nickname = nickname(self.vorname, self.nachname)
		self.homepage = homepage(self.vorname, self.nachname, self.nickname)
		self.email = email(self.vorname, self.nachname, self.nickname, self.homepage)
		self.homepage = url(self.homepage) # http:// hinzufügen, nachdem die Domain für die E-Mail genutzt wurde
		self.geburtsdatum = geburtsdatum()
		self.geburtsort = stadt()
		self.alter = alter(self.geburtsdatum)
		if self.alter > 22 and r.randint(1, 100) < 60:
			self.geburtsname = nachname()
		else:
			self.geburtsname = self.nachname
		self.wohnort = stadt()
		self.beruf = Person._gen_beruf(self)
		self.interessen = Person._gen_interessen(self)
		self.lieblingsfarbe = farbe()
		self.lieblingsessen = essen() + chance(50, " mit " + beilage())
		self.motto = sprichwort()

		Person.anzahl += 1
		if Person.debug: print("Neue Person generiert: " + self.name)

	def __del__(self):
		Person.anzahl -= 1
		if Person.debug: print("Person '" + self.name + "' wurde gelöscht.")

	def __str__(self):
		s = "*" * 80 + "\n"
		s += "Name: " + self.name + " (" + self.nickname + ")\n"
		s += "Geburtsname: " + self.geburtsname
		s += "\nGeschlecht: "
		if self.geschlecht:
			s += "männlich"
		else:
			s += "weiblich"
		s += "\nGeburtsdatum: " + self.geburtsdatum + " (" + str(self.alter) + ")\n"
		s += "Geburtsort: " + self.geburtsort + "\n"
		s += "Wohnort: " + self.wohnort + "\n"
		s += "Beruf: " + self.beruf + "\n"
		s += "E-Mail: " + self.email + "\n"
		s += "Homepage: " + self.homepage + "\n"
		s += "Interessen: " + self.interessen + "\n"
		s += "Lieblingsfarbe: " + self.lieblingsfarbe + "\n"
		s += "Lieblingsessen: " + self.lieblingsessen + "\n"
		s += "Motto: " + self.motto + "\n"
		s += "*" * 80 + "\n"
		return s

	def _gen_beruf(self):
		"""
		Generiert den Beruf einer Person anhand des Alters und Statistiken.

		Es wird von 10% Arbeitslosigkeit ausgegangen, die ofizielle Statistik ist allerdings 7,10% im Jahr 2013.
		Quelle: http://de.statista.com/statistik/daten/studie/1224/umfrage/arbeitslosenquote-in-deutschland-seit-1995/

		Es wird angenommen, dass 30% der zwischen 19 und 29 jährigen studieren:
		Studienanfänger 43,3%
		Studienabsolventen: 26,2%
		Quelle: http://de.wikipedia.org/wiki/Abiturientenquote_und_Studienanf%C3%A4ngerquote
		"""
		if self.geschlecht: # männlich
			if self.alter < 6:
				return "kein"
			elif self.alter <= 18:
				return "Schüler"
			elif self.alter > 18 and self.alter < 30 and r.randint(0,100) <= 30: # 30% studieren
				return "Student"
			elif self.alter > 68:
				return "Rentner"
			elif r.randint(0,9): # 1 von 10 arbeitslos
				return beruf_m()
			else:
				return "arbeitslos"
		else: # weiblich
			if self.alter < 6:
				return "kein"
			elif self.alter <= 18:
				return "Schülerin"
			elif self.alter > 18 and self.alter < 30 and r.randint(0,100) <= 30: # 30% studieren
				return "Studentin"
			elif self.alter > 68:
				return "Rentnerin"
			elif r.randint(0,9): # 1 von 10 arbeitslos
				return beruf_w()
			else:
				return "arbeitslos"

	def _gen_interessen(self):
		"""
		Gibt eine Liste mit Interessen zurück.
		"""
		_anzahl = r.randint(1,3)
		if r.randint(0,1): # 50% haben mehr als 3 Interessen, maximal 8
			_anzahl + r.randint(1, 5)
		_s = ', '.join(r.sample(interessen, _anzahl))
		return _s

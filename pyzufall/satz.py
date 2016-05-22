#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
pyzufall.satz
-------------

Stellt Funktionen bereit, die Sätze nach diversen Satz-Schemata generieren.

Die Funktion :py:func:`pyzufall.satz.satz()` beinhaltet alle.
"""

from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import *

import re
import random as r

from .helfer import erste_gross, chance, str_add, aufzaehlung
from .generator import adjektiv, band, bandart, baum, beilage, beruf_m, beruf_w, beziehung_m, beziehung_w, color, datum, essen, farbe, firma, geburtsdatum, gegenstand, interesse, koerperteil, nachname, objekt, objekt_m, objekt_w, ort, person, person_m, person_objekt_m, person_objekt_w, person_w, pflanze, sprichwort, stadt, stadt_bl, tier, trinken, verbd, verbi, verbi2, verbn, verbt, verbt2, vorname, vorname_m, vorname_w, wort, zahl

# Daten
from .generator import adjektive, farben, interessen


def satz_nulltransitiv():
	"""
	Generiert einen Satz mit einem nulltransitiven Verb.

	Beispiel: Im Park schneit es.
	"""
	if r.randint(0,1):
		s = ort() + ' ' + verbn() + ' es' + chance(25, ' ' + adjektiv()) + '.'
	else:
		s = 'Es ' + verbn() + chance(25, ' ' + adjektiv()) + '.'
	return erste_gross(s)


def satz_baum():
	"""
	Generiert einen Satz mit dem Thema Baum.

	Beispiel: Die gnadenlose Kerstin tritt gegen den Apfelbaum.
	"""
	if r.randint(0,1): #männlich
		person = person_m()
		objekt = objekt_m(baum())
	else: # weiblich
		person = person_w()
		objekt = objekt_w(baum())
	s = person + ' ' + r.choice(['pflanzt', 'klettert auf', 'fällt', 'zersägt', 'stellt sich unter', 'umarmt', 'tritt gegen']) + ' ' + objekt + '.'
	return erste_gross(s)


besetzung = ['Sänger', 'Gitarrist', 'Keyboarder', 'Bassist', 'Schlagzeuger', 'Manager', 'Geiger', 'Trompeter', 'Saxophonist', 'Backgroundsänger']
def satz_band_mitglied():
	"""
	Generiert einen Satz, in dem ein Bandmitglied vorgestellt wird.

	Beispiel: Annelise ist Gitarristin von der Gothicband "Kräuter in der Innenstadt".
	"""
	if r.randint(0,1): # männlich
		s = vorname_m() + chance(50, ' ' + nachname()) + ' ist ' + chance(50, 'der ') + r.choice(besetzung) + chance(50, ' von') + ' der ' + bandart() + ' "' + band() + '".'
	else: # weiblich
		s = vorname_w() + chance(50, ' ' + nachname()) + ' ist ' + chance(50, 'die ') + r.choice(besetzung) + 'in' + chance(50, ' von') + ' der ' + bandart() + ' "' + band() + '".'
	return erste_gross(s)


def satz_band_gegruendet():
	"""
	Generiert einen Satz, der den Zeitpunkt einer Bandgründung zum Thema hat.

	Beispiel: Die Electroband "Kartoffel auf dem Klo" wurde am 26.10.2009 in Selb gegründet.
	"""
	if r.randint(0,1):
		s = 'Die ' + bandart() + ' "' + band() + '" wurde '
	else:
		s = band() + ' (' + bandart() + ') wurde '

	if r.randint(0,1): # 50% Datum oder Jahr
		s += 'am ' + datum()
	else:
		s += chance(75, r.choice(['Anfang', 'Mitte', 'Mitte des Jahres', 'Ende', 'im Frühling', 'im Sommer', 'im Herbst', 'im Winter', 'im Jahr'])) + ' ' + str(r.randint(1950, 2013))

	s += chance(50, ' in ' + stadt()) + ' gegründet.'
	return erste_gross(s)


def satz_band_besetzung():
	"""
	Generiert einen Satz mit den Mitgliedern einer Band.

	Beispiel: Die Black Metal Band "Die Oralen Nudeln" besteht aus Marlene, Gert, Stefanie, Timm, Andrej, Friederike und Dorothea.
	"""
	mit_nachname = r.randint(0,1)
	s = 'Die '+ bandart() + ' "' + band() + '" besteht aus ' + vorname()
	if mit_nachname:
		s += ' ' + nachname()
	for i in range(0,r.randint(0,6)): # 2 bis 8 Mitglieder
		s += ', ' + vorname()
		if mit_nachname:
			s += ' ' + nachname()
	s += ' und ' + vorname()
	if mit_nachname:
		s += ' ' + nachname()
	return erste_gross(s) + '.'


def satz_band():
	"""
	Generiert einen zufälligen Satz zum Thema Band.
	"""
	return r.choice([satz_band_mitglied, satz_band_gegruendet, satz_band_besetzung])()


def satz_arbeit():
	"""
	Generiert einen Satz über eine berufstätige Person.

	Beispiel: Achmed, der Grafiker aus Waldheim, spielt den Nasenbär.
	"""
	x = r.randint(1,4)
	if x == 1:
		s = vorname_m() + chance(50, ' ' + nachname()) + ' ist ' + chance(50, 'ein ') + beruf_m() + chance(50, ' aus ' + stadt())
	if x == 2:
		s = vorname_w() + chance(50, ' ' + nachname()) + ' ist ' + chance(75, 'eine ') + beruf_w() + chance(50, ' aus ' + stadt())
	if x == 3:
		s = vorname_m() + chance(50, ' ' + nachname()) + chance(50, ', der ' + beruf_m() + chance(50, ' aus ' + stadt()) + ',') + ' ' + verbt() + ' ' + r.choice([person_objekt_m(), objekt_m(objekt())])
	if x == 4:
		s = vorname_w() + chance(50, ' ' + nachname()) + chance(50, ', die ' + beruf_w() + chance(50, ' aus ' + stadt()) + ',') + ' ' + verbt() + ' ' + r.choice([person_objekt_w(), objekt_w(objekt())])
	return erste_gross(s) + '.'


def satz_essen():
	"""
	Generiert einen Satz mit Essen und/oder Trinken.

	Beispiel: Die Wärterin isst Orangen mit Mayonnaise und trinkt dazu Milch.
	"""
	x = r.randint(1,3)
	if x == 1: # Essen mit Beilage
		s = person() + chance(25, ' ' + r.choice(['ist', 'sitzt', 'befindet sich']) + ' ' + ort() + ' und') + ' isst ' + chance(50, r.choice(['gerade', 'oft', 'nicht oft', 'selten', 'gerne', 'nicht gerne']) + ' ') + essen() + chance(50, ' mit ' + r.choice(['viel', 'ganz viel', 'ein bischen', 'ein wenig', 'lecker', 'einer großen Portion']) + ' ' + beilage())
	if x == 2: # Trinken
		s = person() + ' trinkt ' + chance(50, r.choice(['gerade', 'oft', 'nicht oft', 'selten', 'gerne', 'nicht gerne', 'jeden Abend ein Glas', 'zu viel']) + ' ') + trinken()
	if x == 3: # Essen und Trinken
		s = person() + ' isst ' + essen() + chance(50, ' mit ' + beilage()) + ' und trinkt ' + chance(50, 'dazu ') + trinken()
	return erste_gross(s) + '.'


def satz_koerperteil():
	"""
	Generiert einen Satz zum Thema Körperteile.

	Beispiel: Die ekelhafte Oma massiert ihren Fuß.
	"""
	x = r.randint(1,5)
	if x == 1:
		if r.randint(0,1): # Er
			s = koerperteil()
			s = re.sub('der ', 'den ', s)
			if r.randint(0,1):
				s = re.sub('den ', 'seinen ', s)
				s = re.sub('die ', 'seine ', s)
				s = re.sub('das ', 'sein ', s)
			s = person_m() + ' ' + r.choice(['verletzt sich', 'stößt sich', 'bricht' + chance(50, ' sich'), 'verstaucht' + chance(50, ' sich'), 'massiert']) + ' ' + s
		else: # Sie
			s = koerperteil()
			s = re.sub('der ', 'den ', s)
			if r.randint(0,1):
				s = re.sub('den ', 'ihren ', s)
				s = re.sub('die ', 'ihre ', s)
				s = re.sub('das ', 'ihr ', s)
			s = person_w() + ' ' + r.choice(['verletzt sich', 'stößt sich', 'bricht' + chance(50, ' sich'), 'verstaucht' + chance(50, ' sich'), 'massiert']) + ' ' + s
	if x == 2: # hat Kopfschmerzen
		s = koerperteil()
		s = re.sub('e$', 'en', s) # Lungen
		s = s.split()[1] # Körperteil ohne Artikel
		s = person() + ' hat ' + chance(50, r.choice(['schlimme', 'ein bischen', 'brutale', 'oft', 'manchmal']) + ' ') + s + 'schmerzen'
	if x == 3:
		s = koerperteil()
		s = re.sub('der ', 'am ', s)
		s = re.sub('die ', 'an der ', s)
		s = re.sub('das ', 'am ', s)
		s = person() + ' hat eine ' + chance(25, r.choice(['schmerzhafte ', 'brutale ', 'miese ', 'kleine ', 'eiternde '])) + r.choice(['Verletzung', 'Entzündung', 'Wunde', 'Beschädigung']) + ' ' + s
	if x == 4:
		s = koerperteil()
		s = re.sub('der ', 'Mein ', s)
		s = re.sub('die ', 'Meine ', s)
		s = re.sub('das ', 'Mein ', s)
		s = s + ' ' + r.choice(['tut weh', 'schmerzt', 'blutet', 'juckt', 'brennt', 'stinkt'])
	if x == 5:
		s = koerperteil()
		s = re.sub('der ', 'einen ' + str_add(adjektiv(), 'en '), s)
		s = re.sub('die ', 'eine ' + str_add(adjektiv(), 'e '), s)
		s = re.sub('das ', 'ein ' + str_add(adjektiv(), 'es '), s)
		s = person() + ' hat ' + s
	return erste_gross(s) + '.'


def satz_kloster():
	"""
	Generiert einen Satz über eine Person in einem Kloster.

	Beispiel: Bruder Ludwig ist der böseste Mönch im Kloster.
	"""
	_adj = adjektiv()
	# verhindert 'monströsste' und 'gerechtste'
	if _adj[-1] == 's' or _adj[-1] == 't':
		_adj += 'este'
	else:
		_adj += 'ste'
	if r.randint(0,1): # männlich
		s = chance(25, 'Der ') + 'Bruder ' + vorname_m() + r.choice([' war', ' ist']) + ' der ' + _adj + ' Mönch ' + r.choice(['im Kloster', 'im Orden', 'in der Abtei'])
	else: # weiblich
		s = chance(25, 'Die ') + 'Schwester ' + vorname_w() + r.choice([' war', ' ist']) + ' die ' + _adj + ' Nonne ' + r.choice(['im Kloster', 'im Orden', 'in der Abtei'])
	return erste_gross(s) + '.'


def satz_folgehandlung():
	"""
	Generiert einen Satz, der eine Folgehandlung beschreibt.

	Beispiel: Ohne dass Irmgard überlebt, bricht sie aggressiv ein.
	"""
	v1, v2 = verbi2().split(", ")
	v12 = ''
	if ' ' in v1: # bildet sich => bilder ER sich
		v1, v12 = v1.split(' ')
		v12 += ' '
	
	verb2 = verbi()
	verb22 = ' '
	if ' ' in verb2:
		verb2, verb22 = verb2.split(' ')
		verb22 = ' ' + verb22 + ' '
	
	if r.randint(0,3): # Selbst
		if r.randint(0,1): # m
			erste_person, zweit_person = person_m(), ' er '
		else: # w
			erste_person, zweit_person = person_w(), ' sie '
	else: # Dritte
		if r.randint(0,1): # m
			erste_person, zweit_person = person_m(), r.choice([' sein ' + r.choice(beziehung_m), ' seine ' + r.choice(beziehung_w)]) + ' '
		else: # w
			erste_person, zweit_person = person_w(), r.choice([' ihr ' + r.choice(beziehung_m), ' ihre ' + r.choice(beziehung_w)]) + ' '
	
	s = r.choice(['Weil', 'Während', 'Obwohl', 'Ohne dass', 'Nur weil', 'Gerade weil']) + r.choice([verb22 + erste_person + ' ', ' ' + erste_person + verb22]) + chance(50, ort() + ' ') + chance(50, adjektiv() + ' ') + verb2 + ', ' + v1 + zweit_person + v12 + chance(50, adjektiv() + ' ') + v2 + '.'
	return erste_gross(s)


def satz_absurde_farbfunktion():
	"""
	Generiert einen Satz nach folgendem Muster: Gelb ist brauner als Türkis.
	"""
	farbe1, farbe2, farbe3 = r.sample(farben, 3)
	s = farbe1 + ' ist ' + str_add(r.choice([farbe2.lower, adjektiv])(), 'er') + ' als ' + farbe3 + '.'
	return erste_gross(s)


def satz_freunde_lieben():
	"""
	Generiert einen Satz über eine Person mit Eigenschaften.

	Beispiel: In der Garage ist das Mannsweib lesbisch.
	"""
	if r.randint(0,1): #männlich
		s = person_m() + ' ist ' + adjektiv() + chance(50, r.choice(['. Alle', ', aber']) + ' seine Freunde lieben ihn dafür') + '.'
	else: #weiblich
		s = person_w() + ' ist ' + adjektiv() + chance(50, r.choice(['. Alle', ', aber']) + ' ihre Freunde lieben sie dafür') + '.'
	return erste_gross(s)


def satz_farbe():
	"""
	Generiert einen Satz nach dem Muster: Braun ist eine unsittliche Farbe.
	"""
	s = farbe() + ' ist eine ' + str_add(adjektiv(), 'e ') + 'Farbe.'
	return erste_gross(s)


def satz_adjektiv_sprichwort():
	"""
	Generiert einen Satz nach dem Muster: Je untrainierter desto lächerlicher.
	"""
	_adj1, _adj2 = r.sample(adjektive, 2)
	_s = 'Je ' + str_add(_adj1, 'er') + ' desto ' + str_add(_adj2, 'er.')
	return erste_gross(_s)


def satz_adjektiv_am_ort():
	"""
	Generiert einen Satz nach dem Muster: <Ort> <Verb> <Person> <Adjektiv>.

	Beispiel: Auf dem Spielplatz ist die Freundin hilfsbereit.
	"""
	s = ort() + ' ' + r.choice(['war', 'ist']) + ' ' + person() + ' ' + chance(50, r.choice(['sehr', 'ziemlich', 'ein bischen', 'nicht sehr', 'garnicht', 'nicht']) + ' ') + adjektiv() + '.'
	return erste_gross(s)


def satz_interessen():
	"""
	Generiert einen Satz über die Interessen einer Person.
	"""
	if r.randint(0,1):
		_s = "{} Interessen sind {}.".format(str_add(vorname(), 's'), aufzaehlung(r.sample(interessen, r.randint(2,6))))
	else:
		_s = "{} zählt zu {} Interessen.".format(interesse(), str_add(vorname(), 's'))
	return erste_gross(_s)


def satz_thema():
	"""
	Generiert einen Satz zu einem zufälligen Thema.
	"""
	return r.choice([satz_nulltransitiv, satz_baum, satz_band, satz_kloster, satz_folgehandlung, satz_freunde_lieben, satz_adjektiv_am_ort, satz_absurde_farbfunktion, satz_farbe, satz_adjektiv_sprichwort, satz_arbeit, satz_essen, satz_koerperteil, satz_interessen])()


def satz_standard_1():
	"""
	Generiert einen einfachen Satz nach dem Muster: <Person> <Verb> <Adjektiv> <Ort>.

	Beispiel: Die Geschmacklose bepisst sich cool in der Kirche.
	"""
	if r.randint(0,1):
		v1, v2 = verbi2().split(",")
	else:
		v1, v2 = verbi(), ''
	s = person() + ' ' + v1 + ' ' + r.choice([adjektiv(), ort(), adjektiv() + ' ' + ort()]) + v2 + '.'
	return erste_gross(s)


def satz_standard_2():
	"""
	Generiert einen einfachen Satz nach dem Muster: <Ort> <Verb> <Person> <Adjektiv>.

	Beispiel: Beim ersten Date flieht er.
	"""
	if r.randint(0,1):
		v1, v2 = verbi2().split(",")
	else:
		v1, v2 = verbi(), ''
	s = ort() + ' ' + v1 + ' ' + person() + chance(75, ' ' + adjektiv()) + v2 + '.'
	return erste_gross(s)


def satz_standard_3():
	"""
	Generiert einen einfachen Satz nach dem Muster: <Adjektiv> <Verb> <Person> <Ort>.

	Beispiel: Gehirntot weint die Schädlingsbekämpferin in der Psychiatrie.
	"""
	if r.randint(0,1):
		v1, v2 = verbi2().split(",")
	else:
		v1, v2 = verbi(), ''
	s = adjektiv() + ' ' + v1 + ' ' + person() + chance(75, ' ' + ort()) + v2 + '.'
	return erste_gross(s)


def satz_standard_4():
	"""
	Generiert einen einfachen Satz nach dem Muster: <Person> <Verb> <Person/Objekt> <Adjektiv> <Ort>.

	Beispiel: Der Ruhige raubt ein Schaf aus.
	"""
	if r.randint(0,1): # männlich
		_person = person_m()
		_objekt = r.choice([person_objekt_m(), objekt_m(objekt())])
	else: # weiblich
		_person = person_w()
		_objekt = r.choice([person_objekt_w(), objekt_w(objekt())])

	if r.randint(0,1): # getrenntes Verb
		v1, v2 = verbt2().split(",")
	else:
		v1, v2 = verbt(), ''

	s = _person + ' ' + v1 + ' ' + _objekt + r.choice([' ' + adjektiv(), ' ' + ort(), ' ' + adjektiv() + ' ' + ort(), '']) + v2 + '.'
	return erste_gross(s)
	

def satz_standard():
	"""
	Generiert einen zufälligen Standard-Satz.
	"""
	_funktion = 'satz_standard_' + str(r.randint(1, 4))
	return eval(_funktion)()


def satz_frage_1():
	"""
	Generiert eine Frage nach dem Grund, aus dem eine Person eine Tätigkeit ausführt

	Beispiel: Wieso fällt dein Partner in Gedanken hin?
	"""
	if r.randint(0,1): # getrenntes Verb
		v1, v2 = verbi2().split(",")
	else:
		v1, v2 = verbi(), ''
	s = chance(50, r.choice(['Warum ', 'Wieso ', 'Weshalb '])) + v1 + ' ' + person() + r.choice([' ' + adjektiv(), ' ' + ort(), ' ' + adjektiv() + ' ' + ort(), '']) + v2 + '?'
	return erste_gross(s)


def satz_frage_2():
	"""
	Generiert eine Frage nach der Person, die eine Tätigkeit ausführt.

	Beispiel: Wer telefoniert bewusstlos in der Abtei?
	"""
	if r.randint(0,1): # getrenntes Verb
		v1, v2 = verbi2().split(",")
	else:
		v1, v2 = verbi(), ''
	s = 'Wer ' + v1 + ' ' + r.choice([adjektiv(), ort(), adjektiv() + ' ' + ort()]) + v2 + '?'
	return erste_gross(s)


def satz_frage_3():
	"""
	Generiert eine Frage nach dem Ort, an dem eine Person eine Tätigkeit ausführt.

	Beispiel: Wo singt ein Siebdrucker?
	"""
	if r.randint(0,1): # getrenntes Verb
		v1, v2 = verbi2().split(",")
	else:
		v1, v2 = verbi(), ''
	s = 'Wo ' + v1 + ' ' + person() + chance(25, ' ' + adjektiv()) + v2 + '?'
	return erste_gross(s)


def satz_frage_4():
	"""
	Generiert eine Frage nach der Art, wie eine Person eine Tätigkeit ausführt.

	Beispiel: Wie wird sie beim ersten Date angefasst?
	"""
	if r.randint(0,1): # getrenntes Verb
		v1, v2 = verbi2().split(",")
	else:
		v1, v2 = verbi(), ''
	s = 'Wie ' + v1 + ' ' + person() + chance(50, ' ' + ort()) + v2 + '?'
	return erste_gross(s)


def satz_frage_5():
	"""
	Generiert eine Frage nach dem Zeitpunkt, an dem eine Person eine Tätigkeit ausführt.

	Beispiel: Wann säuft eine Hure?
	"""
	if r.randint(0,1):
		v1, v2 = verbi2().split(",")
	else:
		v1, v2 = verbi(), ''
	s = 'Wann ' + v1 + ' ' + person() + chance(50, ' endlich') + chance(25, ' ' + ort()) + v2 + '?'
	return erste_gross(s)


def satz_frage():
	"""
	Generiert eine zufällige Frage.
	"""
	_funktion = 'satz_frage_' + str(r.randint(1, 5))
	return eval(_funktion)()


def satz():
	"""
	Generiert einen zufälligen Satz.

	20% Standard-Sätze, 20% Fragen und 60% Themen-Sätze
	"""
	x = r.randint(1,5)

	if x == 1:
		s = satz_standard()
	elif x == 2:
		s = satz_frage()
	else:
		s = satz_thema()

	return s

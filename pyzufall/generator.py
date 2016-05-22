#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
pyzufall.generator
------------------

Stellt diverse Generator-Funktionen zur Verfügung.
"""

from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import *

import re
import random
from datetime import timedelta, date

from .helfer import lese, chance, str_add, uml

# Regex Pattern für Doctests
from pyzufall.helfer import re_wort, re_worte, re_liste, re_datum, re_email

# Benutze /dev/urandom oder Windows CryptGenRandom für bessere Entropy
r = random.SystemRandom()

# Namen einlesen
vornamen_m = lese('vornamen_m.txt')
vornamen_w = lese('vornamen_w.txt')
nachnamen = lese('nachnamen.txt')

# Objekte einlesen
pflanzen = lese('pflanzen.txt')
baeume = lese('baeume.txt')
tiere = lese('tiere.txt')
gegenstaende = lese('gegenstaende.txt')
koerperteile = lese('koerperteile.txt')
nahrung = lese('nahrung.txt')
geschmack = lese('geschmack.txt')
berufe = lese('berufe.txt')
musik = lese('musikgenre.txt')
stadte = lese('stadt_bundesland.txt')
interessen = lese('interessen.txt')
domains = lese('email_domains.txt')

# Wortarten einlesen

# Verben
nullwertige_verben = lese('nullwertige_verben.txt')
intransitive_verben = lese('intransitive_verben.txt')
intransitive_verben_2 = lese('intransitive_verben_2.txt')
transitive_verben = lese('transitive_verben.txt')
transitive_verben_2 = lese('transitive_verben_2.txt')
ditransitive_verben = lese('ditransitive_verben.txt')

# Adjektive
adjektive = lese('adjektiv.txt')

# Sazteile oder Sätze
ortsangabe = lese('ort.txt')
ns = lese('nebensatz.txt')
sprichwoerter = lese('sprichwoerter.txt')


def geschlecht():
	"""
	Gibt ein zufälliges Geschlecht zurück.

	1 = männlich
	0 = weiblich

	2011 gibt es laut Statistik 51,18% weibliche Personen in Deutschland:
	https://www.destatis.de/DE/ZahlenFakten/GesellschaftStaat/Bevoelkerung/Bevoelkerungsstand/Tabellen/Zensus_Geschlecht_Staatsangehoerigkeit.html

	:rtype: int

	.. only:: doctest

		>>> s = geschlecht()

		>>> assert s is 0 or 1
	"""
	if r.randint(1, 100) <= 51:
		return 0
	else:
		return 1


def vorname_m():
	"""
	Gibt einen männlichen Vornamen zurück.

	.. only:: doctest

		>>> s = vorname_m()

		testet ob ergebnis in liste ist
		>>> assert s in vornamen_m
		
		testet ob ergebnis aus buchstaben besteht
		>>> assert re.match(re_wort, s)
	"""
	return r.choice(vornamen_m)


def vorname_w():
	"""
	Gibt einen weiblichen Vornamen zurück.

	.. only:: doctest

		>>> s = vorname_w()

		testet ob ergebnis in liste ist
		>>> assert s in vornamen_w
		
		testet ob ergebnis aus buchstaben besteht
		>>> assert re.match(re_wort, s)
	"""
	return r.choice(vornamen_w)


def vorname():
	"""
	Gibt einen Vornamen zurück.
	"""
	return r.choice([vorname_m, vorname_w])()


def nachname():
	"""
	Gibt einen Nachnamen zurück.

	.. only:: doctest

		>>> s = nachname()

		testet ob ergebnis in liste ist
		>>> assert s in nachnamen
		
		testet ob ergebnis aus buchstaben besteht
		>>> assert re.match(re_wort, s)
	"""
	return r.choice(nachnamen)


def nickname(vorname='', nachname=''):
	"""
	Generiert einen Nickname, Angabe von Vor- und Nachname optional.

	Beispiel: dicker_falke, beate_brutal85, stinkender_panda24

	.. versionadded:: 0.13
	"""
	if vorname and nachname and r.randint(1,100) <= 75:
		x =  r.randint(1, 5)
		if x == 1:
			s = vorname[0] + nachname[:2]
		elif x == 2:
			s = vorname[:r.randint(2, len(vorname))] + nachname[:r.randint(2, len(nachname))]
		elif x == 3:
			s = vorname[:r.randint(3, len(vorname))] + wort(r.randint(3, 5))
		elif x == 4:
			s = vorname
			y = objekt().split(' ', 1)[1]
			i = 0
			while ( y[0].lower() != s[0].lower() and i < 250 ):
				if i % 2 == 0:
					y = objekt().split(' ', 1)[1]
				else:
					y = adjektiv()
				i += 1
			s = s + '_' + y
			s = s.replace('-', '_')
		elif x == 5:
			s = vorname + verbi()
			s = s.replace(' ', '')
	else:
		x =  r.randint(1, 2)
		if x == 1:
			s = objekt().replace(' ', '_')
			s = s.replace('-', '_')
		elif x == 2:
			s = objekt()
			if s.split(' ', 1)[0] == 'der':
				s = str_add(adjektiv(), 'er') + '_' + s.split(' ', 1)[1]
			else:
				s = str_add(adjektiv(), 'e') + '_' + s.split(' ', 1)[1]
			s = s.replace('-', '_')

	return s.lower() + chance(20, str(r.randint(1,99)))


def homepage(vorname, nachname, nick=''):
	"""
	Gibt die Domain einer persönlichen Homepage zurück.

	Beispiel: lilim.eu, heruntergekommene-kastanie.net, damian-schuett.org

	.. versionadded:: 0.13
	"""
	x = r.randint(1,8)
	if x == 1 or x == 2:
		s = vorname + '-' + nachname
	elif x == 3:
		s = vorname + '.' + nachname
	elif x == 4:
		s = vorname[0] + nachname
	elif x == 5:
		s = vorname + nachname[0]
	elif x == 6:
		s = nachname
	elif nick:
		s = nick
	else:
		s = nickname(vorname, nachname)
	s = s.replace('_', '-')

	return uml(s.lower()) + '.' + r.choice(['de', 'net', 'org', 'eu', 'com', 'me'])


def url(domain):
	"""
	>>> s = url('davidak.de')

	>>> print(s)
	http://davidak.de/

	.. versionadded:: 0.13

	.. only:: doctest

		>>> s = url('säge.de')

		>>> print(s)
		http://säge.de/
	"""
	return 'http://{}/'.format(domain)


def email(vorname, nachname, nick='', domain=''):
	"""
	Generiert eine E-Mail-Adresse.

	Beispiel: ismail@ismail-christ.eu, emelieeiru63@lebanese.cc, nic@copacabana.com

	.. only:: doctest

		>>> s = email('Bernd', 'Lieferts')

		>>> assert re.match(re_email, s)

	.. versionadded:: 0.13
	"""
	if nick == '':
		nick = nickname(vorname, nachname)

	if domain and r.randint(1, 100) < 60:
		s = r.choice([vorname, nick]) + '@' + domain
	else:
		s = r.choice([vorname + '.' + nachname, vorname, nachname, nick]) + '@' + r.choice(domains)

	return uml(s.lower())


def verbn():
	"""
	Gibt ein nullwertiges Verb zurück.

	`Beschreibung auf Wikipedia <http://de.wikipedia.org/wiki/Transitivität_(Grammatik)#Festlegung_der_Transitivit.C3.A4t_eines_Verbs/>`_

	.. only:: doctest

		>>> s = verbn()

		testst ob ergebnis in liste ist
		>>> assert s in nullwertige_verben
		
		testet ob ergebnis aus buchstaben besteht
		>>> assert re.match(re_wort, s)
	"""
	return r.choice(nullwertige_verben)


def verbi():
	"""
	Gibt ein intransitives Verb zurück.

	`Beschreibung auf Wikipedia <http://de.wikipedia.org/wiki/Transitivität_(Grammatik)#Festlegung_der_Transitivit.C3.A4t_eines_Verbs/>`_

	.. only:: doctest

		>>> s = verbi()

		testet ob ergebnis in liste ist
		>>> assert s in intransitive_verben
		
		testet ob ergebnis aus buchstaben besteht
		>>> assert re.match(re_worte, s)
	"""
	return r.choice(intransitive_verben)


def verbi2():
	"""
	Gibt ein intransitives, getrenntes Verb zurück.

	`Beschreibung auf Wikipedia <http://de.wikipedia.org/wiki/Transitivität_(Grammatik)#Festlegung_der_Transitivit.C3.A4t_eines_Verbs/>`_

	.. only:: doctest

		>>> s = verbi2()

		testet ob ergebnis in liste ist
		>>> assert s in intransitive_verben_2
		
		>>> assert re.match(re_liste, s)
	"""
	return r.choice(intransitive_verben_2)


def verbt():
	"""
	Gibt ein transitives Verb zurück.

	`Beschreibung auf Wikipedia <http://de.wikipedia.org/wiki/Transitivität_(Grammatik)#Festlegung_der_Transitivit.C3.A4t_eines_Verbs/>`_

	.. only:: doctest

		>>> s = verbt()

		testet ob ergebnis in liste ist
		>>> assert s in transitive_verben
		
		testet ob ergebnis aus buchstaben besteht
		>>> assert re.match(re_wort, s)
	"""
	return r.choice(transitive_verben)


def verbt2():
	"""
	Gibt ein intransitives, getrenntes Verb zurück.

	`Beschreibung auf Wikipedia <http://de.wikipedia.org/wiki/Transitivität_(Grammatik)#Festlegung_der_Transitivit.C3.A4t_eines_Verbs/>`_

	.. only:: doctest

		>>> s = verbt2()

		testet ob ergebnis in liste ist
		>>> assert s in transitive_verben_2
		
		>>> assert re.match(re_liste, s)
	"""
	return r.choice(transitive_verben_2)


def verbd():
	"""
	Gibt ein ditransitives Verb zurück.

	`Beschreibung auf Wikipedia <http://de.wikipedia.org/wiki/Transitivität_(Grammatik)#Festlegung_der_Transitivit.C3.A4t_eines_Verbs/>`_

	.. only:: doctest

		>>> s = verbd()

		testet ob ergebnis in liste ist
		>>> assert s in ditransitive_verben
		
		testet ob ergebnis aus buchstaben besteht
		>>> assert re.match(re_wort, s)
	"""
	return r.choice(ditransitive_verben)


def adjektiv():
	"""
	Gibt ein Adjektiv zurück.

	.. only:: doctest

		>>> s = adjektiv()

		testet ob ergebnis in liste ist
		>>> assert s in adjektive
		
		testet ob ergebnis aus buchstaben besteht
		>>> assert re.match(re_wort, s)
	"""
	return r.choice(adjektive)


def gegenstand():
	"""
	Gibt einen Gegenstand zurück.

	.. only:: doctest

		>>> s = gegenstand()

		testet ob ergebnis in liste ist
		>>> assert s in gegenstaende
		
		testet ob ergebnis aus buchstaben besteht
		>>> assert re.match(re_worte, s)
	"""
	return r.choice(gegenstaende)


def koerperteil():
	"""
	Gibt ein Körperteil zurück.

	.. only:: doctest

		>>> s = koerperteil()

		testet ob ergebnis in liste ist
		>>> assert s in koerperteile
		
		testet ob ergebnis aus buchstaben besteht
		>>> assert re.match(re_worte, s)
	"""
	return r.choice(koerperteile)


def interesse():
	"""
	Gibt ein zufälliges Interesse bzw Hobby zurück.

	.. deprecated:: 0.11
		Wird durch :func:`pyzufall.generator.interessen_liste` ersetzt.

	.. only:: doctest

		>>> s = interesse()

		testet ob ergebnis in liste ist
		>>> assert s in interessen
		
		testet ob ergebnis aus buchstaben besteht
		>>> assert re.match(re_worte, s)
	"""
	return r.choice(interessen)


def tier():
	"""
	Gibt ein Tier zurück.

	.. only:: doctest

		>>> s = tier()

		testet ob ergebnis in liste ist
		>>> assert s in tiere
		
		testet ob ergebnis aus buchstaben besteht
		>>> assert re.match(re_worte, s)
	"""
	return r.choice(tiere)


def baum():
	"""
	Gibt einen Baum zurück.

	.. only:: doctest

		>>> s = baum()

		testet ob ergebnis in liste ist
		>>> assert s in baeume
		
		testet ob ergebnis aus buchstaben besteht
		>>> assert re.match(re_worte, s)
	"""
	return r.choice(baeume)


def pflanze():
	"""
	Gibt eine Pflanze zurück.

	.. only:: doctest

		>>> s = pflanze()

		testet ob ergebnis in liste ist
		>>> assert s in pflanzen
		
		testet ob ergebnis aus buchstaben besteht
		>>> assert re.match(re_worte, s)
	"""
	return r.choice(pflanzen)


beziehung_m = ['Vater', 'Bruder', 'Mann', 'Sohn', 'Onkel', 'Opa', 'Cousin', 'Enkel', 'Chef', 'Freund', 'Partner', 'Kollege', 'Mitarbeiter', 'Mitbewohner', 'Vermieter', 'Lehrer']
beziehung_w = ['Mutter', 'Schwester', 'Frau', 'Tochter', 'Tante', 'Oma', 'Cousine', 'Enkelin', 'Cheffin', 'Freundin', 'Partnerin', 'Kollegin', 'Mitarbeiterin', 'Mitbewohnerin', 'Vermieterin', 'Lehrerin']
possessivpronomen_m = ['mein', 'dein', 'sein', 'ihr']
personen = ['er', 'sie', 'es', 'jemand', 'niemand']
spezial_m = ['ein Held', 'ein Penner', 'ein Verkäufer', 'ein Zuhälter', 'ein Polizist', 'ein Beamter', 'ein Arzt', 'Hitler', 'ein Bernd', 'ein Schwuler', 'ein Behinderter', 'der Affenmensch', 'der Satanist', 'der Alkoholiker', 'ein normaler Mensch', 'ein Pirat', 'ein Hartz-IV-Empfänger', 'ein Müllmann']
spezial_w = ['eine Heldin', 'eine Pennerin', 'eine Verkäuferin', 'eine Zuhälterin', 'eine Prostituierte', 'eine Nutte', 'eine Hure', 'eine Schlampe', 'eine Lehrerin', 'eine Polizistin', 'eine Beamtin', 'eine Ärztin', 'eine Behinderte', 'eine Sekretärin', 'die Transe', 'das Mannsweib', 'das Penismädchen', 'die Lesbe', 'die Kampflesbe', 'die Satanistin', 'die Alkoholikerin', 'die Piratin', 'die Hartz-IV-Empfängerin']
def person_m():
	"""
	Gibt eine männliche Person zurück.

	.. only:: doctest

		>>> s = person_m()

		>>> assert re.match(re_worte, s)
	"""
	z = r.randint(1,10)
	if z == 1:
		s = chance(25, str_add(adjektiv(), 'er '))
		s = r.choice([vorname_m(), vorname_w()]) + 's ' + s + r.choice(beziehung_m)
	elif z == 2:
		s = chance(25, str_add(adjektiv(), 'er '))
		s = r.choice(possessivpronomen_m) + ' ' + s + r.choice(beziehung_m)
	elif z == 3:
		s =  chance(50, str_add(adjektiv(), 'e '))
		s = 'der ' + s + r.choice(beziehung_m)
	elif z == 4:
		s = str_add(adjektiv(), 'e ')
		s = 'der ' + s + r.choice(vornamen_m)
	elif z == 5:
		s = str_add(adjektiv(), 'e')
		s = 'der ' + s.capitalize()
	elif z == 6:
		s = r.choice(['der ', 'ein ']) + beruf_m()
	elif z == 7:
		s = r.choice(spezial_m)
	elif z == 8:
		s = 'er'
	else:
		s = vorname_m()
	return s


def person_w():
	"""
	Gibt eine weibliche Person zurück.

	.. only:: doctest

		>>> s = person_w()

		>>> assert re.match(re_worte, s)
	"""
	z = r.randint(1,10)
	if z == 1:
		s = chance(25, str_add(adjektiv(), 'e '))
		s = r.choice([vorname_m(), vorname_w()]) + 's ' + s + r.choice(beziehung_w)
	elif z == 2:
		s = chance(25, str_add(adjektiv(), 'e '))
		s = r.choice(possessivpronomen_m) + 'e ' + s + r.choice(beziehung_w)
	elif z == 3:
		s =  chance(50, str_add(adjektiv(), 'e '))
		s = 'die ' + s + r.choice(beziehung_w)
	elif z == 4:
		s = str_add(adjektiv(), 'e ')
		s = 'die ' + s + vorname_w()
	elif z == 5:
		s = str_add(adjektiv(), 'e')
		s = 'die ' + s.capitalize()
	elif z == 6:
		s = r.choice(['die ', 'eine ']) + beruf_w()
	elif z == 7:
		s = r.choice(spezial_w)
	elif z == 8:
		s = 'sie'
	else:
		s = vorname_w()
	return s


def person():
	"""
	Gibt eine zufällige Person zurück.
	"""
	return r.choice([person_m, person_w])()


vokal = ['a', 'e', 'i', 'o', 'u', 'ei', 'au']
konsonant = ['b', 'c', 'd', 'f', 'g', 'h', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'sch']
konsonant2 = ['h', 'k', 'l', 'm', 'n', 's', 't']
def wort(laenge=r.randint(3,12)):
	"""
	Gibt ein Fantasiewort zurück.

	:param laenge: int

	.. only:: doctest

		>>> s = wort()

		>>> assert re.match(re_wort, s)
	"""
	anfaengt = r.randint(1,3)
	s = ""
	
	if anfaengt == 2: # Anfang wird ein Vokal
		s = r.choice(vokal)
		while len(s) < laenge:
			s += r.choice(konsonant)
			if len(s) < laenge and r.randint(0,1):
				s += r.choice(konsonant2)
			if len(s) >= laenge:
				break
			s += r.choice(vokal)

	else: # Anfang wird ein Konsonant
		s = r.choice(konsonant)
		while len(s) < laenge:
			s += r.choice(vokal)
			if len(s) >= laenge:
				break
			s += r.choice(konsonant)
			if len(s) < laenge and r.randint(0,1):
				s += r.choice(konsonant2)
	s = s.capitalize()
	return s


def zahl():
	"""
	Gibt eine Zahl zwischen 0 und 100 zurück.

	:rtype: string

	.. only:: doctest

		>>> s = zahl()

		>>> assert s.isdigit()
	"""
	s = r.randint(0,100)
	return str(s)


farben = ['Rot', 'Gelb', 'Blau', 'Violett', 'Türkis', 'Orange', 'Grün', 'Magenta', 'Braun', 'Grau', 'Weiß', 'Schwarz']
def farbe():
	"""
	Gibt eine Farbe zurück.

	.. only:: doctest

		>>> s = farbe()

		testet ob ergebnis in liste ist
		>>> assert s in farben
		
		testet ob ergebnis aus buchstaben besteht
		>>> assert re.match(re_wort, s)
	"""
	return r.choice(farben)


colors = ['red', 'yellow', 'blue', 'violet', 'orange', 'green', 'magenta', 'brown', 'gray', 'white', 'black']
def color():
	"""
	Gibt eine Farbe auf englisch zurück.

	.. only:: doctest

		>>> s = color()

		testet ob ergebnis in liste ist
		>>> assert s in colors
		
		testet ob ergebnis aus buchstaben besteht
		>>> assert re.match(re_wort, s)
	"""
	return r.choice(colors)


def zeitpunkt(start, ende):
	"""
	Gibt einen zufälligen Zeitpunkt (datetime.date) zwischen zwei Zeitpunkten zurück.
	Es handelt sich dabei um ein gültiges Datum.

	.. versionadded:: 0.13

	:param: start, ende: datetime
	:rtype: datetime

	.. only:: doctest

		>>> _heute = date.today()

		>>> _datum = date(2000, 3, 27)

		>>> s = zeitpunkt(_datum, _heute)

		>>> assert re.match(re_datum, s.strftime("%d.%m.%Y"))
	"""
	for arg in [start, ende]:
		if type(arg) is not date:
			raise TypeError("Es muss ein datetime.date Objekt übergeben werden, nicht " + str(type(arg)))

	delta = ende - start
	int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
	rand_second = random.randrange(int_delta)
	return start + timedelta(seconds=rand_second)


def geburtsdatum():
	"""
	Gibt ein gültiges Datum zwischen <vor 110 Jahren> und <heute> zurück.

	:rtype: string

	.. only:: doctest

		>>> s = geburtsdatum()

		>>> assert re.match(re_datum, s)
	"""
	_vor_110_jahren = date.today() - timedelta(days=(110 * 365.24))
	_datum = zeitpunkt(_vor_110_jahren, date.today())
	return _datum.strftime("%d.%m.%Y")


def datum():
	"""
	Gibt ein gültiges Datum zwischen <vor 50 Jahren> und <heute> zurück.

	:rtype: string

	.. only:: doctest

		>>> s = datum()

		>>> assert re.match(re_datum, s)
	"""
	_vor_50_jahren = date.today() - timedelta(days=(50 * 365.24))
	_datum = zeitpunkt(_vor_50_jahren, date.today())
	return _datum.strftime("%d.%m.%Y")


def sprichwort():
	"""
	Gibt ein Sprichwort zurück.

	.. only:: doctest

		>>> s = sprichwort()

		testet ob ergebnis in liste ist
		>>> assert s in sprichwoerter
	"""
	return r.choice(sprichwoerter)


def beruf_m():
	"""
	Gibt eine männliche Berufsbezeichnung zurück.

	.. only:: doctest

		>>> s = beruf_m()

		testet ob ergebnis in liste ist
		>>> assert s in berufe
		
		testet ob ergebnis aus buchstaben besteht
		>>> assert re.match(re_worte, s)
	"""
	return r.choice(berufe)


def beruf_w():
	"""
	Gibt eine weibliche Berufsbezeichnung zurück.

	.. only:: doctest

		>>> s = beruf_w()
		
		>>> assert re.match(re_worte, s)
	"""
	s = beruf_m() + 'in'
	s = re.sub('mannin$', 'frau', s) # Restaurantfachmannin => Restaurantfachfrau
	s = re.sub('kraftin$', 'kraft', s) # Edv-Fachkraftin => Edv-Fachkraft
	s = re.sub('angestellterin$', 'angestellte', s)
	s = re.sub('Fotomodellin$', 'Fotomodell', s)
	s = re.sub('Technischer Zeichnerin$', 'Technische Zeichnerin', s)
	s = re.sub('Arztin$', 'Ärztin', s)
	s = re.sub('arztin$', 'ärztin', s)
	s = re.sub('beamterin$', 'beamtin', s) # Polizeibeamterin => Polizeibeamte
	s = re.sub('stewardin$', 'stewardess', s)
	s = re.sub('Etagenaufsichtin$', 'Etagenaufsicht', s)
	s = re.sub('ein$', 'in', s) # Mikrobiologein => Mikrobiologin
	return s


def objekt():
	"""
	Gibt ein Objekt zurück.
	"""
	return r.choice([gegenstand, tier, pflanze, baum])()


def objekt_m(s):
	"""
	Bringt ein Objekt in Berzug zu einer männlichen Person.

	Beispiel:
	'der Bär' wird zu 'den Bären' oder 'seinen Bären'
	"""
	if 'der ' in s:
		s = re.sub('e$', 'en', s) # Löwen
	s = re.sub('Bär$', 'Bären', s)
	s = re.sub('der ', 'den ', s)
	
	if r.randint(0,2):
		s = re.sub('den ', r.choice(['einen ', 'seinen ', 'deinen ']), s)
		s = re.sub('die ', r.choice(['eine ', 'seine ', 'deine ']), s)
		s = re.sub('das ', r.choice(['ein ', 'sein ', 'dein ']), s)
	
	return s


def objekt_w(s):
	"""
	Bringt ein Objekt in Berzug zu einer weiblichen Person.

	Beispiel:
	'der Bär' wird zu 'den Bären' oder 'ihren Bären'
	"""
	if 'der ' in s:
		s = re.sub('e$', 'en', s) # Löwen
	s = re.sub('Bär$', 'Bären', s)
	s = re.sub('der ', 'den ', s)
	
	if r.randint(0,2):
		s = re.sub('den ', r.choice(['einen ', 'ihren ', 'deinen ']), s)
		s = re.sub('die ', r.choice(['eine ', 'ihre ', 'deine ']), s)
		s = re.sub('das ', r.choice(['ein ', 'ihr ', 'dein ']), s)
	
	return s


def person_objekt_m():
	"""
	Gibt eine Person als Objekt in Bezug auf eine männliche Person zurück.

	Beispiel: seine Mitarbeiterin

	.. only:: doctest

		>>> s = person_objekt_m()
		
		>>> assert re.match(re_worte, s)
	"""
	y = r.randint(1,4)
	if y == 1:
		s = vorname_m()
	if y == 2:
		s = vorname_w()
	if y == 3:
		s =  chance(25, str_add(adjektiv(), 'en '))
		s = r.choice(['seinen ', 'deinen ']) + s + r.choice(beziehung_m)
		s = re.sub('Kollege', 'Kollegen', s)
	if y == 4:
		s =  chance(25, str_add(adjektiv(), 'e '))
		s = r.choice(['seine ', 'deine ']) + s + r.choice(beziehung_w)
		
	return s


def person_objekt_w():
	"""
	Gibt eine Person als Objekt in Bezug auf eine weibliche Person zurück.

	Beispiel: ihre Mutter

	.. only:: doctest

		>>> s = person_objekt_w()
		
		>>> assert re.match(re_worte, s)
	"""
	y = r.randint(1,4)
	if y == 1:
		s = vorname_m()
	if y == 2:
		s = vorname_w()
	if y == 3:
		s =  chance(25, str_add(adjektiv(), 'en '))
		s = r.choice(['ihren ', 'deinen ']) + s + r.choice(beziehung_m)
		s = re.sub('Kollege', 'Kollegen', s)
	if y == 4:
		s =  chance(25, str_add(adjektiv(), 'e '))
		s = r.choice(['ihre ', 'deine ']) + s + r.choice(beziehung_w)

	return s


def ort():
	"""
	Gibt eine Ortsangabe zurück.

	Beispiel: 'im Flur'

	.. todo::

		aufteilen in generator und zufällige aus liste

	.. only:: doctest

		>>> s = ort()
		
		>>> assert re.match(r'^[A-Za-z0-9äÄöÖüÜß -]+$', s)
	"""
	tausende = ['500', '1000', '2000', '5000', '10000', '100000']
	if r.randint(0,3):
		zuschauer = r.choice(tausende)
	else:
		zuschauer = str(r.randint(1,10000))

	s = r.choice(ortsangabe)
	s = re.sub('auf Gleis XX$', 'auf Gleis ' + str(r.randint(1,14)), s)
	s = re.sub('XXZusch', zuschauer, s)
	s = re.sub('XXName', r.choice([vorname_m(), vorname_w()]) + 's', s)
	return s


voressen = ['Brat', 'Rühr', 'Reibe', 'Brech', 'Back', 'Ofen', 'Hack', 'Mager', 'Frisch', 'Bio', 'Gammel', 'Soja', 'Tofu', 'Milch']
def essen():
	"""
	Gibt ein Essen zurück.

	.. only:: doctest

		>>> s = essen()
		
		>>> assert re.match(re_wort, s)
	"""
	if r.randint(0,2): # zusammengesetzt aus zwei Wörtern
		if r.randint(0,2):
			s = r.choice(geschmack) + r.choice(nahrung).lower()
		else:
			s = r.choice(voressen) + r.choice(nahrung).lower()
	else: # aus einem Wort bestehend
		if r.randint(0,2):
			s = r.choice(geschmack)
		else:
			s = r.choice(nahrung)
	return s


beilag = ['Soße', 'Sauce', 'Brühe', 'Brei', 'Püree', 'Kartoffeln', 'Salat', 'Marmelade']
beilag2 = ['Kroketten', 'Pommes', 'Rösti', 'Röstzwiebeln', 'Mayo', 'Mayonnaise', 'Ketchup', 'Bratkartoffeln', 'Zwiebelringen', 'Kartoffelpuffer', 'Soße', 'Nudeln', 'Gemüse', 'Knödeln', 'Salat', 'Marmelade']
def beilage():
	"""
	Gibt eine Beilage zum Essen zurück.

	.. only:: doctest

		>>> s = beilage()
		
		>>> assert re.match(re_wort, s)
	"""
	if r.randint(0,2):
		s = r.choice(beilag2)
	else:
		s = r.choice(geschmack) + r.choice(beilag).lower()
	return s


getraenk = ['Wasser', 'Saft', 'Tee', 'Kaffee', 'Eistee', 'Milch', 'Punsch', 'Bowle', 'Bier', 'Likör',  'Wein', 'Rum', 'Sekt', 'Schnaps', 'Cocktail']
def trinken():
	"""
	Gibt ein Getränk zurück.

	.. only:: doctest

		>>> s = trinken()
		
		>>> assert re.match(re_wort, s)
	"""
	if r.randint(0,2):
		s = r.choice(geschmack) + r.choice(getraenk).lower()
	else:
		s = r.choice(getraenk)
	return s


def stadt():
	"""
	Gibt eine Stadt zurück.

	.. only:: doctest

		>>> s = stadt()
		
		>>> assert re.match(r'^[A-Za-zäÄöÖüÜß/. -]+$', s)
	"""
	return r.choice(stadte).split(' (', 1)[0] # Stadt von Bundesland trennen


def stadt_bl():
	"""
	Gibt eine Stadt mit Bundesland zurück.

	.. only:: doctest

		>>> s = stadt_bl()

		testet ob ergebnis in liste ist
		>>> assert s in stadte
		
		>>> assert re.match(r'^[A-Za-zäÄöÖüÜß/.() -]+$', s)
	"""
	return r.choice(stadte)


gruppe = ['Menschen', 'Personen', 'Kinder', 'Tiere', 'Gedärme', 'Kadaver', 'Nudeln', 'Unterhosen', 'Würstchen', 'Bäume', 'Stühle', 'Schweine', 'Neger', 'Alkoholiker', 'Leichen']
def band():
	"""
	Gibt einen fiktiven Bandnamen zurück.

	.. only:: doctest

		>>> s = band()
		
		>>> assert re.match(r'^[A-Za-z0-9äÄöÖüÜß -]+$', s)
	"""
	z = r.randint(0,5)
	if z == 0:
		s = 'Die ' + str_add(adjektiv().capitalize(), 'en ') + r.choice(gruppe)
	if z == 1:
		s = r.choice(geschmack) + ' ' + ort()
	if z == 2:
		s = adjektiv().capitalize() + ' ' + ort()
	if z == 3:
		s = str_add(adjektiv().capitalize(), 'e ') + essen()
	if z == 4:
		s = adjektiv().capitalize()
	if z == 5:
		s = wort()
	return s


def bandart():
	"""
	Gibt eine Bandart zurück.

	Beispiel: 'Gothic Metal Band'

	.. only:: doctest

		>>> s = bandart()
		
		>>> assert re.match(r'^[A-Za-zäÄöÖüÜß -]+[Bb]and$', s)
	"""
	m = r.choice(musik)
	if ' ' in m:
		s = m + ' Band'
	elif '-' in m:
		s = m + '-Band'
	else:
		s = m + 'band'
	return s


def firma():
	"""
	Gibt einen fiktiven Firmenname zurück.

	.. todo::

		Funktion programmieren
	"""
	pass

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .version import __version__

import random
import datetime
import re
import os

r = random.SystemRandom() # Uses /dev/urandom or Windows CryptGenRandom for better entropy

def lese(dateiname):
	"""
	Liest die Datei mit dem übergebenen Namen aus data/ zeilenweise ein und gib eine Liste zurück.

	`<http://stackoverflow.com/questions/10174211/make-an-always-relative-to-current-module-file-path>`_
	"""
	dateipfad = os.path.join(os.path.dirname(__file__), 'data/' + dateiname)
	return open(dateipfad, 'r').read().splitlines()

# Namen einlesen
vornamen_m = lese('vornamen_m')
vornamen_w = lese('vornamen_w')
nachnamen = lese('nachnamen')

# Objekte einlesen
pflanzen = lese('pflanzen')
baeume = lese('baeume')
tiere = lese('tiere')
gegenstaende = lese('gegenstaende')
koerperteile = lese('koerperteile')
nahrung = lese('nahrung')
geschmack = lese('geschmack')
berufe = lese('berufe')
musik = lese('musikgenre')
stadte = lese('stadt_bundesland')
interessen = lese('interessen.txt')

# Wortarten einlesen

# Verben
nullwertige_verben = lese('nullwertige_verben')
intransitive_verben = lese('intransitive_verben')
intransitive_verben_2 = lese('intransitive_verben_2')
transitive_verben = lese('transitive_verben')
transitive_verben_2 = lese('transitive_verben_2')
ditransitive_verben = lese('ditransitive_verben')

# Adjektive
adjektive = lese('adjektiv')

# Sazteile oder Sätze
ortsangabe = lese('ort')
ns = lese('nebensatz')
sprichwoerter = lese('sprichwoerter')


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


def geschlecht():
	"""
	Gibt ein zufälliges Geschlecht zurück.

	1 = männlich
	0 = weiblich

	2011 gibt es laut Statistik 51,18% weibliche Personen in Deutschland:
	https://www.destatis.de/DE/ZahlenFakten/GesellschaftStaat/Bevoelkerung/Bevoelkerungsstand/Tabellen/Zensus_Geschlecht_Staatsangehoerigkeit.html
	"""
	if r.randint(0, 100) <= 51:
		return 0
	else:
		return 1


def vorname_m():
	"""
	Gibt einen männlichen Vornamen zurück.
	"""
	return r.choice(vornamen_m)


def vorname_w():
	"""
	Gibt einen weiblichen Vornamen zurück.
	"""
	return r.choice(vornamen_w)


def vorname():
	"""
	Gibt einen zufälligen Vornamen zurück.
	"""
	return r.choice([vorname_m, vorname_w])()


def nachname():
	"""
	Gibt einen Nachnamen zurück.
	"""
	return r.choice(nachnamen)


def verbn():
	"""
	Gibt ein nullwertiges Verb zurück.

	`Beschreibung auf Wikipedia <http://de.wikipedia.org/wiki/Transitivität_(Grammatik)#Festlegung_der_Transitivit.C3.A4t_eines_Verbs/>`_
	"""
	return r.choice(nullwertige_verben)


def verbi():
	"""
	Gibt ein intransitives Verb zurück.

	`Beschreibung auf Wikipedia <http://de.wikipedia.org/wiki/Transitivität_(Grammatik)#Festlegung_der_Transitivit.C3.A4t_eines_Verbs/>`_
	"""
	return r.choice(intransitive_verben)


def verbi2():
	"""
	Gibt ein intransitives, getrenntes Verb zurück.

	`Beschreibung auf Wikipedia <http://de.wikipedia.org/wiki/Transitivität_(Grammatik)#Festlegung_der_Transitivit.C3.A4t_eines_Verbs/>`_
	"""
	return r.choice(intransitive_verben_2)


def verbt():
	"""
	Gibt ein transitives Verb zurück.

	`Beschreibung auf Wikipedia <http://de.wikipedia.org/wiki/Transitivität_(Grammatik)#Festlegung_der_Transitivit.C3.A4t_eines_Verbs/>`_
	"""
	return r.choice(transitive_verben)


def verbt2():
	"""
	Gibt ein intransitives, getrenntes Verb zurück.

	`Beschreibung auf Wikipedia <http://de.wikipedia.org/wiki/Transitivität_(Grammatik)#Festlegung_der_Transitivit.C3.A4t_eines_Verbs/>`_
	"""
	return r.choice(transitive_verben_2)


def verbd():
	"""
	Gibt ein ditransitives Verb zurück.

	`Beschreibung auf Wikipedia <http://de.wikipedia.org/wiki/Transitivität_(Grammatik)#Festlegung_der_Transitivit.C3.A4t_eines_Verbs/>`_
	"""
	return r.choice(ditransitive_verben)


def adjektiv():
	"""
	Gibt ein Adjektiv zurück.
	"""
	return r.choice(adjektive)


def gegenstand():
	"""
	Gibt einen Gegenstand zurück.
	"""
	return r.choice(gegenstaende)


def koerperteil():
	"""
	Gibt ein Körperteil zurück.
	"""
	return r.choice(koerperteile)


def interesse():
	"""
	Gibt ein zufälliges Interesse bzw Hobby zurück.
	"""
	return r.choice(interessen)


def tier():
	"""
	Gibt ein Tier zurück.
	"""
	return r.choice(tiere)


def baum():
	"""
	Gibt einen Baum zurück.
	"""
	return r.choice(baeume)


def pflanze():
	"""
	Gibt eine Pflanze zurück.
	"""
	return r.choice(pflanzen)


beziehung_m = ['Vater', 'Bruder', 'Mann', 'Sohn', 'Onkel', 'Opa', 'Cousin', 'Enkel', 'Chef', 'Freund', 'Partner', 'Kollege', 'Mitarbeiter', 'Mitbewohner', 'Vermieter', 'Lehrer']
beziehung_w = ['Mutter', 'Schwester', 'Frau', 'Tochter', 'Tante', 'Oma', 'Cousine', 'Enkelin', 'Cheffin', 'Freundin', 'Partnerin', 'Kollegin', 'Mitarbeiterin', 'Mitbewohnerin', 'Vermieterin', 'Lehrerin']
possessivpronomen_m = ['mein', 'dein', 'sein', 'ihr']
personen = ['er', 'sie', 'es', 'jemand', 'niemand']
spezial_m = ['ein Held', 'ein Penner', 'ein Verkäufer', 'ein Zuhälter', 'ein Lehrer', 'ein Polizist', 'ein Beamter', 'ein Arzt', 'Hitler', 'ein Bernd', 'ein Schwuler', 'ein Behinderter', 'der Affenmensch', 'der Satanist', 'der Alkoholiker', 'ein normaler Mensch', 'ein Pirat', 'ein Hartz-IV-Empfänger', 'ein Müllmann']
spezial_w = ['eine Heldin', 'eine Pennerin', 'eine Verkäuferin', 'eine Zuhälterin', 'eine Prostituierte', 'eine Nutte', 'eine Hure', 'eine Schlampe', 'eine Lehrerin', 'eine Polizistin', 'eine Beamtin', 'eine Ärztin', 'eine Behinderte', 'eine Sekretärin', 'die Transe', 'das Mannsweib', 'das Penismädchen', 'die Lesbe', 'die Kampflesbe', 'die Satanistin', 'die Alkoholikerin', 'die Piratin', 'die Hartz-IV-Empfängerin']
def person_m():
	"""
	Gibt eine männliche Person zurück.
	"""
	z = r.randint(1,10)
	if z == 1:
		s = e25(adjektiv() + 'er ')
		s = re.sub('eer $', 'er ', s) # feigeer
		s = r.choice([vorname_m(), vorname_w()]) + 's ' + s + r.choice(beziehung_m)
	elif z == 2:
		s = e25(adjektiv() + 'er ')
		s = re.sub('eer $', 'er ', s) # feigeer
		s = r.choice(possessivpronomen_m) + ' ' + s + r.choice(beziehung_m)
	elif z == 3:
		s =  e50(adjektiv() + 'e ')
		s = re.sub('ee $', 'e ', s) # der feigee
		s = 'der ' + s + r.choice(beziehung_m)
	elif z == 4:
		s = adjektiv() + 'e '
		s = re.sub('ee $', 'e ', s) # der feigee
		s = 'der ' + s + r.choice(vornamen_m)
	elif z == 5:
		s = adjektiv() + 'e'
		s = re.sub('ee$', 'e', s) # der feigee
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
	"""
	z = r.randint(1,10)
	if z == 1:
		s = e25(adjektiv() + 'e ')
		s = re.sub('ee $', 'e ', s) # feigee
		s = r.choice([vorname_m(), vorname_w()]) + 's ' + s + r.choice(beziehung_w)
	elif z == 2:
		s = e25(adjektiv() + 'e ')
		s = re.sub('ee $', 'e ', s) # die feigee
		s = r.choice(possessivpronomen_m) + 'e ' + s + r.choice(beziehung_w)
	elif z == 3:
		s =  e50(adjektiv() + 'e ')
		s = re.sub('ee $', 'e ', s) # die feigee
		s = 'die ' + s + r.choice(beziehung_w)
	elif z == 4:
		s = adjektiv() + 'e '
		s = re.sub('ee $', 'e ', s) # die feigee
		s = 'die ' + s + vorname_w()
	elif z == 5:
		s = adjektiv() + 'e'
		s = re.sub('ee$', 'e', s) # die feigee
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
def wort():
	"""
	Gibt ein Fantasiewort zurück.
	"""
	laenge = r.randint(3,12)
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
	"""
	s = r.randint(0,100)
	return str(s)


farben = ['Rot', 'Gelb', 'Blau', 'Violett', 'Türkis', 'Orange', 'Grün', 'Magenta', 'Braun', 'Grau', 'Weiß', 'Schwarz']
def farbe():
	"""
	Gibt eine Farbe zurück.
	"""
	return r.choice(farben)


colors = ['red', 'yellow', 'blue', 'violet', 'orange', 'green', 'magenta', 'brown', 'gray', 'white', 'black']
def color():
	"""
	Gibt eine Farbe auf englisch zurück.
	"""
	return r.choice(colors)


def geburtsdatum():
	"""
	Gibt ein gültiges Datum zwischen dem 01.01.1910 und 31.12.2012 zurück.
	"""
	while(True):
		try:
			_s = str(r.randint(1,31)).zfill(2) + '.' + str(r.randint(1,12)).zfill(2) + '.' + str(r.randint(1910,2012))
			_dateobj = datetime.datetime.strptime(_s, "%d.%m.%Y").date() # kann der String in ein gültiges Datum umgewandelt werden?
			return _s
		except:
			print(_s + " ist kein gültiges Datum!")


def datum():
	"""
	Gibt ein gültiges Datum zwischen dem 01.01.1950 und 31.12.2012 zurück.
	"""
	while(True):
		try:
			_s = str(r.randint(1,31)).zfill(2) + '.' + str(r.randint(1,12)).zfill(2) + '.' + str(r.randint(1950,2012))
			_dateobj = datetime.datetime.strptime(_s, "%d.%m.%Y").date() # kann der String in ein gültiges Datum umgewandelt werden?
			return _s
		except:
			print(_s + " ist kein gültiges Datum!")


def sprichwort():
	"""
	Gibt ein Sprichwort zurück.
	"""
	return r.choice(sprichwoerter)


def beruf_m():
	"""
	Gibt eine männliche Berufsbezeichnung zurück.
	"""
	return r.choice(berufe)


def beruf_w():
	"""
	Gibt eine weibliche Berufsbezeichnung zurück.
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
	s = re.sub('ein$', 'in', s) # Mikrobiologein => Mikrobiologin
	return s


def objekt():
	"""
	Gibt ein Objekt zurück.
	"""
	return r.choice([gegenstand(), tier(), pflanze(), baum()])


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
	"""
	y = r.randint(1,4)
	if y == 1:
		s = vorname_m()
	if y == 2:
		s = vorname_w()
	if y == 3:
		s =  e25(adjektiv() + 'en ')
		s = re.sub('een ', 'en ', s) # feigeen
		s = r.choice(['seinen ', 'deinen ']) + s + r.choice(beziehung_m)
		s = re.sub('Kollege', 'Kollegen', s)
	if y == 4:
		s =  e25(adjektiv() + 'e ')
		s = re.sub('ee ', 'e ', s) # feigee
		s = r.choice(['seine ', 'deine ']) + s + r.choice(beziehung_w)
		
	return s


def person_objekt_w():
	"""
	Gibt eine Person als Objekt in Bezug auf eine weibliche Person zurück.

	Beispiel: ihre Mutter
	"""
	y = r.randint(1,4)
	if y == 1:
		s = vorname_m()
	if y == 2:
		s = vorname_w()
	if y == 3:
		s =  e25(adjektiv() + 'en ')
		s = re.sub('een ', 'en ', s) # feigeen
		s = r.choice(['ihren ', 'deinen ']) + s + r.choice(beziehung_m)
		s = re.sub('Kollege', 'Kollegen', s)
	if y == 4:
		s =  e25(adjektiv() + 'e ')
		s = re.sub('ee ', 'e ', s) # feigee
		s = r.choice(['ihre ', 'deine ']) + s + r.choice(beziehung_w)

	return s


def ort():
	"""
	Gibt eine Ortsangabe zurück.

	Beispiel: 'im Flur'
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
	Gibt ein Gericht zurück.
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
	"""
	if r.randint(0,2):
		s = r.choice(geschmack) + r.choice(getraenk).lower()
	else:
		s = r.choice(getraenk)
	return s


def stadt():
	"""
	Gibt eine Stadt zurück.
	"""
	s = r.choice(stadte).split(' (', 1) # Stadt und Bundesland trennen
	s = s[0] # Nur Stadt, nicht Bundesland
	return s


def stadt_bl():
	"""
	Gibt eine Stadt mit Bundesland zurück.
	"""
	return r.choice(stadte)


gruppe = ['Menschen', 'Personen', 'Kinder', 'Tiere', 'Gedärme', 'Kadaver', 'Nudeln', 'Unterhosen', 'Würstchen', 'Bäume', 'Stühle', 'Schweine', 'Neger', 'Alkoholiker', 'Leichen']
def band():
	"""
	Gibt einen fiktiven Bandnamen zurück.
	"""
	z = r.randint(0,5)
	if z == 0:
		s = 'Die ' + adjektiv().capitalize() + 'en ' + r.choice(gruppe)
	if z == 1:
		s = r.choice(geschmack) + ' ' + ort()
	if z == 2:
		s = adjektiv().capitalize() + ' ' + ort()
	if z == 3:
		s = adjektiv().capitalize() + 'e ' + essen()
	if z == 4:
		s = adjektiv().capitalize()
	if z == 5:
		s = wort()
	return s


def bandart():
	"""
	Gibt eine Bandart zurück.

	Beispiel: 'Gothic Metal Band'
	"""
	if r.randint(0,2):
		m = r.choice(musik)
		if ' ' in m:
			s = m + ' Band'
		elif '-' in m:
			s = m + '-Band'
		else:
			s = m + 'band'
	else:
		s = r.choice(['Band', 'Musikergruppe'])
	return s


def firma():
	"""
	Gibt einen fiktiven Firmenname zurück.

	.. todo::

		Funktion programmieren
	"""
	pass


# Satz-Schemata

def satz_nulltransitiv():
	"""
	Generiert einen Satz mit einem nulltransitiven Verb.

	Beispiel: Im Park schneit es.
	"""
	if r.randint(0,1):
		s = ort() + ' ' + verbn() + ' es' + e25(' ' + adjektiv()) + '.'
	else:
		s = 'Es ' + verbn() + e25(' ' + adjektiv()) + '.'
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
		s = r.choice(vornamen_m) + e50(' ' + r.choice(nachnamen)) + ' ist ' + e50('der ') + r.choice(besetzung) + e50(' von') + ' der ' + bandart() + ' "' + band() + '".'
	else: # weiblich
		s = r.choice(vornamen_w) + e50(' ' + r.choice(nachnamen)) + ' ist ' + e50('die ') + r.choice(besetzung) + 'in' + e50(' von') + ' der ' + bandart() + ' "' + band() + '".'
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
		s += e75(r.choice(['Anfang', 'Mitte', 'Mitte des Jahres', 'Ende', 'im Frühling', 'im Sommer', 'im Herbst', 'im Winter', 'im Jahr'])) + ' ' + str(r.randint(1950, 2013))

	s += e50(' in ' + stadt()) + ' gegründet.'
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
	Generiert einen Satz zum Thema Band.
	"""
	return r.choice([satz_band_mitglied, satz_band_gegruendet, satz_band_besetzung])()


def satz_arbeit():
	"""
	Generiert einen Satz über eine berufstätige Person.

	Beispiel: Achmed, der Grafiker aus Waldheim, spielt den Nasenbär.
	"""
	x = r.randint(1,4)
	if x == 1:
		s = vorname_m() + e50(' ' + nachname()) + ' ist ' + e75('ein ') + beruf_m() + e25(' aus ' + stadt())
	if x == 2:
		s = vorname_w() + e50(' ' + nachname()) + ' ist ' + e75('eine ') + beruf_w() + e25(' aus ' + stadt())
	if x == 3:
		s = vorname_m() + e50(' ' + nachname()) + e50(', der ' + beruf_m() + e50(' aus ' + stadt()) + ',') + ' ' + verbt() + ' ' + r.choice([person_objekt_m(), objekt_m(objekt())])
	if x == 4:
		s = vorname_w() + e50(' ' + nachname()) + e50(', die ' + beruf_w() + e50(' aus ' + stadt()) + ',') + ' ' + verbt() + ' ' + r.choice([person_objekt_w(), objekt_w(objekt())])
	return erste_gross(s) + '.'


def satz_essen():
	"""
	Generiert einen Satz mit Essen und/oder Trinken.

	Beispiel: Die Wärterin isst Orangen mit Mayonnaise und trinkt dazu Milch.
	"""
	x = r.randint(1,3)
	if x == 1: # Essen mit Beilage
		s = person() + e25(' ' + r.choice(['ist', 'sitzt', 'befindet sich']) + ' ' + ort() + ' und') + ' isst ' + e50(r.choice(['gerade', 'oft', 'nicht oft', 'selten', 'gerne', 'nicht gerne']) + ' ') + essen() + e50(' mit ' + r.choice(['viel', 'ganz viel', 'ein bischen', 'ein wenig', 'lecker', 'einer großen Portion']) + ' ' + beilage())
	if x == 2: # Trinken
		s = person() + ' trinkt ' + e50(r.choice(['gerade', 'oft', 'nicht oft', 'selten', 'gerne', 'nicht gerne', 'jeden Abend ein Glas', 'zu viel']) + ' ') + trinken()
	if x == 3: # Essen und Trinken
		s = person() + ' isst ' + essen() + e50(' mit ' + beilage()) + ' und trinkt ' + e50('dazu ') + trinken()
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
			s = person_m() + ' ' + r.choice(['verletzt sich', 'stößt sich', 'bricht' + e50(' sich'), 'verstaucht' + e50(' sich'), 'massiert']) + ' ' + s
		else: # Sie
			s = koerperteil()
			s = re.sub('der ', 'den ', s)
			if r.randint(0,1):
				s = re.sub('den ', 'ihren ', s)
				s = re.sub('die ', 'ihre ', s)
				s = re.sub('das ', 'ihr ', s)
			s = person_w() + ' ' + r.choice(['verletzt sich', 'stößt sich', 'bricht' + e50(' sich'), 'verstaucht' + e50(' sich'), 'massiert']) + ' ' + s
	if x == 2: # hat Kopfschmerzen
		s = koerperteil()
		s = re.sub('e$', 'en', s) # Lungen
		s = s.split()[1] # Körperteil ohne Artikel
		s = person() + ' hat ' + e25(r.choice(['schlimme', 'ein bischen', 'brutale', 'oft', 'manchmal']) + ' ') + s + 'schmerzen'
	if x == 3:
		s = koerperteil()
		s = re.sub('der ', 'am ', s)
		s = re.sub('die ', 'an der ', s)
		s = re.sub('das ', 'am ', s)
		s = person() + ' hat eine ' + e25(r.choice(['schmerzhafte ', 'brutale ', 'miese ', 'kleine ', 'eiternde '])) + r.choice(['Verletzung', 'Entzündung', 'Wunde', 'Beschädigung']) + ' ' + s
	if x == 4:
		s = koerperteil()
		s = re.sub('der ', 'Mein ', s)
		s = re.sub('die ', 'Meine ', s)
		s = re.sub('das ', 'Mein ', s)
		s = s + ' ' + r.choice(['tut weh', 'schmerzt', 'blutet', 'juckt', 'brennt', 'stinkt'])
	if x == 5:
		s = koerperteil()
		s = re.sub('der ', 'einen ' + adjektiv() + 'en ', s)
		s = re.sub('die ', 'eine ' + adjektiv() + 'e ', s)
		s = re.sub('das ', 'ein ' + adjektiv() + 'es ', s)
		s = person() + ' hat ' + s
	return erste_gross(s) + '.'


def satz_kloster():
	"""
	Generiert einen Satz über eine Person in einem Kloster.

	Beispiel: Der Bruder Florian ist der debilste Mönch in der Abtei.

	.. todo::

		"..."ste nicht immer richtig:

		- Bruder Dennis war der monströsste Mönch im Kloster.
		- Schwester Lara ist die diskretste Nonne in der Abtei.
		- Bruder Marcel war der gerechtste Mönch im Orden.
		- Bruder Nicolaus ist der falschste Mönch im Kloster.
	"""
	if r.randint(0,1): # männlich
		s = e25('Der ') + 'Bruder ' + vorname_m() + r.choice([' war', ' ist']) + ' der ' + adjektiv() + 'ste Mönch ' + r.choice(['im Kloster', 'im Orden', 'in der Abtei'])
	else: # weiblich
		s = e25('Die ') + 'Schwester ' + vorname_w() + r.choice([' war', ' ist']) + ' die ' + adjektiv() + 'ste Nonne ' + r.choice(['im Kloster', 'im Orden', 'in der Abtei'])
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
	
	s = r.choice(['Weil', 'Während', 'Obwohl', 'Ohne dass', 'Nur weil', 'Gerade weil']) + r.choice([verb22 + erste_person + ' ', ' ' + erste_person + verb22]) + e50(ort() + ' ') + e50(adjektiv() + ' ') + verb2 + ', ' + v1 + zweit_person + v12 + e50(adjektiv() + ' ') + v2 + '.'
	return erste_gross(s)


def satz_absurde_farbfunktion():
	"""
	Generiert einen Satz nach folgendem Muster: Gelb ist brauner als Türkis.
	"""
	farbe1, farbe2, farbe3 = farbe(), farbe(), farbe()
	while farbe1 is farbe2 or farbe2 is farbe3 or farbe1 is farbe3:
		farbe1, farbe2, farbe3 = farbe(), farbe(), farbe()
	s = farbe1 + ' ist ' + r.choice([farbe2.lower(), adjektiv()]) + 'er als ' + farbe3 + '.'
	return erste_gross(s)


def satz_freunde_lieben():
	"""
	Generiert einen Satz über eine Person mit Eigenschaften.

	Beispiel: In der Garage ist das Mannsweib lesbisch.
	"""
	if r.randint(0,1): #männlich
		s = person_m() + ' ist ' + adjektiv() + e50(r.choice(['. Alle', ', aber']) + ' seine Freunde lieben ihn dafür') + '.'
	else: #weiblich
		s = person_w() + ' ist ' + adjektiv() + e50(r.choice(['. Alle', ', aber']) + ' ihre Freunde lieben sie dafür') + '.'
	return erste_gross(s)


def satz_farbe():
	"""
	Generiert einen Satz nach dem Muster: Braun ist eine unsittliche Farbe.
	"""
	s = farbe() + ' ist eine ' + adjektiv() + 'e ' + 'Farbe.'
	return erste_gross(s)


def satz_adjektiv_sprichwort():
	"""
	Generiert einen Satz nach dem Muster: Je untrainierter desto lächerlicher.
	"""
	adjektiv1, adjektiv2 = adjektiv(), adjektiv()
	while adjektiv1 is adjektiv2:
		adjektiv2 = adjektiv()
	s = 'Je ' + adjektiv1 + 'er desto ' + adjektiv2 + 'er.'
	return erste_gross(s)


def satz_adjektiv_am_ort():
	"""
	Generiert einen Satz nach dem Muster: <Ort> <Verb> <Person> <Adjektiv>.

	Beispiel: Auf dem Spielplatz ist die Freundin hilfsbereit.
	"""
	s = ort() + ' ' + r.choice(['war', 'ist']) + ' ' + person() + ' ' + e50(r.choice(['sehr', 'ziemlich', 'ein bischen', 'nicht sehr', 'garnicht', 'nicht']) + ' ') + adjektiv() + '.'
	return erste_gross(s)


def satz_thema():
	"""
	Generiert einen Satz zu einem zufälligen Thema.
	"""
	return r.choice([satz_nulltransitiv, satz_baum, satz_band, satz_kloster, satz_folgehandlung, satz_freunde_lieben, satz_adjektiv_am_ort, satz_absurde_farbfunktion, satz_farbe, satz_adjektiv_sprichwort, satz_arbeit, satz_essen, satz_koerperteil])()


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
	s = ort() + ' ' + v1 + ' ' + person() + e75(' ' + adjektiv()) + v2 + '.'
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
	s = adjektiv() + ' ' + v1 + ' ' + person() + e75(' ' + ort()) + v2 + '.'
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
	s = e50(r.choice(['Warum ', 'Wieso ', 'Weshalb '])) + v1 + ' ' + person() + r.choice([' ' + adjektiv(), ' ' + ort(), ' ' + adjektiv() + ' ' + ort(), '']) + v2 + '?'
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
	s = 'Wo ' + v1 + ' ' + person() + e25(' ' + adjektiv()) + v2 + '?'
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
	s = 'Wie ' + v1 + ' ' + person() + e50(' ' + ort()) + v2 + '?'
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
	s = 'Wann ' + v1 + ' ' + person() + e50(' endlich') + e25(' ' + ort()) + v2 + '?'
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

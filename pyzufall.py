#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Generiert unter anderem Namen, Orte, Fantasieworte, Berufsbezeichnungen und letztendlich ganze Sätze.
"""

import random
import re
import os


r = random.SystemRandom() # Uses /dev/urandom or Windows CryptGenRandom for better entropy

def lese(dateiname):
	"""
	Liest die Datei mit dem übergebenen Namen aus data/ zeilenweise ein und gib eine Liste zurück.

	http://stackoverflow.com/questions/10174211/make-an-always-relative-to-current-module-file-path
	http://stackoverflow.com/questions/595305/python-path-of-scrip
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


def e16(wort):
	"""
	Das übergebene Wort wird mit einer Wahrscheinlichkeit von 16% zurückgegeben.
	"""
	if r.randint(0,5) == 1:
		return wort
	else:
		return ''

def e25(wort):
	"""
	Das übergebene Wort wird mit einer Wahrscheinlichkeit von 25% zurückgegeben.
	"""
	if r.randint(1,4) == 1:
		return wort
	else:
		return ''

def e50(wort):
	"""
	Das übergebene Wort wird mit einer Wahrscheinlichkeit von 50% zurückgegeben.
	"""
	if r.randint(0,1):
		return wort
	else:
		return ''

def e75(wort):
	"""
	Das übergebene Wort wird mit einer Wahrscheinlichkeit von 75% zurückgegeben.
	"""
	if r.randint(0,3):
		return wort
	else:
		return ''

def ersten_buchstaben_gross(s):
	"""
	Macht den ersten Buchstaben gross.	
	"""
	return s[0].upper() + s[1:]


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

def nachname():
	"""
	Gibt einen Nachnamen zurück.
	"""
	return r.choice(nachnamen)

def verbn():
	"""
	Gibt ein nullwertiges Verb zurück.

	http://de.wikipedia.org/wiki/Transitivität_(Grammatik)#Festlegung_der_Transitivit.C3.A4t_eines_Verbs
	"""
	return r.choice(nullwertige_verben)

def verbi():
	"""
	Gibt ein intransitives Verb zurück.

	http://de.wikipedia.org/wiki/Transitivität_(Grammatik)#Festlegung_der_Transitivit.C3.A4t_eines_Verbs
	"""
	return r.choice(intransitive_verben)
	
def verbi2():
	"""
	Gibt ein intransitives, getrenntes Verb zurück.

	http://de.wikipedia.org/wiki/Transitivität_(Grammatik)#Festlegung_der_Transitivit.C3.A4t_eines_Verbs
	"""
	return r.choice(intransitive_verben_2)

def verbt():
	"""
	Gibt ein transitives Verb zurück.

	http://de.wikipedia.org/wiki/Transitivität_(Grammatik)#Festlegung_der_Transitivit.C3.A4t_eines_Verbs
	"""
	return r.choice(transitive_verben)

def verbt2():
	"""
	Gibt ein intransitives, getrenntes Verb zurück.

	http://de.wikipedia.org/wiki/Transitivität_(Grammatik)#Festlegung_der_Transitivit.C3.A4t_eines_Verbs
	"""
	return r.choice(transitive_verben_2)

def verbd():
	"""
	Gibt ein ditransitives Verb zurück.

	http://de.wikipedia.org/wiki/Transitivität_(Grammatik)#Festlegung_der_Transitivit.C3.A4t_eines_Verbs
	"""
	return r.choice(ditransitive_verben)

def adj():
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
		s = e25(adj() + 'er ')
		s = re.sub('eer $', 'er ', s) # feigeer
		s = r.choice([vorname_m(), vorname_w()]) + 's ' + s + r.choice(beziehung_m)
	elif z == 2:
		s = e25(adj() + 'er ')
		s = re.sub('eer $', 'er ', s) # feigeer
		s = r.choice(possessivpronomen_m) + ' ' + s + r.choice(beziehung_m)
	elif z == 3:
		s =  e50(adj() + 'e ')
		s = re.sub('ee $', 'e ', s) # der feigee
		s = 'der ' + s + r.choice(beziehung_m)
	elif z == 4:
		s = adj() + 'e '
		s = re.sub('ee $', 'e ', s) # der feigee
		s = 'der ' + s + r.choice(vornamen_m)
	elif z == 5:
		s = adj() + 'e'
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
		s = e25(adj() + 'e ')
		s = re.sub('ee $', 'e ', s) # feigee
		s = r.choice([vorname_m(), vorname_w()]) + 's ' + s + r.choice(beziehung_w)
	elif z == 2:
		s = e25(adj() + 'e ')
		s = re.sub('ee $', 'e ', s) # die feigee
		s = r.choice(possessivpronomen_m) + 'e ' + s + r.choice(beziehung_w)
	elif z == 3:
		s =  e50(adj() + 'e ')
		s = re.sub('ee $', 'e ', s) # die feigee
		s = 'die ' + s + r.choice(beziehung_w)
	elif z == 4:
		s = adj() + 'e '
		s = re.sub('ee $', 'e ', s) # die feigee
		s = 'die ' + s + vorname_w()
	elif z == 5:
		s = adj() + 'e'
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
	Gibt eine Person zurück.
	"""
	if r.randint(0,1):
		return person_m()
	else:
		return person_w()

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

def datum():
	"""
	Gibt ein Datum zwischen dem 01.01.1950 und 31.12.2012 zurück.
	"""
	return str(r.randint(1,31)) + '.' + str(r.randint(1,12)) + '.' + str(r.randint(1950,2012))

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
	"""
	y = r.randint(1,4)
	if y == 1:
		s = vorname_m()
	if y == 2:
		s = vorname_w()
	if y == 3:
		s =  e25(adj() + 'en ')
		s = re.sub('een ', 'en ', s) # feigeen
		s = r.choice(['seinen ', 'deinen ']) + s + r.choice(beziehung_m)
		s = re.sub('Kollege', 'Kollegen', s)
	if y == 4:
		s =  e25(adj() + 'e ')
		s = re.sub('ee ', 'e ', s) # feigee
		s = r.choice(['seine ', 'deine ']) + s + r.choice(beziehung_w)
		
	return s

def person_objekt_w():
	"""
	Gibt eine Person als Objekt in Bezug auf eine weibliche Person zurück.
	"""
	y = r.randint(1,4)
	if y == 1:
		s = vorname_m()
	if y == 2:
		s = vorname_w()
	if y == 3:
		s =  e25(adj() + 'en ')
		s = re.sub('een ', 'en ', s) # feigeen
		s = r.choice(['ihren ', 'deinen ']) + s + r.choice(beziehung_m)
		s = re.sub('Kollege', 'Kollegen', s)
	if y == 4:
		s =  e25(adj() + 'e ')
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
def essen(anz):
	"""
	Gibt Essen zurück.

	.. todo::
	
		Sollte in zwei Funktionen aufgeteilt werden.
	"""
	if anz: # zusammengesetzt aus zwei Wörtern
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
	if r.randint(0,3):
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
		s = 'Die ' + adj().capitalize() + 'en ' + r.choice(gruppe)
	if z == 1:
		s = r.choice(geschmack) + ' ' + ort()
	if z == 2:
		s = adj().capitalize() + ' ' + ort()
	if z == 3:
		s = adj().capitalize() + 'e ' + essen(r.randint(0,2))
	if z == 4:
		s = adj().capitalize()
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

	TODO
	"""
	pass

#
# TODO
# Jedes Satzschema als Funktion mit Docstring und Beispiel.
# Hirarchie erhalten in satz()
# 
besetzung = ['Sänger', 'Gitarrist', 'Keyboarder', 'Bassist', 'Schlagzeuger', 'Manager', 'Geiger', 'Trompeter', 'Saxophonist', 'Backgroundsänger']
def themen_satz():
	"""
	Gibt einen Satz zu einem zufälligen Themen-Komplex zurück.
	"""
	x = r.randint(1,6)
	
	if x == 1: # Im Park schneit es. / Es stürmt.
		if r.randint(0,2):
			s = ort() + ' ' + verbn() + ' es' + e25(' ' + adj())
		else:
			s = 'Es ' + verbn() + e25(' ' + adj())
	
	if x == 2: # Baum
		if r.randint(0,1):
			s = person_m() + ' ' + r.choice(['pflanzt', 'klettert auf', 'fällt', 'zersägt', 'stellt sich unter', 'umarmt', 'tritt gegen']) + ' ' + objekt_m(baum())
		else:
			s = person_w() + ' ' + r.choice(['pflanzt', 'klettert auf', 'fällt', 'zersägt', 'stellt sich unter', 'umarmt', 'tritt gegen']) + ' ' + objekt_w(baum())
	
	if x == 3: # Körper
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
			s = re.sub('der ', 'einen ' + adj() + 'en ', s)
			s = re.sub('die ', 'eine ' + adj() + 'e ', s)
			s = re.sub('das ', 'ein ' + adj() + 'es ', s)
			s = person() + ' hat ' + s

	if x == 4: # Essen & Trinken
		x = r.randint(1,3)
		if x == 1: # Essen mit Beilage
			s = person() + e25(' ' + r.choice(['ist', 'sitzt', 'befindet sich']) + ' ' + ort() + ' und') + ' isst ' + e50(r.choice(['gerade', 'oft', 'nicht oft', 'selten', 'gerne', 'nicht gerne']) + ' ') + essen(r.randint(0,2)) + e50(' mit ' + r.choice(['viel', 'ganz viel', 'ein bischen', 'ein wenig', 'lecker', 'einer großen Portion']) + ' ' + beilage())
		if x == 2: # Trinken
			s = person() + ' trinkt ' + e50(r.choice(['gerade', 'oft', 'nicht oft', 'selten', 'gerne', 'nicht gerne', 'jeden Abend ein Glas', 'zu viel']) + ' ') + trinken()
		if x == 3: # Essen und Trinken
			s = person() + ' isst ' + essen(r.randint(0,2)) + e50(' mit ' + beilage()) + ' und trinkt ' + e50('dazu ') + trinken()

	if x == 5: # Arbeit
		x = r.randint(1,4)
		if x == 1:
			s = vorname_m() + e50(' ' + nachname()) + ' ist ' + e75('ein ') + beruf_m() + e25(' aus ' + stadt())
		if x == 2:
			s = vorname_w() + e50(' ' + nachname()) + ' ist ' + e50('eine ') + beruf_w() + e50(' aus ' + stadt())
		if x == 3:
			s = vorname_m() + e50(' ' + nachname()) + e50(', der ' + beruf_m() + e50(' aus ' + stadt()) + ',') + ' ' + verbt() + ' ' + r.choice([person_objekt_m(), objekt_m(objekt())])
		if x == 4:
			s = vorname_w() + e50(' ' + nachname()) + e50(', die ' + beruf_w() + e50(' aus ' + stadt()) + ',') + ' ' + verbt() + ' ' + r.choice([person_objekt_w(), objekt_w(objekt())])
	
	if x == 6: # Absurd
		x = r.randint(1,8)
		if x == 1:
			s = person_m() + ' ist ' + adj() + e50(r.choice(['. Alle', ', aber']) + ' seine Freunde lieben ihn dafür')
		if x == 2:
			s = person_w() + ' ist ' + adj() + e50(r.choice(['. Alle', ', aber']) + ' ihre Freunde lieben sie dafür')
		if x == 3:
			adj1 = adj()
			adj2 = adj()
			while adj1 is adj2:
				adj2 = adj()
			s = 'Je ' + adj1 + 'er desto ' + adj2 + 'er'
		if x == 4:
			s = farbe() + ' ist eine ' + adj() + 'e ' + 'Farbe'
		if x == 5:
			farbe1, farbe2, farbe3 = farbe(), farbe(), farbe()
			while farbe1 is farbe2 or farbe2 is farbe3 or farbe1 is farbe3:
				farbe1, farbe2, farbe3 = farbe(), farbe(), farbe()
			s = farbe1 + ' ist ' + r.choice([farbe2.lower(), adj()]) + 'er als ' + farbe3
		if x == 6:
			s = ort() + ' ' + r.choice(['war', 'ist']) + ' ' + r.choice(['er', 'sie', 'es']) + ' ' + e50(r.choice(['sehr', 'ziemlich', 'ein bischen', 'nicht sehr', 'garnicht', 'nicht']) + ' ') + adj()
		if x == 7:
			s = 'Bruder ' + vorname_m() + r.choice([' war', ' ist']) + ' der ' + adj() + 'ste Mönch ' + r.choice(['im Kloster', 'im Orden', 'in der Abtei'])
		if x == 8:
			s = 'Schwester ' + vorname_w() + r.choice([' war', ' ist']) + ' die ' + adj() + 'ste Nonne ' + r.choice(['im Kloster', 'im Orden', 'in der Abtei'])

	return s + '.'

def standard_satz():
	"""
	Gibt einen einfachen Satz, bestehend aus Person, Verb, Adjektiv, Ort und teilweise auch Objekt zurück.
	"""
	x = r.randint(1,5)
	
	if x == 1:
		if r.randint(0,1):
			v1, v2 = verbi2().split(",")
		else:
			v1, v2 = verbi(), ''
		s = person() + ' ' + v1 + ' ' + r.choice([adj(), ort(), adj() + ' ' + ort()]) + v2
	
	if x == 2:
		if r.randint(0,1):
			v1, v2 = verbi2().split(",")
		else:
			v1, v2 = verbi(), ''
		s = ort() + ' ' + v1 + ' ' + person() + e75(' ' + adj()) + v2
	
	if x == 3:
		if r.randint(0,1):
			v1, v2 = verbi2().split(",")
		else:
			v1, v2 = verbi(), ''
		s = adj() + ' ' + v1 + ' ' + person() + e75(' ' + ort()) + v2
	
	if x == 4:
		if r.randint(0,1):
			v1, v2 = verbt2().split(",")
		else:
			v1, v2 = verbt(), ''
		s = person_m() + ' ' + v1 + ' ' + r.choice([person_objekt_m(), objekt_m(objekt())]) + r.choice([' ' + adj(), ' ' + ort(), ' ' + adj() + ' ' + ort(), '']) + v2
	
	if x == 5:
		if r.randint(0,1):
			v1, v2 = verbt2().split(",")
		else:
			v1, v2 = verbt(), ''
		s = person_w() + ' ' + v1 + ' ' + r.choice([person_objekt_w(), objekt_w(objekt())]) + r.choice([' ' + adj(), ' ' + ort(), ' ' + adj() + ' ' + ort(), '']) + v2
	
	return s + e16(r.choice(ns)) + '.'

def frage():
	"""
	Gibt eine Frage zurück.
	"""
	x = r.randint(1,5)
	
	if x == 1:
		if r.randint(0,1):
			v1, v2 = verbi2().split(",")
		else:
			v1, v2 = verbi(), ''
		s = e50(r.choice(['Warum ', 'Wieso ', 'Weshalb '])) + v1 + ' ' + person() + r.choice([' ' + adj(), ' ' + ort(), ' ' + adj() + ' ' + ort(), '']) + v2
	if x == 2:
		if r.randint(0,1):
			v1, v2 = verbi2().split(",")
		else:
			v1, v2 = verbi(), ''
		s = 'Wer ' + v1 + ' ' + r.choice([adj(), ort(), adj() + ' ' + ort()]) +v2
	if x == 3:
		if r.randint(0,1):
			v1, v2 = verbi2().split(",")
		else:
			v1, v2 = verbi(), ''
		s = 'Wo ' + v1 + ' ' + person() + e25(' ' + adj()) +v2
	if x == 4:
		if r.randint(0,1):
			v1, v2 = verbi2().split(",")
		else:
			v1, v2 = verbi(), ''
		s = 'Wie ' + v1 + ' ' + person() + e50(' ' + ort()) +v2
	if x == 5:
		if r.randint(0,1):
			v1, v2 = verbi2().split(",")
		else:
			v1, v2 = verbi(), ''
		s = 'Wann ' + v1 + ' ' + person() + e50(' endlich') + e25(' ' + ort()) +v2
	
	return s + '?'


def satz():
	"""
	Gibt einen Satz zurück.
	"""
	s = r.choice((themen_satz, standard_satz, frage))()

	#s = ersten_buchstaben_gross(themen_satz())
	return s

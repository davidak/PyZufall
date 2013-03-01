#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import re

r = random.SystemRandom() # Uses /dev/urandom or Windows CryptGenRandom for better entropy

# Daten aus Dateien einlesen
vornamen_m = open('data/vornamen_m', 'r').read().splitlines()
vornamen_w = open('data/vornamen_w', 'r').read().splitlines()
vornamen = vornamen_m + vornamen_w
nachnamen = open('data/nachnamen', 'r').read().splitlines()

pflanzen = open('data/pflanzen', 'r').read().splitlines()
baeume = open('data/baeume', 'r').read().splitlines()
tiere = open('data/tiere', 'r').read().splitlines()
gegenstaende = open('data/gegenstaende', 'r').read().splitlines()
koerperteile = open('data/koerperteile', 'r').read().splitlines()

# http://de.wikipedia.org/wiki/Transitivität_(Grammatik)#Festlegung_der_Transitivit.C3.A4t_eines_Verbs
nullwertige_verben = open('data/nullwertige_verben', 'r').read().splitlines()
intransitive_verben = open('data/intransitive_verben', 'r').read().splitlines()
intransitive_verben_2 = open('data/intransitive_verben_2', 'r').read().splitlines()
transitive_verben = open('data/transitive_verben', 'r').read().splitlines()
transitive_verben_2 = open('data/transitive_verben_2', 'r').read().splitlines()
ditransitive_verben = open('data/ditransitive_verben', 'r').read().splitlines()

adjektive = open('data/adjektiv', 'r').read().splitlines()

ortsangabe = open('data/ort', 'r').read().splitlines()
stadte = open('data/stadt_bundesland', 'r').read().splitlines()
nahrung = open('data/nahrung', 'r').read().splitlines()
geschmack = open('data/geschmack', 'r').read().splitlines()
berufe = open('data/berufe', 'r').read().splitlines()
musik = open('data/musikgenre', 'r').read().splitlines()
sprichwoerter = open('data/sprichwoerter', 'r').read().splitlines()
ns = open('data/nebensatz', 'r').read().splitlines()


# ECHO50: 50% Chance, dass das übergebene Wort zurückgegeben wird
def e16(wort):
	if r.randint(0,5) == 1:
		return wort
	else:
		return ''

def e25(wort):
	if r.randint(1,4) == 1:
		return wort
	else:
		return ''

def e50(wort):
	if r.randint(0,1):
		return wort
	else:
		return ''

def e75(wort):
	if r.randint(0,3):
		return wort
	else:
		return ''


def ersten_buchstaben_gross(s):
    return s[0].upper() + s[1:]


# Verben
def verbn():
	return r.choice(nullwertige_verben)

def verbi():
	return r.choice(intransitive_verben)
	
def verbi2():
	return r.choice(intransitive_verben_2)

def verbt():
	return r.choice(transitive_verben)

def verbt2():
	return r.choice(transitive_verben_2)

def verbd():
	return r.choice(ditransitive_verben)

# Adjektiv
def adj():
	return r.choice(adjektive)

# Gegenstand
def gegenstand():
	return r.choice(gegenstaende)

# Körperteile
def koerperteil():
	return r.choice(koerperteile)

# Tier
def tier():
	return r.choice(tiere)

# Baum
def baum():
	return r.choice(baeume)

# Pflanze
def pflanze():
	return r.choice(pflanzen)


# Person generieren
beziehung_m = ['Vater', 'Bruder', 'Mann', 'Sohn', 'Onkel', 'Opa', 'Cousin', 'Enkel', 'Chef', 'Freund', 'Partner', 'Kollege', 'Mitarbeiter', 'Mitbewohner', 'Vermieter', 'Lehrer']
beziehung_w = ['Mutter', 'Schwester', 'Frau', 'Tochter', 'Tante', 'Oma', 'Cousine', 'Enkelin', 'Cheffin', 'Freundin', 'Partnerin', 'Kollegin', 'Mitarbeiterin', 'Mitbewohnerin', 'Vermieterin', 'Lehrerin']
possessivpronomen_m = ['mein', 'dein', 'sein', 'ihr']

personen = ['er', 'sie', 'es', 'jemand', 'niemand']

spezial_m = ['ein Held', 'ein Penner', 'ein Verkäufer', 'ein Zuhälter', 'ein Lehrer', 'ein Polizist', 'ein Beamter', 'ein Arzt', 'Hitler', 'ein Bernd', 'ein Schwuler', 'ein Behinderter', 'der Affenmensch', 'der Satanist', 'der Alkoholiker', 'ein normaler Mensch', 'ein Pirat', 'ein Hartz-IV-Empfänger', 'ein Müllmann']
spezial_w = ['eine Heldin', 'eine Pennerin', 'eine Verkäuferin', 'eine Zuhälterin', 'eine Prostituierte', 'eine Nutte', 'eine Hure', 'eine Schlampe', 'eine Lehrerin', 'eine Polizistin', 'eine Beamtin', 'eine Ärztin', 'eine Behinderte', 'eine Sekretärin', 'die Transe', 'das Mannsweib', 'das Penismädchen', 'die Lesbe', 'die Kampflesbe', 'die Satanistin', 'die Alkoholikerin', 'die Piratin', 'die Hartz-IV-Empfängerin']

def person_m():
	z = r.randint(1,10)
	if z == 1:
		s = e25(adj() + 'er ')
		s = re.sub('eer $', 'er ', s) # feigeer
		s = r.choice(vornamen) + 's ' + s + r.choice(beziehung_m)
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
		s = r.choice(['der ', 'ein ']) + beruf()
	elif z == 7:
		s = r.choice(spezial_m)
	elif z == 8:
		s = 'er'
	else:
		s = r.choice(vornamen_m)
	return s

def person_w():
	z = r.randint(1,10)
	if z == 1:
		s = e25(adj() + 'e ')
		s = re.sub('ee $', 'e ', s) # feigee
		s = r.choice(vornamen) + 's ' + s + r.choice(beziehung_w)
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
		s = 'die ' + s + r.choice(vornamen_w)
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
		s = r.choice(vornamen_w)
	return s

def person():
	if r.randint(0,1):
		s = person_m()
	else:
		s = person_w()
	return s


# Wort
vokal = ['a', 'e', 'i', 'o', 'u', 'ei', 'au']
konsonant = ['b', 'c', 'd', 'f', 'g', 'h', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'sch']
konsonant2 = ['h', 'k', 'l', 'm', 'n', 's', 't']

def wort():
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


# Zahl
def zahl():
	s = r.randint(0,100)
	return str(s)


# Farbe
farben = ['Rot', 'Gelb', 'Blau', 'Violett', 'Türkis', 'Orange', 'Grün', 'Magenta', 'Braun', 'Grau', 'Weiß', 'Schwarz']
def farbe():
	s = r.choice(farben)
	return s


# Farben auf englisch
colors = ['red', 'yellow', 'blue', 'violet', 'orange', 'green', 'magenta', 'brown', 'gray', 'white', 'black']
def color():
	s = r.choice(colors)
	return s


# Datum
def datum():
	s = str(r.randint(1,31)) + '.' + str(r.randint(1,12)) + '.' + str(r.randint(1950,2012))
	return s


# Sprichwort
def sprichwort():
	s = r.choice(sprichwoerter)
	return s


# Berufsbezeichnung
def beruf():
	s = r.choice(berufe)
	return s


# Berufsbezeichnung weiblich
def beruf_w():
	s = beruf() + 'in'
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

# Objekt
def objekt():
	return r.choice([gegenstand(), tier(), pflanze(), baum()])

# Grammatikalisches Objekt
def objekt_m(s):
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
	y = r.randint(1,4)
	if y == 1:
		s = r.choice(vornamen_m)
	if y == 2:
		s = r.choice(vornamen_w)
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
	y = r.randint(1,4)
	if y == 1:
		s = r.choice(vornamen_m)
	if y == 2:
		s = r.choice(vornamen_w)
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


# Ortsangabe
def ort():
	tausende = ['500', '1000', '2000', '5000', '10000', '100000']
	if r.randint(0,3):
		zuschauer = r.choice(tausende)
	else:
		zuschauer = str(r.randint(1,10000))

	s = r.choice(ortsangabe)
	s = re.sub('auf Gleis XX$', 'auf Gleis ' + str(r.randint(1,14)), s)
	s = re.sub('XXZusch', zuschauer, s)
	s = re.sub('XXName', r.choice(vornamen) + 's', s)
	return s


# Essen und Beilage generieren
voressen = ['Brat', 'Rühr', 'Reibe', 'Brech', 'Back', 'Ofen', 'Hack', 'Mager', 'Frisch', 'Bio', 'Gammel', 'Soja', 'Tofu', 'Milch']

def essen(anz):
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
	if r.randint(0,3):
		s = r.choice(beilag2)
	else:
		s = r.choice(geschmack) + r.choice(beilag).lower()
	return s


# Trinken generieren
getraenk = ['Wasser', 'Saft', 'Tee', 'Kaffee', 'Eistee', 'Milch', 'Punsch', 'Bowle', 'Bier', 'Likör',  'Wein', 'Rum', 'Sekt', 'Schnaps', 'Cocktail']

def trinken():
	if r.randint(0,2):
		s = r.choice(geschmack) + r.choice(getraenk).lower()
	else:
		s = r.choice(getraenk)
	return s


# Stadt
def stadt():
	s = r.choice(stadte).split(' (', 1) # Stadt und Bundesland trennen
	s = s[0] # Nur Stadt, nicht Bundesland
	return s


# Stadt mit Bundesland
def stadt_bl():
	s = r.choice(stadte)
	return s


# Band
gruppe = ['Menschen', 'Personen', 'Kinder', 'Tiere', 'Gedärme', 'Kadaver', 'Nudeln', 'Unterhosen', 'Würstchen', 'Bäume', 'Stühle', 'Schweine', 'Neger', 'Alkoholiker', 'Leichen']

def band():
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


# Bandart
def bandart():
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


# Firma


# Satz generieren

# Themen-Satz
besetzung = ['Sänger', 'Gitarrist', 'Keyboarder', 'Bassist', 'Schlagzeuger', 'Manager', 'Geiger', 'Trompeter', 'Saxophonist', 'Backgroundsänger']

def themen_satz():
	x = 3#r.randint(1,10)
	
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
			s = s + ' ' + r.choice(['tut weh', 'schmerzt', 'blutet', 'juckt', 'brennt'])
		if x == 5:
			s = koerperteil()
			s = re.sub('der ', 'einen ' + adj() + 'en ', s)
			s = re.sub('die ', 'eine ' + adj() + 'e ', s)
			s = re.sub('das ', 'ein ' + adj() + 'es ', s)
			s = person() + ' hat ' + s

	return s + '.'


# Standard-Satz
def standard_satz():
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

# Frage
def frage():
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
	#s = ersten_buchstaben_gross(r.choice([themen_satz(), standard_satz(), frage()]))
	s = ersten_buchstaben_gross(themen_satz())
	return s

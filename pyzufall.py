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
geschmack = open('data/geschmack', 'r').read().splitlines()
nahrung = open('data/nahrung', 'r').read().splitlines()
ns = open('data/nebensatz', 'r').read().splitlines()
verb = open('data/verb', 'r').read().splitlines()
verb2 = open('data/verb2', 'r').read().splitlines()
adj = open('data/adjektiv', 'r').read().splitlines()
ortsangabe = open('data/ort', 'r').read().splitlines()
stadte = open('data/stadt_bundesland', 'r').read().splitlines()
berufe = open('data/berufe', 'r').read().splitlines()
musik = open('data/musikgenre', 'r').read().splitlines()
sprichwoerter = open('data/sprichwoerter', 'r').read().splitlines()

# ECHO50: 50% Chance, dass das übergebene Wort zurückgegeben wird
def e5(wort):
	if r.randint(0,1):
		return wort
	else:
		return ''


def ersten_buchstaben_gross(s):
    return s[0].upper() + s[1:]


# Person generieren
beziehung_m = ['Vater', 'Bruder', 'Mann', 'Sohn', 'Onkel', 'Opa', 'Cousin', 'Enkel', 'Chef', 'Freund', 'Partner', 'Kollege', 'Mitarbeiter', 'Mitbewohner', 'Vermieter', 'Lehrer']
beziehung_w = ['Mutter', 'Schwester', 'Frau', 'Tochter', 'Tante', 'Oma', 'Cousine', 'Enkelin', 'Cheffin', 'Freundin', 'Partnerin', 'Kollegin', 'Mitarbeiterin', 'Mitbewohnerin', 'Vermieterin', 'Lehrerin']
possessivpronomen_m = ['mein', 'dein', 'sein', 'ihr']

personen = ['er', 'sie', 'es', 'jemand', 'niemand']

spezial_m = ['ein Held', 'ein Penner', 'ein Verkäufer', 'ein Zuhälter', 'ein Lehrer', 'ein Polizist', 'ein Beamter', 'ein Arzt', 'Hitler', 'ein Bernd', 'ein Schwuler', 'ein Behinderter', 'der Affenmensch', 'der Satanist', 'der Alkoholiker', 'ein normaler Mensch', 'ein Pirat', 'ein Hartz-IV-Empfänger', 'ein Müllmann']
spezial_w = ['eine Heldin', 'eine Pennerin', 'eine Verkäuferin', 'eine Zuhälterin', 'eine Prostituierte', 'eine Nutte', 'eine Hure', 'eine Schlampe', 'eine Lehrerin', 'eine Polizistin', 'eine Beamtin', 'eine Ärztin', 'eine Behinderte', 'eine Sekretärin', 'die Transe', 'das Mannsweib', 'das Penismädchen', 'die Lesbe', 'die Kampflesbe', 'die Satanistin', 'die Alkoholikerin', 'die Piratin', 'die Hartz-IV-Empfängerin']

def person_m():
	z = r.randint(1,7)
	if z == 1:
		s = r.choice(vornamen) + 's ' + r.choice(beziehung_m)
	elif z == 2:
		s = r.choice(possessivpronomen_m) + ' ' + r.choice(beziehung_m)
	elif z == 3:
		s = 'der ' + r.choice(beziehung_m)
	elif z == 4:
		s = r.choice(spezial_m)
	elif z == 5:
		s = 'er'
	else:
		s = r.choice(vornamen_m)
	return s

def person_w():
	z = r.randint(1,7)
	if z == 1:
		s = r.choice(vornamen) + 's ' + r.choice(beziehung_w)
	elif z == 2:
		s = r.choice(possessivpronomen_m) + 'e ' + r.choice(beziehung_w)
	elif z == 3:
		s = 'die ' + r.choice(beziehung_w)
	elif z == 4:
		s = r.choice(spezial_w)
	elif z == 5:
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
	s = r.choice(stadte).split(' (', 1)
	s = stadt[0]
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
		s = 'Die ' + r.choice(adj).capitalize() + 'en ' + r.choice(gruppe)
	if z == 1:
		s = r.choice(geschmack) + ' ' + ort()
	if z == 2:
		s = r.choice(adj).capitalize() + ' ' + ort()
	if z == 3:
		s = r.choice(adj).capitalize() + 'e ' + essen(r.randint(0,2))
	if z == 4:
		s = r.choice(adj).capitalize()
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

besetzung = ['Sänger', 'Gitarrist', 'Keyboarder', 'Bassist', 'Schlagzeuger', 'Manager', 'Geiger', 'Trompeter', 'Saxophonist', 'Backgroundsänger']

def satz():
	z = r.randint(0,17)
	
	if z == 2: # Essen
		satz = person() + ' isst'
		x = r.randint(0,10)
		if x == 1:
			satz += ' gerade'
		elif x == 2:
			satz += ' gerne'
		elif x == 3:
			satz += ' nicht gerne'
		elif x == 4:
			satz += ' oft'
		elif x == 5:
			satz += ' selten'
		satz += ' ' + essen(r.randint(0,2))
		if r.randint(0,2):
			satz += ' mit ' + e5(r.choice(['viel ', 'ganz viel ', 'ein bischen ', 'ein wenig ', 'lecker ', 'einer großen Portion '])) + beilage()
		satz += '.'
	
	elif z == 3: # Trinken
		satz = person() + ' trinkt'
		x = r.randint(0,10)
		if x == 1:
			satz += ' gerade'
		elif x == 2:
			satz += ' gerne'
		elif x == 3:
			satz += ' nicht gerne'
		elif x == 4:
			satz += ' oft'
		elif x == 5:
			satz += ' selten'
		elif x == 6:
			satz += ' jeden Abend ein Glas'
		elif x == 7:
			satz += ' zu viel'
		satz += ' ' + trinken() + '.'
	
	elif z == 4: # Essen und Trinken
		satz = person() + ' isst ' + essen(r.randint(0,2)) + e5(' mit ' + beilage()) + ' und trinkt ' + e5('dazu ') + trinken() + '.'
	
	elif z == 5: # Essen oder Trinken am Ort
		satz = person() + ' ' + r.choice(['ist', 'sitzt', 'befindet sich']) + ' ' + ort() + ' und '
		if r.randint(0,1):
			satz += 'isst ' + e5('dort ') + essen(r.randint(0,2)) +e5(' mit ' + beilage())
		else:
			satz += 'trinkt ' + e5('dort ') + trinken()
		satz += '.'
	
	elif z == 6: # Bandmitglieder Besetzung
		if r.randint(0,1): # männlich
			satz = r.choice(vornamen_m) + e5(' ' + r.choice(nachnamen)) + ' ist ' + e5('der ') + r.choice(besetzung) + e5(' von') + ' der ' + bandart() + ' "' + band() + '".'
		else: # weiblich
			satz = r.choice(vornamen_w) + e5(' ' + r.choice(nachnamen)) + ' ist ' + e5('die ') + r.choice(besetzung) + 'in' + e5(' von') + ' der ' + bandart() + ' "' + band() + '".'
	
	elif z == 7: # Band gegründet
		if r.randint(0,1):
			satz = 'Die ' + bandart() + ' ' + band() + ' wurde'
		else:
			satz = band() + ' (' + bandart() + ') wurde'
		if r.randint(0,1): # 50% Datum oder Jahr
			satz += ' am ' + datum()
		else:
			if r.randint(0,1):
				satz += ' ' + r.choice(['Anfang', 'Mitte', 'Mitte des Jahres', 'Ende', 'im Frühling', 'im Sommer', 'im Herbst', 'im Winter'])
			satz += ' ' + str(r.randint(1950, 2013))
		if r.randint(0,1): # 50% Ort
			satz += ' in ' + stadt()
		satz += ' gegründet.'
	
	elif z == 8: # Bandmitglieder mit oder ohne Nachnamen
		if r.randint(0,2): # ohne
			satz = 'Die '+ bandart() + ' "' + band() + '" besteht aus ' + r.choice(vornamen)
			for i in range(0,r.randint(0,4)): # 2 bis 6 Mitglieder
				satz += ', ' + r.choice(vornamen)
			satz += ' und ' + r.choice(vornamen) + '.'
		else:
			satz = 'Die '+ bandart() + ' "' + band() + '" besteht aus ' + r.choice(vornamen) + ' ' + r.choice(nachnamen)
			for i in range(0,r.randint(0,4)): # 2 bis 6 Mitglieder
				satz += ', ' + r.choice(vornamen) + ' ' + r.choice(nachnamen)
			satz += ' und ' + r.choice(vornamen) + ' ' + r.choice(nachnamen) + '.'
	
	elif z == 9: # Arbeiter
		if r.randint(0,1): # männlich
			satz = r.choice(vornamen_m) + ' ist ' + e5('ein ') + beruf() + e5(' aus ' + stadt()) + '.'
		else: # weiblich
			satz = r.choice(vornamen_w) + ' ist ' + e5('eine ') + beruf_w() + e5(' aus ' + stadt()) + '.'
		# bei firma()
	
	elif z == 10: # X ist beruflich
		if r.randint(0,1): # männlich
			satz = r.choice(vornamen_m) + e5(' ' + r.choice(nachnamen))
			if r.randint(0,1): # 50% Beruf anzeigen
				if r.randint(0,1):
					satz += ', der ' + beruf()
					if r.randint(0,1):
						satz += ' aus ' + stadt()
					satz += ','
				else:
					satz += ' (' + beruf() + ')'
		else: # weiblich
			satz = r.choice(vornamen_w) + e5(' ' + r.choice(nachnamen))
			if r.randint(0,1): # 50% Beruf anzeigen
				if r.randint(0,1):
					satz += ', die ' + beruf_w()
					if r.randint(0,1):
						satz += ' aus ' + stadt()
					satz += ','
				else:
					satz += ' (' + beruf_w() + ')'
		satz += ' ist' + e5(' gerade') + ' beruflich '
		if r.randint(0,2):
			satz += ort()
		else:
			satz += 'in ' + stadt()
		
		if not r.randint(0,3):
			satz += r.choice([', das darf der Chef aber nicht wissen', ', hat aber keine Lust mehr und will nach Hause', ' und hat Gummistiefel an', ' und lacht darüber', ' und ist das schrecklich peinlich', ' und setzt sich erstmal', ' und wird dafür ausgelacht', ' und ist glücklich', ' und hat Spaß dabei', ' und verliert die Hose', ' und fällt hin', ', kennt sich dort aber überhaupt nicht aus'])
		satz += '.'
	
	elif z == 11: # Freunde lieben dafür
		zz = r.randint(0,2)
		if zz == 0: # männlich
			satz = r.choice(vornamen_m) + e5(' ' + r.choice(nachnamen))
			satz += ' ist ' + r.choice(adj)
			if r.randint(0,1): #
				satz += r.choice(['. Alle', ', aber']) + ' seine Freunde lieben ihn dafür.'
			else:
				satz += '.'
		elif zz == 1:	# weiblich
			satz = r.choice(vornamen_w) + e5(' ' + r.choice(nachnamen))
			satz += ' ist ' + r.choice(adj)
			if r.randint(0,1): #
				satz += r.choice(['. Alle', ', aber']) + ' ihre Freunde lieben sie dafür.'
			else:
				satz += '.'
		else:
			satz = 'Ich bin ' + r.choice(adj) + r.choice(['. Alle', ', aber']) + ' meine Freunde lieben mich dafür.'
	
	elif z == 12:
		adj1 = r.choice(adj)
		adj2 = r.choice(adj)
		while adj1 is adj2:
			adj2 = r.choice(adj)
		satz = 'Je ' + adj1 + 'er desto ' + adj2 + 'er.'
	
	elif z == 13: # absurde Farbfunktion
		if r.randint(0,1):
			satz = farbe() + ' ist eine ' + r.choice(adj) + 'e ' + 'Farbe.'
		else:
			farbe1, farbe2, farbe3 = farbe(), farbe(), farbe()
			while farbe1 is farbe2 or farbe2 is farbe3 or farbe1 is farbe3:
				farbe1, farbe2, farbe3 = farbe(), farbe(), farbe()
			satz = farbe1 + ' ist ' + r.choice([farbe2.lower(), r.choice(adj)]) + 'er als ' + farbe3 + '.'
	
	elif z == 14:
		satz = ort() + ' ' + r.choice(['war', 'ist']) + ' ' + r.choice(['er', 'sie', 'es']) + ' ' + e5(r.choice(['sehr', 'ziemlich', 'ein bischen', 'nicht sehr', 'garnicht', 'nicht']) + ' ') + r.choice(adj) + '.'
	
	elif z == 15: # Kloster
		if r.randint(0,1): # männlich
			satz = 'Bruder ' + r.choice(vornamen_m) + r.choice([' war', ' ist']) + ' der ' + r.choice(adj) + 'ste Mönch ' + r.choice(['im Kloster', 'im Orden', 'in der Abtei']) + '.'
		else: # weiblich
			satz = 'Schwester ' + r.choice(vornamen_w) + r.choice([' war', ' ist']) + ' die ' + r.choice(adj) + 'ste Nonne ' + r.choice(['im Kloster', 'im Orden', 'in der Abtei']) + '.'
	
	elif z == 16: # Frage
		if r.randint(0,1): # normales verb
			satz = r.choice(['Warum ', 'Wieso ', 'Weshalb ', '']) + r.choice(verb) + ' ' + person() + e5(' ' + r.choice(adj)) + e5(' ' + ort()) + '?'
		else: # getrenntes verb
			v1, v2 = r.choice(verb2).split(",")
			satz = r.choice(['Warum ', 'Wieso ', 'Weshalb ', '']) + v1 + ' ' + person() + ' ' + e5(r.choice(adj) + ' ') + e5(ort() + ' ') + v2 + '?'
		if not r.randint(0,10):
			satz += ' ' + r.choice(['Mann weiss es nicht.', 'Denk mal drüber nach!'])
	
	elif z == 17: # Folgehandlung
		v1, v2 = r.choice(verb2).split(",")
		v12 = ''
		if ' ' in v1: # bildet sich => bilder ER sich
			v1, v12 = v1.split(' ')
			v12 += ' '
		
		verb1 = r.choice(verb)
		verb12 = ' '
		if ' ' in verb1:
			verb1, verb12 = verb1.split(' ')
			verb12 = ' ' + verb12 + ' '
		
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
		
		satz = r.choice(['Weil', 'Während', 'Obwohl', 'Ohne dass', 'Nur weil', 'Gerade weil']) + r.choice([verb12 + erste_person + ' ', ' ' + erste_person + verb12]) + e5(ort() + ' ') + e5(r.choice(adj) + ' ') + verb1 + ', ' + v1 + zweit_person + v12 + e5(r.choice(adj) + ' ') + v2 + '.'
	
	else:
		if r.randint(0,1): # Standardsatz mit getrenntem Verb
			v1, v2 = r.choice(verb2).split(",")
			satz = person() + ' ' + v1
			if r.randint(0,3):
				satz += ' ' + r.choice(adj)
			if r.randint(0,2):
				satz += ' ' + ort()
			satz += ' ' + v2
		else: # Standardsatz
			satz = person() + ' ' + r.choice(verb)
			if r.randint(0,3):
				satz += ' ' + r.choice(adj)
			if r.randint(0,2):
				satz += ' ' + ort()
		if r.randint(0,5) == 1: # Chance 1/6
			satz += r.choice(ns)
		satz += '.'
	
	satz = ersten_buchstaben_gross(satz)
	return satz

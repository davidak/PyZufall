#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import re

random.seed() # Zufallsgenerator initialisieren

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
ort = open('data/ort', 'r').read().splitlines()
stadte = open('data/stadt_bundesland', 'r').read().splitlines()
berufe = open('data/berufe', 'r').read().splitlines()
musik = open('data/musikgenre', 'r').read().splitlines()
sprichwoerter = open('data/sprichwoerter', 'r').read().splitlines()

# ECHO50: 50% Chance, dass das übergebene Wort zurückgegeben wird
def e5(wort):
	if random.randint(0,1):
		return wort
	else:
		return ''


def ersten_buchstaben_gross(s):
    return s[0].upper() + s[1:]


# Person generieren
beziehung_m = ['Vater', 'Bruder', 'Mann', 'Sohn', 'Onkel', 'Opa', 'Cousin', 'Enkel', 'Chef', 'Freund', 'Partner', 'Kollege', 'Mitarbeiter', 'Mitbewohner', 'Vermieter', 'Lehrer']
beziehung_w = ['Mutter', 'Schwester', 'Frau', 'Tochter', 'Tante', 'Oma', 'Cousine', 'Enkelin', 'Cheffin', 'Freundin', 'Partnerin', 'Kollegin', 'Mitarbeiterin', 'Mitbewohnerin', 'Vermieterin', 'Lehrerin']
spezial = ['er', 'sie', 'es', 'jemand', 'niemand', 'ein Held', 'ein Penner', 'ein Verkäufer', 'ein Zuhälter', 'eine Prostituierte', 'eine Nutte', 'eine Hure', 'eine Schlampe', 'ein Lehrer', 'ein Polizist', 'ein Beamter', 'ein Arzt', 'Hitler', 'ein Bernd', 'ein Schwuler', 'ein Behinderter', 'eine Sekretärin', 'der Affenmensch', 'die Transe', 'das Mannsweib', 'das Penismädchen', 'die Lesbe', 'die Kampflesbe', 'der Satanist', 'der Alkoholiker', 'ein normaler Mensch', 'der Pirat', 'der Hartz-IV-Empfänger', 'ein Müllmann']
possessivpronomen_m = ['mein', 'dein', 'sein', 'ihr']

def person():
	z = random.randint(1,12)
	if z == 1:
		person = random.choice(vornamen) + 's ' + random.choice(beziehung_m)
	elif z == 2:
		person = random.choice(vornamen) + 's ' + random.choice(beziehung_w)
	elif z == 3:
		person = random.choice(possessivpronomen_m) + ' ' + random.choice(beziehung_m)
	elif z == 4:
		person = random.choice(possessivpronomen_m) + 'e ' + random.choice(beziehung_w)
	elif z == 5:
		person = 'der ' + random.choice(beziehung_m)
	elif z == 6:
		person = 'die ' + random.choice(beziehung_w)
	elif z == 7:
		person = random.choice(spezial)
	else:
		person = random.choice(vornamen)
	return person


# Wort
vokal = ['a', 'e', 'i', 'o', 'u', 'ei', 'au']
konsonant = ['b', 'c', 'd', 'f', 'g', 'h', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'sch']
konsonant2 = ['h', 'k', 'l', 'm', 'n', 's', 't']

def wort():
	laenge = random.randint(3,12)
	anfaengt = random.randint(1,3)
	text = ""
	
	if anfaengt == 2: # Anfang wird ein Vokal
		text = random.choice(vokal)
		while len(text) < laenge:
			text += random.choice(konsonant)
			if len(text) < laenge and random.randint(0,1):
				text += random.choice(konsonant2)
			if len(text) >= laenge:
				break
			text += random.choice(vokal)

	else: # Anfang wird ein Konsonant
		text = random.choice(konsonant)
		while len(text) < laenge:
			text += random.choice(vokal)
			if len(text) >= laenge:
				break
			text += random.choice(konsonant)
			if len(text) < laenge and random.randint(0,1):
				text += random.choice(konsonant2)
	text = text.capitalize()
	return text


# Zahl
def zahl():
	text = random.randint(0,100)
	return str(text)


# Farbe
farben = ['Rot', 'Gelb', 'Blau', 'Violett', 'Türkis', 'Orange', 'Grün', 'Magenta', 'Braun', 'Grau', 'Weiß', 'Schwarz']
def farbe():
	farbe = random.choice(farben)
	return farbe


# Farben auf englisch
colors = ['red', 'yellow', 'blue', 'violet', 'orange', 'green', 'magenta', 'brown', 'gray', 'white', 'black']
def color():
	color = random.choice(colors)
	return color


# Datum
def datum():
	text = str(random.randint(1,31)) + '.' + str(random.randint(1,12)) + '.' + str(random.randint(1950,2012))
	return text


# Sprichwort
def sprichwort():
	text = random.choice(sprichwoerter)
	return text


# Berufsbezeichnung
def beruf():
	text = random.choice(berufe)
	return text


# Berufsbezeichnung weiblich
def beruf_w():
	text = beruf() + 'in'
	text = re.sub('mannin$', 'frau', text) # Restaurantfachmannin => Restaurantfachfrau
	text = re.sub('kraftin$', 'kraft', text) # Edv-Fachkraftin => Edv-Fachkraft
	text = re.sub('angestellterin$', 'angestellte', text)
	text = re.sub('Fotomodellin$', 'Fotomodell', text)
	text = re.sub('Technischer Zeichnerin$', 'Technische Zeichnerin', text)
	text = re.sub('Arztin$', 'Ärztin', text)
	text = re.sub('arztin$', 'ärztin', text)
	text = re.sub('beamterin$', 'beamtin', text) # Polizeibeamterin => Polizeibeamte
	text = re.sub('ein$', 'in', text) # Mikrobiologein => Mikrobiologin
	return text


# Essen und Beilage generieren
voressen = ['Brat', 'Rühr', 'Reibe', 'Brech', 'Back', 'Ofen', 'Hack', 'Mager', 'Frisch', 'Bio', 'Gammel', 'Soja', 'Tofu', 'Milch']

def essen(anz):
	if anz: # zusammengesetzt aus zwei Wörtern
		if random.randint(0,2):
			essen = random.choice(geschmack) + random.choice(nahrung).lower()
		else:
			essen = random.choice(voressen) + random.choice(nahrung).lower()
	else: # aus einem Wort bestehend
		if random.randint(0,2):
			essen = random.choice(geschmack)
		else:
			essen = random.choice(nahrung)
	return essen

beilag = ['Soße', 'Sauce', 'Brühe', 'Brei', 'Püree', 'Kartoffeln', 'Salat', 'Marmelade']
beilag2 = ['Kroketten', 'Pommes', 'Rösti', 'Röstzwiebeln', 'Mayo', 'Mayonnaise', 'Ketchup', 'Bratkartoffeln', 'Zwiebelringen', 'Kartoffelpuffer', 'Soße', 'Nudeln', 'Gemüse', 'Knödeln', 'Salat', 'Marmelade']
def beilage():
	if random.randint(0,3):
		text = random.choice(beilag2)
	else:
		text = random.choice(geschmack) + random.choice(beilag).lower()
	return text


# Trinken generieren
getraenk = ['Wasser', 'Saft', 'Tee', 'Kaffee', 'Eistee', 'Milch', 'Punsch', 'Bowle', 'Bier', 'Likör',  'Wein', 'Rum', 'Sekt', 'Schnaps', 'Cocktail']

def trinken():
	if random.randint(0,2):
		trinken = random.choice(geschmack) + random.choice(getraenk).lower()
	else:
		trinken = random.choice(getraenk)
	return trinken


# Stadt
def stadt():
	stadt = random.choice(stadte).split(' (', 1)
	stadt = stadt[0]
	return stadt


# Stadt mit Bundesland
def stadt_bl():
	stadt = random.choice(stadte)
	return stadt


# Band
gruppe = ['Menschen', 'Personen', 'Kinder', 'Tiere', 'Gedärme', 'Kadaver', 'Nudeln', 'Unterhosen', 'Würstchen', 'Bäume', 'Stühle', 'Schweine', 'Neger', 'Alkoholiker', 'Leichen']

def band():
	z = random.randint(0,5)
	if z == 0:
		band = 'Die ' + random.choice(adj).capitalize() + 'en ' + random.choice(gruppe)
	if z == 1:
		band = random.choice(geschmack) + ' ' + random.choice(ort)
	if z == 2:
		band = random.choice(adj).capitalize() + ' ' + random.choice(ort)
	if z == 3:
		band = random.choice(adj).capitalize() + 'e ' + essen(random.randint(0,2))
	if z == 4:
		band = random.choice(adj).capitalize()
	if z == 5:
		band = wort()
	return band


# Bandart
def bandart():
	if random.randint(0,2):
		m = random.choice(musik)
		if ' ' in m:
			text = m + ' Band'
		elif '-' in m:
			text = m + '-Band'
		else:
			text = m + 'band'
	else:
		text = random.choice(['Band', 'Musikergruppe'])
	return text


# Firma


# Satz generieren

besetzung = ['Sänger', 'Gitarrist', 'Keyboarder', 'Bassist', 'Schlagzeuger', 'Manager', 'Geiger', 'Trompeter', 'Saxophonist', 'Backgroundsänger']

def satz():
	z = random.randint(0,16)
	
	if z == 2: # Essen
		satz = person() + ' isst'
		x = random.randint(0,10)
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
		satz += ' ' + essen(random.randint(0,2))
		if random.randint(0,2):
			satz += ' mit ' + e5(random.choice(['viel ', 'ganz viel ', 'ein bischen ', 'ein wenig ', 'lecker ', 'einer großen Portion '])) + beilage()
		satz += '.'
	
	elif z == 3: # Trinken
		satz = person() + ' trinkt'
		x = random.randint(0,10)
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
		satz = person() + ' isst ' + essen(random.randint(0,2)) + e5(' mit ' + beilage()) + ' und trinkt ' + e5('dazu ') + trinken() + '.'
	
	elif z == 5: # Essen oder Trinken am Ort
		satz = person()
		if random.randint(0,1):
			satz += ' ist '
		else:
			satz += ' sitzt '
		satz += random.choice(ort) + ' und '
		if random.randint(0,1):
			satz += 'isst ' + e5('dort ') + essen(random.randint(0,2)) +e5(' mit ' + beilage())
		else:
			satz += 'trinkt ' + e5('dort ') + trinken()
		satz += '.'
	
	elif z == 6: # Bandmitglieder Besetzung
		if random.randint(0,1): # männlich
			satz = random.choice(vornamen_m) + e5(' ' + random.choice(nachnamen)) + ' ist ' + e5('der ') + random.choice(besetzung) + e5(' von') + ' der ' + bandart() + ' "' + band() + '".'
		else: # weiblich
			satz = random.choice(vornamen_w) + e5(' ' + random.choice(nachnamen)) + ' ist ' + e5('die ') + random.choice(besetzung) + 'in' + e5(' von') + ' der ' + bandart() + ' "' + band() + '".'
	
	elif z == 7: # Band gegründet
		if random.randint(0,1):
			satz = 'Die ' + bandart() + ' ' + band() + ' wurde'
		else:
			satz = band() + ' (' + bandart() + ') wurde'
		if random.randint(0,1): # 50% Datum oder Jahr
			satz += ' am ' + datum()
		else:
			if random.randint(0,1):
				satz += ' ' + random.choice(['Anfang', 'Mitte', 'Mitte des Jahres', 'Ende', 'im Frühling', 'im Sommer', 'im Herbst', 'im Winter'])
			satz += ' ' + str(random.randint(1950, 2012))
		if random.randint(0,1): # 50% Ort
			satz += ' in ' + stadt()
		satz += ' gegründet.'
	
	elif z == 8: # Bandmitglieder mit oder ohne Nachnamen
		if random.randint(0,2): # ohne
			satz = 'Die '+ bandart() + ' "' + band() + '" besteht aus ' + random.choice(vornamen)
			for i in range(0,random.randint(0,4)): # 2 bis 6 Mitglieder
				satz += ', ' + random.choice(vornamen)
			satz += ' und ' + random.choice(vornamen) + '.'
		else:
			satz = 'Die '+ bandart() + ' "' + band() + '" besteht aus ' + random.choice(vornamen) + ' ' + random.choice(nachnamen)
			for i in range(0,random.randint(0,4)): # 2 bis 6 Mitglieder
				satz += ', ' + random.choice(vornamen) + ' ' + random.choice(nachnamen)
			satz += ' und ' + random.choice(vornamen) + ' ' + random.choice(nachnamen) + '.'
	
	elif z == 9: # Arbeiter
		if random.randint(0,1): # männlich
			satz = random.choice(vornamen_m) + ' ist ' + e5('ein ') + beruf() + e5(' aus ' + stadt()) + '.'
		else: # weiblich
			satz = random.choice(vornamen_w) + ' ist ' + e5('eine ') + beruf_w() + e5(' aus ' + stadt()) + '.'
		# bei firma()
	
	elif z == 10: # X ist beruflich
		if random.randint(0,1): # männlich
			satz = random.choice(vornamen_m) + e5(' ' + random.choice(nachnamen))
			if random.randint(0,1): # 50% Beruf anzeigen
				if random.randint(0,1):
					satz += ', der ' + beruf()
					if random.randint(0,1):
						satz += ' aus ' + stadt()
					satz += ','
				else:
					satz += ' (' + beruf() + ')'
		else: # weiblich
			satz = random.choice(vornamen_w) + e5(' ' + random.choice(nachnamen))
			if random.randint(0,1): # 50% Beruf anzeigen
				if random.randint(0,1):
					satz += ', die ' + beruf_w()
					if random.randint(0,1):
						satz += ' aus ' + stadt()
					satz += ','
				else:
					satz += ' (' + beruf_w() + ')'
		satz += ' ist' + e5(' gerade') + ' beruflich '
		if random.randint(0,2):
			satz += random.choice(ort)
		else:
			satz += 'in ' + stadt()
		
		if not random.randint(0,3):
			satz += random.choice([', das darf der Chef aber nicht wissen', ', hat aber keine Lust mehr und will nach Hause', ' und hat Gummistiefel an', ' und lacht darüber', ' und ist das schrecklich peinlich', ' und setzt sich erstmal', ' und wird dafür ausgelacht', ' und ist glücklich', ' und hat Spaß dabei', ' und verliert die Hose', ' und fällt hin', ', kennt sich dort aber überhaupt nicht aus'])
		satz += '.'
	
	elif z == 11: # Freunde lieben dafür
		zz = random.randint(0,2)
		if zz == 0: # männlich
			satz = random.choice(vornamen_m) + e5(' ' + random.choice(nachnamen))
			satz += ' ist ' + random.choice(adj)
			if random.randint(0,1): #
				satz += random.choice(['. Alle', ', aber']) + ' seine Freunde lieben ihn dafür.'
			else:
				satz += '.'
		elif zz == 1:	# weiblich
			satz = random.choice(vornamen_w) + e5(' ' + random.choice(nachnamen))
			satz += ' ist ' + random.choice(adj)
			if random.randint(0,1): #
				satz += random.choice(['. Alle', ', aber']) + ' ihre Freunde lieben sie dafür.'
			else:
				satz += '.'
		else:
			satz = 'Ich bin ' + random.choice(adj) + random.choice(['. Alle', ', aber']) + ' meine Freunde lieben mich dafür.'
	
	elif z == 12:
		satz = 'Je ' + random.choice(adj) + 'er desto ' + random.choice(adj) + 'er.'
	
	elif z == 13:
		satz = farbe() + ' ist eine ' + random.choice(adj) + 'e ' + 'Farbe.'
	
	elif z == 14:
		satz = ersten_buchstaben_gross(random.choice(ort)) + ' ' + random.choice(['war', 'ist']) + ' ' + random.choice(['er', 'sie', 'es']) + ' ' + e5(random.choice(['sehr', 'ziemlich', 'ein bischen', 'nicht sehr', 'garnicht', 'nicht']) + ' ') + random.choice(adj) + '.'
	
	elif z == 15: # Kloster
		if random.randint(0,1): # männlich
			satz = 'Bruder ' + random.choice(vornamen_m) + random.choice([' war', ' ist']) + ' der ' + random.choice(adj) + 'ste Mönch ' + random.choice(['im Kloster', 'im Orden', 'in der Abtei']) + '.'
		else: # weiblich
			satz = 'Schwester ' + random.choice(vornamen_w) + random.choice([' war', ' ist']) + ' die ' + random.choice(adj) + 'ste Nonne ' + random.choice(['im Kloster', 'im Orden', 'in der Abtei']) + '.'
	
	elif z == 16:
		if random.randint(0,1): # normales verb
			if random.randint(0,1):
				satz = random.choice(['Warum', 'Wieso', 'Weshalb'])
				satz += ' ' + random.choice(verb)
			else:
				satz = random.choice(verb).capitalize()
			satz += ' ' + person() + e5(' ' + random.choice(adj)) + e5(' ' + random.choice(ort)) + '?'
		else: # getrenntes verb
			v1, v2 = random.choice(verb2).split(",")
			if random.randint(0,1):
				satz = random.choice(['Warum', 'Wieso', 'Weshalb'])
				satz += ' ' + v1
			else:
				satz = v1.capitalize()
			satz += ' ' + person() + ' ' + e5(random.choice(adj) + ' ') + e5(random.choice(ort) + ' ') + v2 + '?'
		if not random.randint(0,10):
			satz += ' ' + random.choice(['Mann weiss es nicht.', 'Denk mal drüber nach!'])
	
	else:
		if random.randint(0,1): # Standardsatz mit getrenntem Verb
			v1, v2 = random.choice(verb2).split(",")
			satz = person() + ' ' + v1
			if random.randint(0,3):
				satz += ' ' + random.choice(adj)
			if random.randint(0,2):
				satz += ' ' + random.choice(ort)
			satz += ' ' + v2
		else: # Standardsatz
			satz = person() + ' ' + random.choice(verb)
			if random.randint(0,3):
				satz += ' ' + random.choice(adj)
			if random.randint(0,2):
				satz += ' ' + random.choice(ort)
		if random.randint(0,5) == 1: # Chance 1/6
			satz += random.choice(ns)
		satz += '.'
	
	satz = ersten_buchstaben_gross(satz)
	return satz

#if random.randint(0,1) #50%
# EOF
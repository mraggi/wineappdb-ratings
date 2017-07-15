#!/bin/python3

import re #regular expressions
import requests
from bs4 import BeautifulSoup
import argparse

def ProcessGameName(game):
	#game = game.lower()
	game = game.replace("&","and")
	game = game.replace(".","")
	game = game.replace(" :",":")
	game = re.sub("\(.*\)","",game)
	game = game.replace("  "," ")
	game = game.replace("\\u2122","")
	game = game.replace("\\u00ae","")
	game = game.replace("\\u00e7","ç")
	game = game.replace("\\u00fc","ü")
	game = game.replace("\\u00e6","ae")
	game = game.replace("\\u2019","'")
	game = game.replace("\\u0027","'")
	game = game.replace("\\u0026","and")
	game = game.replace("\\u2013","-")
	game = game.replace("\\/","/")
	game = game.replace("\\","")
	game = re.sub("^(.*), The","The \\1",game)
	game = game.replace("- Enhanced Edition","")
	game = game.replace("- Expansion Pass","")
	game = game.replace("- Extended Edition","")
	game = game.replace("- Ultimate Edition","")
	game = game.replace("- Complete Edition","")
	game = game.replace(": Enhanced Edition","")
	game = game.replace(": Gold Edition","")
	game = game.replace(": Gold","")
	game = game.replace(": Hero Edition","")
	game = game.replace(": Royal Edition","")
	game = game.replace(": Champion Edition","")
	game = game.replace(": Complete Edition","")
	game = game.replace(": Game of the Century Edition","")
	game = game.replace(": Complete","")
	game = game.replace(": Bundle","")
	game = game.replace(": Master Edition","")
	game = game.replace(": Epic Edition","")
	game = game.replace(": Advanced Edition","")
	game = game.replace(": Fortune's Edition","")
	game = game.replace(": Collector's Edition","")
	game = game.replace(": Soundtrack Edition","")
	game = game.replace(" Limited Edition","")
	game = game.replace(" Enhanced Edition","")
	game = game.replace(" GOTY Edition","")
	game = game.replace(" Game of the Year Edition","")
	game = game.replace(" Special Edition","")
	game = game.replace(" Deluxe Edition","")
	game = game.replace(" Director's Cut Digital Classic Edition","")
	game = game.replace(" Epic Edition","")
	game = game.replace(" The Complete Edition","")
	game = game.replace(" Gold Edition","")
	game = game.replace(" Editor's Choice Edition","")
	game = game.replace(" Masterpiece Edition","")
	game = game.replace(" Premium Edition","")
	game = game.replace(" Imperial Edition","")
	game = game.replace(" Ultimate Edition","")
	game = game.replace(" Reforged Edition","")
	game = game.replace(" Reforged Edition","")
	game = game.replace(" Championship Edition","")
	game = game.strip()
	return game

def ExtractGames(txt):
	bla = txt.split(",\"title\":")
	#print(len(bla))
	Games = []
	first = True
	for x in bla:
		if first:
			first = False
			continue
		x = x.split("\"")
		game = x[1]
		Games.append(ProcessGameName(game))
		#print(ProcessGameName(game))
		
	return Games

def GogExtract():
	gogurl = "https://www.gog.com/games/ajax/filtered?mediaType=game&sort=bestselling&page="
	#getparams = {"sort":"bestselling","page":1,"mediaType":"game"}
	Games = []
	
	for page in range(1,43): #uhh... change 43 for something
		#getparams["page"] = page
		r = requests.get(gogurl+str(page))
		html = r.text
		#print("Page",page," has html:",r.json())
		Games.extend(ExtractGames(html))
	return Games
	

A = GogExtract()
for a in A:
	print(a)

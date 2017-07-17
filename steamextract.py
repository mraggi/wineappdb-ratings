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
	game = game.replace("\\u00b7",".")
	game = game.replace("\\/","/")
	game = game.replace("\\","")
	game = re.sub("^(.*), The","The \\1",game)
	#before = game
	game = game.replace(" Enhanced Edition","")
	game = game.replace(" Expansion Pass","")
	game = game.replace(" Extended Edition","")
	game = game.replace(" Ultimate Edition","")
	game = game.replace(" Director's Cut","")
	game = game.replace(" Complete Edition","")
	game = game.replace(" DLC pack","")
	game = game.replace(" Collector's Edition","")
	game = game.replace(" Digital Deluxe Edition","")
	game = game.replace(" Digital Collector's Edition","")
	game = game.replace(" Immortal Edition","")
	game = game.replace(" Director's Cut","")
	game = game.replace(" Gold Edition","")
	game = game.replace(" Gold","")
	game = game.replace(" Hero Edition","")
	game = game.replace(" Royal Edition","")
	game = game.replace(" Champion Edition","")
	game = game.replace(" Complete Edition","")
	game = game.replace(" Game of the Century Edition","")
	game = game.replace(" Complete","")
	game = game.replace(" Bundle","")
	game = game.replace(" Master Edition","")
	game = game.replace(" Epic Edition","")
	game = game.replace(" Advanced Edition","")
	game = game.replace(" Fortune's Edition","")
	game = game.replace(" Collector's Edition","")
	game = game.replace(" Deluxe Edition","")
	game = game.replace(" Deluxe","")
	game = game.replace(" Complete Chronicles","")
	game = game.replace(" Definitive Edition","")
	game = game.replace(" Black Edition","")
	game = game.replace(" DLC","")
	game = game.replace(" Limited Edition","")
	game = game.replace(" GOTY Edition","")
	game = game.replace(" Game of the Year Edition","")
	game = game.replace(" Special Edition","")
	game = game.replace(" Deluxe Edition","")
	game = game.replace(" Director's Cut Digital Classic Edition","")
	game = game.replace(" The Complete Edition","")
	game = game.replace(" Editor's Choice Edition","")
	game = game.replace(" Masterpiece Edition","")
	game = game.replace(" Premium Edition","")
	game = game.replace(" Imperial Edition","")
	game = game.replace(" Reforged Edition","")
	game = game.replace(" Championship Edition","")
	game = game.replace(" Triple Thrill Pack","")
	game = game.replace(" Collector's Edition","")
	game = game.replace(" 6-pack","")
	game = game.replace(" Collection","")
	game = game.replace(" Definitive Edition","")
	game = game.replace(" Pre-Order","")
	game = game.replace(" Deluxe Ice Cream Edition","")
	game = game.replace(" Legacy Edition","")
	#if (before != game):
		#print(before, " ----: ",game)
	game = game.strip(" -:+'")
	return game

def SteamExtract(filename):
	with open(filename, 'r') as myfile:
		txt = myfile.read()

	#soup = BeautifulSoup(txt,"lxml")

	bla = txt.split("\"name\":")
	#print(len(bla))
	i = 0
	for x in bla:
		if (i >= 2):
			x = x.split("\"")
			game = x[1]
			print(ProcessGameName(game))
		i += 1

parser = argparse.ArgumentParser(description="Extract information from the html file with steam games and print them out to stdout")
parser.add_argument("input", help='The name of the html file')

args = parser.parse_args()
if (args.input):
	SteamExtract(args.input)

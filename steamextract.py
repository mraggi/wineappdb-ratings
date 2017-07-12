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
	game = game.replace("\\/","/")
	game = game.replace("\\","")
	game = game.strip()
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

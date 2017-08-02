#!/bin/python3

import re #regular expressions
import subprocess
import os
import sys

def Canonicalize(s):
	S = s.lower()
	S = S.strip()
	S = S.replace('\'',"")
	S = S.replace('-',"")
	S = S.replace(':',"")
	S = S.replace('+',"")
	S = S.replace('=',"")
	S = S.replace("  "," ")
	S = S.replace("!","")
	S = S.replace("?","")
	return S

Games = {} #empty dictionary


print("Getting gold list... ",)
if (not os.path.isfile("gold.txt")):
	os.system(sys.executable + " winehqextract.py -g > gold.txt")
	print("\tDone!")
else:
	print("\tUsing already found file! If you wish to recover again, rename or delete gold.txt")

with open("gold.txt", 'r') as myfile:
		txt = myfile.read()
		golds = txt.split("\n")
		for game in golds:
			Games[Canonicalize(game)] = "Gold"


print("Getting platinum list... ",)
if (not os.path.isfile("platinum.txt")):
	os.system(sys.executable + " winehqextract.py -p > platinum.txt")
	print("\tDone!")
else:
	print("\tUsing already found file! If you wish to recover again, rename or delete platinum.txt")

with open("platinum.txt", 'r') as myfile:
		txt = myfile.read()
		platinums = txt.split("\n")
		for game in platinums:
			Games[Canonicalize(game)] = "Platinum"


print("Getting list of all gog games... ",)
if (not os.path.isfile("goggames.txt")):
	os.system(sys.executable + " gogextract.py > goggames.txt")
	print("\tDone!")
else:
	print("\tUsing already found file! If you wish to recover again, rename or delete goggames.txt")


with open("goggames.txt", 'r') as myfile:
		txt = myfile.read()
		steams = txt.split("\n")
		print("")
		print("GOG has ",len(steams),"games")
		numwine = 0
		for game in steams:
			if (not game):
				continue
			cg = Canonicalize(game)
			if (cg in Games):
				print("\t",game,"...", Games[cg])
				numwine += 1
		print("\nFinished! You could play", numwine, "games in wine!")

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
	S = S.replace("  "," ")
	S = S.replace("!","")
	S = S.replace("?","")
	return S

print("Getting platinum list... ",)
if (not os.path.isfile("platinum.txt")):
	os.system("python3 winehqextract.py -p > platinum.txt")
	print("\tDone!")
else:
	print("\tUsing already found file! If you wish to recover again, rename or delete platinum.txt")

print("Getting gold list... ",)
if (not os.path.isfile("gold.txt")):
	os.system("python3 winehqextract.py -g > gold.txt")
	print("\tDone!")
else:
	print("\tUsing already found file! If you wish to recover again, rename or delete gold.txt")



print("Getting list of your steam games... ",)
if (not os.path.isfile("steamgames.txt")):
	os.system("python3 steamextract.py MySteamGames.html > steamgames.txt")
	print("\tDone!")
else:
	print("\tUsing already found file! If you wish to recover again, rename or delete steamgames.txt")

Games = {} #empty dictionary

with open("platinum.txt", 'r') as myfile:
		txt = myfile.read()
		platinums = txt.split("\n")
		for game in platinums:
			Games[Canonicalize(game)] = "Platinum"

with open("gold.txt", 'r') as myfile:
		txt = myfile.read()
		golds = txt.split("\n")
		for game in golds:
			Games[Canonicalize(game)] = "Gold"

# Uncomment the following to include silver games!

#print("Getting silver list... ",)
#if (not os.path.isfile("silver.txt")):
	#os.system("python3 winehqextract.py -s > silver.txt")
	#print("\tDone!")
#else:
	#print("\tUsing already found file! If you wish to recover again, rename or delete gold.txt")

#with open("silver.txt", 'r') as myfile:
		#txt = myfile.read()
		#golds = txt.split("\n")
		#for game in golds:
			#Games[Canonicalize(game)] = "Silver"


with open("steamgames.txt", 'r') as myfile:
		txt = myfile.read()
		steams = txt.split("\n")
		print("")
		print("You have",len(steams),"games")
		numwine = 0
		for game in steams:
			if (not game):
				continue
			cg = Canonicalize(game)
			if (cg in Games):
				print("\t",game,"...", Games[cg])
				numwine += 1
		print("\nFinished! You could play", numwine, "games in wine!")

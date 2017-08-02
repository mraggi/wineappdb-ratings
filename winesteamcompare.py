#!/bin/python3

import re #regular expressions
import subprocess
import os
import sys
Games = {} #empty dictionary

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

print("Getting gold list... ",)
if (not os.path.isfile("gold.txt")):
	os.system("python3 winehqextract.py -g > gold.txt")
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
	os.system("python3 winehqextract.py -p > platinum.txt")
	print("\tDone!")
else:
	print("\tUsing already found file! If you wish to recover again, rename or delete platinum.txt")

with open("platinum.txt", 'r') as myfile:
		txt = myfile.read()
		platinums = txt.split("\n")
		for game in platinums:
			Games[Canonicalize(game)] = "Platinum"


print("Getting list of your steam games... ",)
if (not os.path.isfile("steamgames.txt")):
	os.system("python3 steamextract.py MySteamGames.html > steamgames.txt")
	print("\tDone!")
else:
	print("\tUsing already found file! If you wish to recover again, rename or delete steamgames.txt")



# dict of games
mygames = {}

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
				mygames[game] = Games[cg]

# Write a list of games 
with open("results.tsv", 'w') as results:
		for k,v in mygames.items():
			results.write("{0}\t{1}\n".format(k,v))
        
print("\nFinished! You could play", numwine, "games in wine!")
                
		

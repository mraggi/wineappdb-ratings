# Description
A short python script to scrape all games with a given rating from AppDB at winehq.org and compare them to your list of games from steam. You are free to use it however you see fit. However, consider donating to the good guys over at winehq.org for all their great work at https://www.winehq.org/donate

# Usage
First, make sure you have python3 and Beautiful Soup and lxml installed. They probably already come with your python3 installation.

We provide two tools and a third one that uses both to compare results: 
1. `winehqextract.py` downloads and prints games with different ratings.
2. `steamextract.py` extracts game information from steampowered.com
3. `winesteamcompare.py` uses both of the above to generate a list of the games you own on steam that can be played using wine (either gold or platinum rating).

All three tools are easy to modify or extend to suit your needs.

## If you want to know which or your steam games can be played using wine
The first thing you have to do is open your browser and login to http://steampowered.com/ using your username and password. This is because unfortunately I don't (yet) know how to log-in automatically, since steam uses some weird authentication with phones and whatnot. So maybe in the future this step will be skipped, but for now the solution is to download the page yourself.

Log-in to steam through your browser, then go to [Your User Name] -> Games -> All Games. You should see all your games in there. Now save the page with the file name `MySteamGames.html` in the same folder you downloaded the python scripts This file name is important, since it's the file name winesteamcompare expects.



## If you just want to use the wine extractor
Just download winehqextract.py an run the python script with options [-pgsbx] to get a list of Platinum, Gold, Silver, Bronze and Garbage, either with `python3 winehqextract.py -h` or `chmod +x winehqextract.py` and then `./winehqextract.py --help`. 

These commands will print a list of options. The options are straightforward: `-p` or `--platinum` for all platinum games, `-g` or `--gold` for all gold games, etc.

For example, the following command finds all games with a rating of platinum or gold and prints them out.

```
	./winehqextract.py -pg
```

Bear in mind that the command may take a while, since it has to download all pages from the appDB, 

# Future plans
I'm working on scraping your steam games and classify them according to wine ratings.

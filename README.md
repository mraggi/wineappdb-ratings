# Description
A short python script to scrape all games with a given rating from AppDB at winehq.org and compare them to your list of games from steam. You are free to use it however you see fit. However, consider donating to the good guys over at winehq.org for all their great work at https://www.winehq.org/donate

# Usage
First, make sure you have python3 and Beautiful Soup and lxml installed. They probably already come with your python3 installation.

Just download winehqextract.py an run the python script with options [-pgsbx] to get a list of Platinum, Gold, Silver, Bronze and Garbage, either with `python3 winehqextract.py -h` or `chmod +x winehqextract.py` and then `./winehqextract.py --help`. 

These commands will print a list of options. The options are straightforward: `-p` or `--platinum` for all platinum games, `-g` or `--gold` for all gold games, etc.

For example, the following command finds all games with a rating of platinum or gold and prints them out.

```
	./winehqextract.py -pg
```

Bear in mind that the command may take a while, since it has to download all pages from the appDB, 

# Future plans
I'm working on scraping your steam games and classify them according to wine ratings.

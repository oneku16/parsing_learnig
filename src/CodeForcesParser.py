from sys import stdin, stdout
import requests
from bs4 import BeautifulSoup as BS
from art import tprint


def get_id(url: str) -> str:

	req = requests.get(url) 
	source = BS(req.content, "html.parser")
	contests = source.find_all(class_ = "roundbox sidebox")[0].find("a").get("href")
	
	return contests


def get_codeforces(url = get_id("https://codeforces.com/contests")) -> str:
	
	url = "https://codeforces.com" + url
	req = requests.get(url)
	source = BS(req.content, "html.parser")
	codeforces = source.find_all("div", class_ = "datatable")[0].find_next("td").text

	return codeforces

def main(): return(get_codeforces())


if __name__ == "__main__": main()


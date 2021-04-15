import requests as rq
from bs4 import BeautifulSoup

def downloadPage(url, x):
  headers = {'user-agent': 'Italo'};
  r = rq.get(url, headers=headers);
  page = BeautifulSoup(r.text, "html.parser");
  with open("./sites/steam/positivePages/page"+str(x)+".html", "w") as file:
      file.write(str(page));
      
url = "https://store.steampowered.com/app/1455840/Dorfromantik/";

downloadPage(url, 3)
  
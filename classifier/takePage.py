import requests as rq
from bs4 import BeautifulSoup

def downloadPage(url, x):
  headers = {'user-agent': 'Italo'};
  r = rq.get(url, headers=headers);
  page = BeautifulSoup(r.text, "html.parser");
  with open("steam/negativePages/page"+str(x)+".html", "w") as file:
      file.write(str(page));
      
urls = ["https://store.steampowered.com/communityrecommendations/",
"https://store.steampowered.com/curators/",
"https://store.steampowered.com/genre/Early%20Access/",
"https://store.steampowered.com/tags/pt-br/Aventura/",
"https://store.steampowered.com/tags/pt-br/Casual/",
"https://store.steampowered.com/tags/pt-br/A%C3%A7%C3%A3o/",
"https://store.steampowered.com/tags/pt-br/Corrida/",
"https://store.steampowered.com/points/",
"https://store.steampowered.com/news/",
"https://store.steampowered.com/labs/"];
x=1;
for url in urls:
  downloadPage(url, x)
  x+=1;
  
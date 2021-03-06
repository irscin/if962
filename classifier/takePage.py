import requests as rq
from bs4 import BeautifulSoup

def downloadPage(url, x):
  headers = {'user-agent': 'Italo'};
  r = rq.get(url, headers=headers);
  page = BeautifulSoup(r.text, "html.parser");
  with open("epic/positivePages/page"+str(x)+".html", "w") as file:
      file.write(str(page));
      
urls = ["https://www.epicgames.com/store/pt-BR/p/curse-of-the-dead-gods",
"https://www.epicgames.com/store/pt-BR/p/monster-jam-steel-titans-2",
"https://www.epicgames.com/store/pt-BR/p/star-renegades",
"https://www.epicgames.com/store/pt-BR/p/scrapnaut",
"https://www.epicgames.com/store/pt-BR/p/the-dungeon-of-naheulbeuk",
"https://www.epicgames.com/store/pt-BR/p/hitman-3",
"https://www.epicgames.com/store/pt-BR/p/rocket-league",
"https://www.epicgames.com/store/pt-BR/p/grand-theft-auto-v",
"https://www.epicgames.com/store/pt-BR/p/tales-from-the-borderlands",
"https://www.epicgames.com/store/pt-BR/p/anno-2070"];
x=1;
for url in urls:
  downloadPage(url, x)
  x+=1;
  
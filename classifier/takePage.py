import requests as rq
from bs4 import BeautifulSoup

def downloadPage(url, x):
  headers = {'user-agent': 'Italo'};
  r = rq.get(url, headers=headers);
  page = BeautifulSoup(r.text, "html.parser");
  with open("steam/positivePages/page"+str(x)+".html", "w") as file:
      file.write(str(page));
      
urls = ["https://store.steampowered.com/app/367520/Hollow_Knight/",
"https://store.steampowered.com/app/762840/Maquette/","https://store.steampowered.com/app/1361320/The_Room_4_Old_Sins/","https://store.steampowered.com/app/860510/Little_Nightmares_II/","https://store.steampowered.com/app/945360/Among_Us/","https://store.steampowered.com/app/105600/Terraria/","https://store.steampowered.com/app/1215270/Down_the_Rabbit_Hole/","https://store.steampowered.com/app/322500/SUPERHOT/","https://store.steampowered.com/app/262060/Darkest_Dungeon/","https://store.steampowered.com/app/1097150/Fall_Guys_Ultimate_Knockout/"];
x=1;
for url in urls:
  downloadPage(url, x)
  x+=1;
  
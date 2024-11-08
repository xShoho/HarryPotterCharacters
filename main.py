import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

URL = "https://heroes-and-villain.fandom.com/wiki/Category:Harry_Potter_characters"

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

body = soup.find("body", class_= 'mediawiki')
main_content = body.find("div", class_= "category-page__members")

characters = main_content.find_all("a", class_= "category-page__member-link")

all_characters = []

for character in characters:
    all_characters.append({
        "name": ' '.join(character.text.split(" ")[0:-1]),
        "surname": character.text.split(" ")[-1]
    })

for character in all_characters:
    print(f'Name: { character['name'] }\nSurname: { character['surname'] }\n\n')


df = pd.DataFrame.from_dict(all_characters, )

df.to_csv('./HarryPotterCharacters.csv', index= False)
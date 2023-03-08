import unicodedata
import re
import requests
from bs4 import BeautifulSoup
import time
import random
import numpy as np
import pandas as pd

import configparser

config = configparser.ConfigParser()
config.read('config.ini')

scraper = config.get('SCRAPER', 'SITE')

all_hebrewniqqud = []
all_hebrew_no_niqqud = []
all_links = []
all_transliteration = []
all_roots = []
all_part_of_speech = []
all_english = []

for i in range(1, 603):  # MAX=603 ==== 602 pages
    print(f"Scrapping page {i}")
    url = f"{scraper}{i}"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    table_content = soup.find('tbody')

    rows = table_content.find_all('tr')

    hebrewniqqud = []
    hebrew_no_niqqud = []
    link = []
    transliteration = []
    root = []
    part_of_speech = []
    english = []

    # Extract row information
    for r in rows:
        parsed_row = r.find_all('td')
        hebrewniqqud.append(parsed_row[0].find('span', class_='menukad').text)
        link.append('https://www.pealim.com'+r.find('a').get('href'))
        transliteration.append(parsed_row[0].find(
            'span', class_='dict-transcription').text)
        root.append(parsed_row[1].text)
        part_of_speech.append(parsed_row[2].text)
        english.append(parsed_row[3].text)

    # Getting the hebrew without the niqqud
    for hebrew_word in hebrewniqqud:
        base_word = base_word = re.sub(
            '[\u0591-\u05BD\u05BF-\u05C2\u05C4-\u05C7]', '', hebrew_word)
        hebrew_no_niqqud.append(base_word)

    all_hebrewniqqud.extend(hebrewniqqud)
    all_hebrew_no_niqqud.extend(hebrew_no_niqqud)
    all_links.extend(link)
    all_transliteration.extend(transliteration)
    all_roots.extend(root)
    all_part_of_speech.extend(part_of_speech)
    all_english.extend(english)

    time.sleep(random.uniform(1, 5))

data = {
    "Hebrew-Niqqud": all_hebrewniqqud,
    "Hebrew-Base": all_hebrew_no_niqqud,
    "Link": all_links,
    "Transliteration": all_transliteration,
    "Root": all_roots,
    "Part-of-Speech": all_part_of_speech,
    "English": all_english
}

df = pd.DataFrame(data)
df.to_csv("dictionary.csv", index=False)

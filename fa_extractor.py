
# coding: utf-8

import requests
import csv
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
PAGES = 17
user_id = 'FILMAFFINITY_USER_ID'
with open('films.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter.writerow(['Title'] + ['Rating10'])
    for i in range(1, PAGES):
        r = requests.get('https://www.filmaffinity.com/en/userratings.php?user_id={}&p={}'.format(user_id,i),auth=HTTPBasicAuth('filmaffinity_user', 'filmaffinity_pass'))
        soup = BeautifulSoup(r.text, 'html.parser')
        films = []
        ratings = []
        for link in soup.find_all('div'):
            if link.get('class'):
                if link.get('class')[0] == 'mc-title':
                    films.append(link.findChild('a').get('title'))
            if link.get('class'):
                if link.get('class')[0] == 'ur-mr-rat':
                    ratings.append(link.text)
        for i, film in enumerate(films):
            spamwriter.writerow([film] + [ratings[i]])


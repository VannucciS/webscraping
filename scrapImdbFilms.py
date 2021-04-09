import requests
from requests import get
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np

headers = {"Accept-Language": "en-US, en; q=0.5"}

url ="https://www.imdb.com/search/title/?country_of_origin=br&sort=boxoffice_gross_us,desc"
results = requests.get(url, headers=headers)

soup = bs(results.text, 'html.parser')
#print(soup.prettify())

"""

textfile = open('sopa.txt', 'w')
n = text_file.write(soup.prettify())
text_file.close()

"""

# Initialize empty lists where you'll store your data
titles = []
years = []
time = []
imdb_ratings = []
metascores = []
votes = []
us_gross = []

movie_div = soup.find_all('div', class_='lister-item mode-advanced')

#Initiate the for loop

for container in movie_div:
        name = container.h3.a.text
        titles.append(name)
        year = container.h3.find('span', class_='lister-item-year').text
        years.append(year)
        runtime = container.p.find('span', class_='runtime').text if container.p.find('span', class_='runtime').text else '_'
        time.append(runtime)
        ratings = float(container.strong.text)
        imdb_ratings.append(ratings);

movies = pd.DataFrame({
    'movie' : titles,
    'year' : years,
    'runtime': time,
    'Imdb_rating': imdb_ratings})

print(movies)

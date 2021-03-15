from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, \
    WebDriverException

# setting up selenium and starting up chrome driver
driver = webdriver.Chrome(executable_path='C:/Users/talwa/Downloads/chromedriver_win32/chromedriver.exe')
driver.get("https://www.basketball-reference.com/players/a/adamsst01.html")


url = 'https://www.basketball-reference.com/players/a/adamsst01.html'
html = urlopen(url)
soup = BeautifulSoup(html, features='lxml')

rows = soup.findAll('tr', class_="full_table")
items = [[item.getText() for item in rows[i].findAll('td')] for i in range(len(rows))]
#headers = [item for item in soup.findAll('tr', class_="full_table")[1].getText()]

stat_table = {}

for index, item in enumerate(items):
    season = rows[index].findAll('a')[0].getText()
    print(season)
    print(item[1])
    stat_table[index] = {'season': season, 'team': item[1], 'league': item[2], 'position': item[3], 'games': item[4], 'games_started': item[5], 'minutes_played': item[6], 'fgm': item[7], 'fga': item[8], 'fgp': item[9], '3pm': item[10], '3pa': item[11], '3pp': item[12], '2pm': item[13]  }

print(stat_table[0])

        

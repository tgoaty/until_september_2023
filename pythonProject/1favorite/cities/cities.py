import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def get_cities(URL):
    global cities
    URL_TEMPLATE = URL
    response = requests.get(URL_TEMPLATE, headers={'Accept': UserAgent().chrome})
    html = response.content
    bs = BeautifulSoup(html, 'html.parser')
    citie = bs.find_all('td')

    k = 0
    for city in citie:
        if city.text not in cities and city.text.isalpha() and city.text != 'Город' and city.text[0] in 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
            print(city.text, file=fl)
            k += 1
            cities.append(city.text)
    print(URL[30:], len(citie), k)


URL_TEMPLATE = 'https://ru.wikipedia.org/wiki/Список_городов_мира'
response = requests.get(URL_TEMPLATE, headers={'User-Agent': UserAgent().chrome})
print('request=', response.status_code)
html = response.content
bs = BeautifulSoup(html, 'html.parser')
tds = bs.find_all('a', class_='', title=True)

countries = []
k = 1
for td in tds:
    if k > 29 and k < 200:
        countries.append('https://ru.wikipedia.org/wiki/' + td['title'])
    k += 1
print(*countries, sep='\n')
k = 0
cities = []
with open('/home/adwedelf/PycharmProjects/pythonProject/1favorite/cities/cities.txt', 'w') as fl:
    for country in countries:
        k += 1
        print(k, end = ' ')
        get_cities(country)
fl.close()

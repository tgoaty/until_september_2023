import requests  # for getting the html
from bs4 import BeautifulSoup  # for parsing the html
import pandas as pd  # for take the date into csv


url = 'https://memoteka.com/Мемы'  # main page of site
# list of all information types
links = []
names = []
descriptions = []
all_history = []
photos = []
# counter for seeing process
counter_of_meme = 1


def get_soup(daughter_link):  # main function for getting the info from every page
    global counter_of_meme
    soup = BeautifulSoup(requests.get(daughter_link).text, 'html.parser')
    # getting info from soup
    name = soup.find(class_='firstHeading').text
    description = ''
    for text in soup.find('p'):
        description += text.text
    history = None
    if 'История возникновения' in soup.h2.text:
        history = ''
        texts = soup.find_all('p')[2]
        for text in texts:
            history += text.text
    photo = None
    if len(soup.find_all('a', class_='image', href=True)) > 0:
        image = soup.find_all('a', class_='image', href=True)[0]
        photo = 'https://memoteka.com' + image['href']

    # take info to lists
    links.append(daughter_link)
    names.append(name)
    descriptions.append(description)
    all_history.append(history)
    photos.append(photo)

    # where are we locating?
    print(counter_of_meme)
    counter_of_meme += 1


# getting all links from main page
bs = BeautifulSoup(requests.get(url).text, 'html.parser')
all_links = bs.ul.find_all('li')

# make link in right format
count = 0
for link in all_links:
    all_links[count] = 'https://memoteka.com/' + link.text.replace(' ', '_')
    count += 1

# start crawler
all_links.remove('https://memoteka.com/Мемы')  # remove useless link
for link in all_links:
    get_soup(link)

# put info to dataframe (csv)
df = pd.DataFrame({'url': links, 'name': names, 'description': descriptions, 'history': all_history, 'photo': photos})
df.to_csv('memes.csv', index=False)

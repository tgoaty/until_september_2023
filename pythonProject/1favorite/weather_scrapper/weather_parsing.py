# from typing import List
import requests
from bs4 import BeautifulSoup  # html parser
from fake_useragent import UserAgent  # fake data for browser
import pandas as pd  # tables


fl = open('weather.txt', 'w')  # file for log output
# open site, get html and process it in beautiful soup
URL_TEMPLATE = "https://yandex.ru/pogoda/"
response = requests.get(URL_TEMPLATE, headers={'User-Agent': UserAgent().chrome})
print('request=', response.status_code, sep='', file=fl)
html = response.content
bs = BeautifulSoup(html, 'html.parser')

# get all elements which we want
temps = bs.find_all(class_='temp forecast-briefly__temp forecast-briefly__temp_day')
days = bs.find_all(class_='time forecast-briefly__date')
weathers = bs.find_all(class_='forecast-briefly__condition')

# get place name
try:  # block for ignor ban from site
    print(bs.find(class_='title title_level_1 header-title__title').text, file=fl)
    # designation of counters
    count = 0
    rain_days = 0

    # print all elements to log and get three lists of data
    for _ in range(len(temps)):
        print(temps[count].text[-3:], end='° ', file=fl)
        print(days[count].text, end=' ', file=fl)
        print(weathers[count].text, file=fl)
        if 'Дождь' in weathers[count].text or 'Ливни' in weathers[count].text or 'дождь' in weathers[count].text:
            rain_days += 1  # count number of rain days
        count += 1
        # list for cls
        temp_list: list[str] = [i.text[-3:]+'°' for i in temps]
        day_list: list[str] = [i.text for i in days]
        weather_list: list[str] = [i.text for i in weathers]

    # some result of data processing
    weather_list.append('Num of rain days: ' + str(rain_days))
    day_list.append('Num of days: ' + str(len(days)))
    temp_list.append('Average temp: ' + str(sum([int(i[:-1] ) for i in temp_list])/len(temp_list) // 0.1 / 10)+'°')
    print('Num of rain days:', rain_days, file=fl)

    fl.close()
    # save data to csv
    df = pd.DataFrame(dict(Temp=temp_list, Day=day_list, Weather=weather_list))
    df.to_csv('weather.csv', index=False)

except AttributeError:
    print("Browser don't like us")
finally:
    print('Done')
    fl.close()

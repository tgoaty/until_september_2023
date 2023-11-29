from random import shuffle
fl = open('/home/adwedelf/PycharmProjects/pythonProject/1favorite/cities/cities.txt', 'r')
cities = [i[:-1] for i in fl.readlines()]
shuffle(cities)
message = input().lower()

def check_mes(mes):
    mes = mes.lower()
    if mes.title() not in cities:
        print( 'Not in DB')
        return False, mes
    if mes[-1] in '1234567890-=\}{[]"/?ьъёы.,.\\':
        mes = mes[:-1]
    return True, mes




while message != 'q':
    for city in cities:
        city = city.lower()
        flag, message = check_mes(message)
        if flag:
            if city[0] == message[-1]:
                print(city)
                cities.remove(city.title())
                shuffle(cities)
                break
        else:
            break
    message = input().lower()
import requests
from bs4 import BeautifulSoup
import time

ad_link = []
last_link = None
first_search = True

while 1:
    url = 'https://www.kufar.by/l/r~brestskaya-obl/materinskie-platy'
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    ad = soup.find_all(class_='styles_wrapper__5FoK7')
    i = 0
    for get_link_in_ad in ad:
        ad_link.clear()
        ad_link.append(get_link_in_ad.get('href'))
        i += 1
        if i == 1:
            break
    for find_in_link in ad_link:
        find_in_link = find_in_link.split('?rank')
        find_in_link = find_in_link[0]
        print('find - ', find_in_link)
        print('last - ', last_link)
        req_2 = requests.get(find_in_link)
        soup_2 = BeautifulSoup(req_2.text, 'lxml')
        title = soup_2.find_all(class_='styles_brief_wrapper__title__Ksuxa')
        description = soup_2.find_all(attrs={'itemprop': 'description'})
        for find_in_description, find_in_title in zip(description, title):
            if find_in_description.text.find('Socket') != -1:
                if find_in_link != last_link:
                    last_link = find_in_link
                    if first_search is False:
                        print(last_link)
                    continue
            if find_in_title.text.find('Socket') != -1:
                if find_in_link != last_link:
                    last_link = find_in_link
                    if first_search is False:
                        print(last_link)
    first_search = False
    time.sleep(5)





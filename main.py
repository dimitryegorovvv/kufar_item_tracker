import requests
from bs4 import BeautifulSoup
import time

ad_link = []
last_link = [None, None, None, None, None]
first_search = True

# ссылка на категорию с необходимым городом/страной
url = 'https://www.kufar.by/l/telefony-i-planshety?elementType=categories'
# слово, которое необходимо искать в названии товара и описании (маленькими буквами)
text = 'iphone'

while 1:
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    ad = soup.find_all(class_='styles_wrapper__5FoK7')
    i = 0
    ad_link.clear()
    for get_link_in_ad in ad:
        ad_link.append(get_link_in_ad.get('href'))
        i += 1
        if i == 5:
            break
    counter = 0
    for find_in_link in ad_link:
        find_in_link = find_in_link.split('searchId=')[0]
        req_2 = requests.get(find_in_link)
        soup_2 = BeautifulSoup(req_2.text.lower(), 'lxml')
        title = soup_2.find_all(class_='styles_brief_wrapper__title__ksuxa')
        description = soup_2.find_all(attrs={'itemprop': 'description'})

        for find_in_description, find_in_title in zip(description, title):
            if find_in_description.text.find(text) != -1:
                if find_in_link != last_link[0] and find_in_link != last_link[1] and find_in_link != last_link[2] and find_in_link != last_link[3] and find_in_link != last_link[4]:
                    last_link[counter] = find_in_link
                    if first_search is False and last_link[counter].find('rank=') != -1:
                        print('нашлось - ', last_link[counter])
                    continue
            if find_in_title.text.find(text) != -1:
                if find_in_link != last_link[0] and find_in_link != last_link[1] and find_in_link != last_link[2] and find_in_link != last_link[3] and find_in_link != last_link[4]:
                    last_link[counter] = find_in_link
                    if first_search is False and last_link[counter].find('rank=') != -1:
                        print('нашлось - ', last_link[counter])
        counter += 1

    first_search = False
    time.sleep(5)





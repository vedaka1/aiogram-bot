import requests, traceback
from bs4 import BeautifulSoup
from translate import get_translate
from datetime import datetime


url = 'https://readlightnovel.app/the-beginning-after-the-end-535558'

def get_data(url):
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'html.parser')
    novel = soup.find('div', {'class': 'novels-detail-right'})
    info = novel.find_all('a', {'class': 'box'})
    data = []
    for item in info[1::]:
        data.append(f'{item.text} - {item.get("href")}')
    return data

def get_text(url, number):
    try:
        response = requests.get(url=url)
    except:
        print(traceback.format_exc())
    soup = BeautifulSoup(response.text, 'html.parser')
    chapter = soup.find(id="chapterText")
    chapter_text = ''
    file = open(f'translated/{number}.txt', 'w', encoding='UTF-8')
    print('Старт перевода', datetime)
    for item in chapter:
        text_translate = get_translate(item.text)
        chapter_text = (text_translate + '\n')
        file.write(chapter_text)
    file.close()
    print('Перевод завершен', datetime)
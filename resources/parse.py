import requests, os, traceback
from bs4 import BeautifulSoup
from resources.translate import get_translate
from datetime import datetime

url = 'https://readlightnovel.app/the-beginning-after-the-end-535558'

def time(func):
    def wrapper(*args, **kwargs):
        print("Выполняется функция", func.__name__, '\n'
              "Начало", datetime.now())
        func(*args, **kwargs)
        print("Конец", datetime.now())
    return wrapper
    

def get_last_chapters(url):
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'html.parser')
    novel = soup.find('div', {'class': 'novels-detail-right'})
    info = novel.find_all('a', {'class': 'box'})
    data = []
    for item in info[1::]:
        data.append(f'{item.text} - {item.get("href")}')
    return data

    
def get_chapter_text(url, number):
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'html.parser')
    chapter = soup.find(id="chapterText")
    file = open(f'C:/Projects/Python/aiogram-bot/translated/{number}.txt', 'w', encoding='UTF-8')
    print('Старт перевода', datetime.now())
    for item in chapter:
        try:
            text_translate = get_translate(item.text)
            file.write(str(text_translate) + '\n')
        except:
            file.close()
            os.remove(f'C:/Projects/Python/aiogram-bot/translated/{number}.txt')
            print(traceback.format_exc())
    file.close()
    print('Перевод завершен', datetime.now())


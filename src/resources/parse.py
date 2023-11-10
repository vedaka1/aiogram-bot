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
    """Returns the last five chapters of the novel"""
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'html.parser')
    novel = soup.find('div', {'class': 'novels-detail-right'})
    info = novel.find_all('a', {'class': 'box'})
    data = []
    for item in info[1::]:
        data.append(f'{item.text[1:]} - {item.get("href")}')
    return data

    
def get_chapter_text(url, number, lang):
    """Gets the chapter text and translate it into the target language
    """
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'html.parser')
    chapter = soup.find(id="chapterText")
    if not os.path.exists('./translated'):
        os.mkdir('./translated')
    file = open(f'./translated/{number}_{lang}.txt', 'w', encoding='UTF-8')
    if lang == "en":
        for item in chapter:
            try:
                file.write(str(item.text) + '\n')
            except:
                file.close()
                os.remove(f'./translated/{number}_{lang}.txt')
                print(traceback.format_exc())
    else:
        print('Translation start', datetime.now())
        for item in chapter:
            try:
                text_translate = get_translate(item.text, lang)
                file.write(str(text_translate) + '\n')
            except:
                file.close()
                os.remove(f'./translated/{number}.txt')
                print(traceback.format_exc())
        print('End of translation', datetime.now())
    file.close()


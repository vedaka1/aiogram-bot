import os
import traceback
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from resources.translate import get_translate

def get_last_chapters():
    """Returns the last five chapters of the novel"""
    response = requests.get(url='https://readlitenovel.com/the-beginning-after-the-end-535558',
                            timeout=10)
    soup = BeautifulSoup(response.text, 'html.parser')
    novel = soup.find('div', {'class': 'novels-detail-right'})
    info = novel.find_all('a', {'class': 'box'})
    data = []
    for item in info[1::]:
        data.append([item.text[4:], item.get("href")])
    return data

def get_chapter_text(url, number, lang):
    """Gets the chapter text and translate it into the target language"""
    response = requests.get(url=url, timeout=10)
    soup = BeautifulSoup(response.text, 'html.parser')
    chapter = soup.find(id="chapterText")
    if not os.path.exists('./translated'):
        os.mkdir('./translated')
    with open(f'./translated/{number}_{lang}.txt', 'w', encoding='UTF-8') as file:
        if lang == "en":
            for item in chapter:
                try:
                    file.write(str(item.text) + '\n')
                except Exception:
                    file.close()
                    os.remove(f'./translated/{number}_{lang}.txt')
                    print(traceback.format_exc())
        else:
            print('Translation start', datetime.now())
            for item in chapter:
                try:
                    text_translate = get_translate(item.text, lang)
                    file.write(str(text_translate) + '\n')
                except Exception:
                    file.close()
                    os.remove(f'./translated/{number}.txt')
                    print(traceback.format_exc())
            print('End of translation', datetime.now())
        file.close()

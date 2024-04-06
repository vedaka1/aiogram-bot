import os
import traceback

import requests
from bs4 import BeautifulSoup
from httpx import Response

from infrastructure.ioc import init_async_client
from logic.novel.translate import get_translate


async def get_last_chapters() -> list[dict]:
    """Returns the last five chapters of the novel"""
    client = init_async_client()
    data = []
    response: Response = await client.get(
        url="https://readlitenovel.com/the-beginning-after-the-end-535558", timeout=10
    )
    soup = BeautifulSoup(response.text, "html.parser")
    novel = soup.find("div", {"class": "novels-detail-right"})
    info = novel.find_all("a", {"class": "box"})
    for item in info[1::]:
        data.append({"number": int(item.text[4:]), "url": item.get("href")})
    return data


def get_chapter_text(url: str, number: int, lang: str) -> None:
    """Gets the chapter text and translate it into the target language"""
    response = requests.get(url=url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")
    chapter = soup.find(id="chapterText")
    if not os.path.exists("./translated"):
        os.mkdir("./translated")
    with open(f"./translated/{number}_{lang}.txt", "w", encoding="UTF-8") as file:
        if lang == "en":
            for item in chapter:
                try:
                    file.write(str(item.text) + "\n")
                except Exception:
                    file.close()
                    os.remove(f"./translated/{number}_{lang}.txt")
                    print(traceback.format_exc())
        else:
            for item in chapter:
                try:
                    text_translate = get_translate(item.text, lang)
                    file.write(str(text_translate) + "\n")
                except Exception:
                    file.close()
                    os.remove(f"./translated/{number}.txt")
                    print(traceback.format_exc())
        file.close()

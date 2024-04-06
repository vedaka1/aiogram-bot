# aiogram python bot

## Description

It can:

- Parse light novel and send translated chapters
- Chat with you through ChatGPT nad Gemini-Pro
- Generate images (Kadinsky)

## Setup

1. Create a .env file and enter the following variables:
```python
BOT_TOKEN=
API_KEY_CHATGPT=
API_KEY_GEMINI=
API_KEY_KADINSKY=
API_SECRET_KEY_KADINSKY=

DB_HOST=
DB_PORT=
DB_USER=
DB_PASS=
DB_NAME=
```
2. Run <code>docker compose up</code> or  <code>poetry install && poetry run ./src/main.py</code>

## Bot commands

- /start-chat - enable chatGPT mode
- /end-chat - disable chatGPT mode
- /select-model - select AI model
- /last_chapters - bot will send the last chapters of the novel
- /imagine - generate image from prompt e.g. "/imagine cute cat"

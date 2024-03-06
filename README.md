# aiogram python bot

## Description

It can:

- Parse light novel and send translated chapters
- Chat with you through ChatGPT

## Setup

Create a .env file and enter the following variables:
```python
BOT_TOKEN=
API_KEY=
API_KEY_GEMINI=
ROLE=

DB_HOST=
DB_PORT=
DB_USER=
DB_PASS=
DB_NAME=
```

Then run main.py

## Bot commands

- /start-chat - enable chatGPT mode
- /end-chat - disable chatGPT mode
- /select-model - select AI model
- /last_chapters - bot will send the last chapters of the novel

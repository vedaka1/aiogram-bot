# aiogram python bot

## Description

It can:

- Parse light novel and send translated chapters
- Chat with you through ChatGPT

## Setup

Create a config.py file in the resources folder and enter the following variables:

```python
BOT_TOKEN = ""  # telegram bot token
API_KEY = ""    # openAI api key
ROLE = ""       # personality for ChatGPT assistant
```

Then run main.py

## Bot commands

- /start - bot will send the last chapters of the novel
- /start chat - enable chatGPT mode
- /end chat - disable chatGPT mode

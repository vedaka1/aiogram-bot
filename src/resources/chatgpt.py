import openai, logging
from aiogram import md
from resources import config
from resources.database import Database
import g4f, asyncio


logger = logging.getLogger()
g4f.debug.logging = False

_providers = [
            g4f.Provider.Aichat,
            g4f.Provider.ChatBase,
            g4f.Provider.Bing,
            g4f.Provider.GptGo,
            g4f.Provider.You,
            # g4f.Provider.Yqcloud,
            g4f.Provider.GPTalk,
            g4f.Provider.Hashnode,
            g4f.Provider.FreeGpt
        ]

class ChatGPT:
    """ChatGPT class for bot users
    Contains the user's message history
    """
    def __init__(self, user_id: int = 0, model: str = "gpt-3.5-turbo", key=config.API_KEY):
        self.user_id = user_id
        self.model = model
        self.key = key
        self.mode = config.ROLE
        self.db = Database()
        self.messages  = [
            # {"role": "system", "content": f"{self.mode}"}
        ]

        self.client = openai.OpenAI(api_key=self.key)

    def response_completion(self, append=True):
        """Creates a response from ChatGPT"""
        try:
            completion = self.client.chat.completions.create(
                model = self.model,
                messages = self.messages,
                temperature=0.8
            )
            response = completion.choices[0].message.content
            if append:
                self.messages.append({"role": "assistant", "content": response})
            response = md.unparse(response)
            response = response.replace('\`\`\`', '```')
            return response
        
        except Exception as e:
            self.clear_history()
            logger.error(f'User: {self.user_id}, info: {e}')
            return "\U00002757 _Token limit exceeded\, clearing messsages list and restarting_"
    
    def append_message(self, message):
        """Adds the user's message to the message list"""
        print('You:', message)
        self.messages.append({"role": "user", "content": message})

    def clear_history(self):
        self.messages = [
            # {"role": "system", "content": f"{self.mode}"}
        ]

class FreeChatGPT:
    def __init__(self, user_id: int = 0, model: str = "gpt-3.5-turbo", key=config.API_KEY):
        self.user_id = user_id
        self.model = model
        self.key = key
        self.mode = config.ROLE
        self.db = Database()
        self.messages  = [
            {"role": "system", "content": "You will be answer in Russian"}
        ]
        self.messages_length = 30

        self.client = openai.OpenAI(api_key=self.key)

    async def response_completion(self, append=True):
        """Creates a response from g4f ChatGPT"""
        try:
            completion = await g4f.ChatCompletion.create_async(
                    model="gpt-3.5-turbo",
                    messages=self.messages
                )
            if append:
                self.messages.append({"role": "assistant", "content": completion})
            completion = md.unparse(completion)
            completion = completion.replace('\`\`\`', '```')
            return completion
        
        
        except Exception as e:
            self.clear_history()
            logger.error(f'User: {self.user_id}, info: {e}')
            return "\U00002757 _Token limit exceeded\, clearing messsages list and restarting_"

    async def run_provider(self, provider: g4f.Provider.BaseProvider, messages):
        try:
            response = await g4f.ChatCompletion.create_async(
                model=g4f.models.default,
                messages=messages,
                provider=provider,
            )
            print(f"{provider.__name__}:", response)
            return response
        
        except Exception as e:
            print(f"{provider.__name__}:", e)
            
    async def run_all(self):
        calls = [
            self.run_provider(provider, self.messages) for provider in _providers
        ]
        responses = await asyncio.gather(*calls)
        result = [response for response in responses if response != None]
        if result:
            self.messages_length += len(result[0])
            self.messages.append({"role": "assistant", "content": result[0]})
            response = md.unparse(result[0])
            response = response.replace('\`\`\`', '```')
            return response
        else: 
            return "\U00002757 _Не удалось получить ответ_" 

    def append_message(self, message):
        """Adds the user's message to the message list"""
        if self.messages_length > 4000:
            self.clear_history()
        print('You:', message)
        self.messages_length += len(message)
        self.messages.append({"role": "user", "content": message})

    def clear_history(self):
        self.messages_length = 30
        self.messages = [
            {"role": "system", "content": "You will be answer in Russian"}
        ]
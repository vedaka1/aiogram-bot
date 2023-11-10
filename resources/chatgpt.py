import openai
from resources import config
from resources.database import Database

class ChatGPT:
    def __init__(self, model:str="gpt-3.5-turbo", key=config.API_KEY):
        self.key = key
        self.model = model
        self.mode = config.ROLE
        self.db = Database()
        self.messages  = [
            # {"role": "system", "content": f"{self.mode}"}
        ]

        self.client = openai.OpenAI(api_key=self.key)

    def response_completion(self, append=True):
        completion = self.client.chat.completions.create(
            model = self.model,
            messages = self.messages,
            temperature=0.8
        )
        response = completion.choices[0].message.content
        if append:
            self.messages.append({"role": "assistant", "content": response})
        print('Chat:', f"\n{response}\n")
        return response

    
    def append_message(self, message):
        print('You:', message)
        self.messages.append({"role": "user", "content": message})

    def clear_history(self):
        self.messages = [
            # {"role": "system", "content": f"{self.mode}"}
        ]
import openai
from resources import config

class ChatGPT:
    def __init__(self, model:str="gpt-3.5-turbo", key=config.API_KEY):
        self.key = key
        self.model = model
        self.mode = config.ROLE
        self.messages  = [
            {"role": "system", "content": f"{self.mode}"}
        ]
        openai.api_key = self.key

    def response_completion(self, append=True):
        completion = openai.ChatCompletion.create(
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
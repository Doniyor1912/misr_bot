import os

from dotenv import load_dotenv


class Config:
    def __init__(self):
        load_dotenv()
        self.getenvbot()
        self.get_channel_id()



    def get_channel_id(self):
        self.channel_id = os.getenv("CHAT_ID","")

    def getenvbot(self):
        self.token = os.getenv('TOKEN',"defaultbottoken")
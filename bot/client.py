from binance import Client
from config import API_KEY, API_SECRET, BASE_URL
from bot.logger import logger

class BasicBot:
    def __init__(self, api_key=None, api_secret=None, testnet=True):
        self.client = Client(API_KEY, API_SECRET)
        if testnet:
            self.client.FUTURES_URL = BASE_URL
        logger.info("Binance Futures Testnet client initialized")

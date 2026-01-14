from binance import Client
from config import API_KEY, API_SECRET

client = Client(API_KEY, API_SECRET, testnet=True)

def get_market_price(self,symbol):
    ticker = client.futures_symbol_ticker(symbol=symbol)
    return float(ticker["price"])

def get_all_balances(self):
    print("\n=== Futures Account Balance ===")

    balances = client.futures_account_balance()

    has_balance = False
    for asset in balances:
        balance = float(asset["balance"])
        if balance > 0:
            has_balance = True
            print(f"{asset['asset']}  →  {balance}")

    if not has_balance:
        print("No balance available")
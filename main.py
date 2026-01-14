from bot.client import BasicBot
from bot.orders import (
    place_market_order,
    place_limit_order,
    place_stop_limit_order
)
from bot.utils import get_all_balances, get_market_price
from cli import get_user_input

def main():
    bot = BasicBot()

    while True:
        print("\n====== BINANCE FUTURES TESTNET BOT ======")
        print("1. Place Order")
        print("2. Check Market Price")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Select an option (1-4): ").strip()

        try:
            if choice == "1":
                symbol, side, otype, qty, price, stop_price = get_user_input()

                if otype == "MARKET":
                    place_market_order(
                        bot.client, symbol, side, qty
                    )

                elif otype == "LIMIT":
                    place_limit_order(
                        bot.client, symbol, side, qty, price
                    )

                elif otype == "STOP_LIMIT":
                    place_stop_limit_order(
                        bot.client, symbol, side, qty, price, stop_price
                    )

                print("\nOrder Executed Successfully")

            elif choice == "2":
                symbol = input("Enter symbol (e.g. BTCUSDT): ").upper()
                price = get_market_price(bot.client, symbol)
                print(f"\nCurrent Market Price of {symbol}: {price}")

            elif choice == "3":
                print("\nFutures Account Balances")
                balances = get_all_balances(bot.client)

                for asset in balances:
                    if float(asset["balance"]) > 0:
                        print(
                            f"{asset['asset']} | "
                            f"Balance: {asset['balance']} | "
                            f"Available: {asset['withdrawAvailable']}"
                        )

            elif choice == "4":
                print("Exiting bot. Goodbye!")
                break

            else:
                print("Invalid option. Please choose 1–4.")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
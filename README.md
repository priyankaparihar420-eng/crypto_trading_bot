Crypto Trading Bot (Binance Futures Testnet)

This project is a simplified Crypto Trading Bot built using Python that interacts with the Binance USDT-M Futures Testnet.
It allows users to place trades, check market prices, and view account balances through a clean and interactive command-line interface.
The main goal of this project is to demonstrate how a real-world trading bot works at a basic level while following safe practices such as using testnet, environment variables, logging, and modular code structure.

#Applications

1. Useful for learning how crypto trading bots interact with exchanges
2. Can be used as a base project for automated trading strategies
3. Helps understand Futures trading APIs and order execution flow.

#Getting Started

These instructions will help you set up and run the trading bot on your local system for development and testing purposes.
Follow the steps below carefully to get the project running.

#Pre-requisites

What are the things which are to be installed in your system?

This project is built using Python 3.9.6

Libraries to be installed?

pip install python-binance
pip install python-dotenv

You also need:

A Binance Futures Testnet account
API Key and Secret generated from the testnet dashboard

#Deployment

Now you are good to go :)

1. Clone or download the project repository.
2. Extract the project into your preferred directory.
3. Create a virtual environment (recommended).
4. Create a .env file and add your API credentials.
5. Make sure the bot is pointing to the Binance Futures Testnet URL.
6. Run the main script.

#Execution

1. Run the application using:

python main.py

2. You will see a menu with the following options:

Place Order
Check Market Price
Check Balance
Exit

3. Follow the on-screen prompts to place trades or view information.

4. All trading activity is logged internally for debugging and tracking.

#How does it Work?

1. The bot initializes a Binance Futures client using testnet credentials.
2. User input is taken through a command-line interface and validated.
3. Orders are placed using the Binance Futures REST API.
4. Since Futures APIs may return limited responses, the bot explicitly fetches order details after placing an order.
5. Market prices and balances are fetched on demand using utility functions.
6. All API requests, responses, and errors are logged into a log file for safety and traceability.
7. The entire codebase is modular, making it easy to extend or modify.

#Built with

Python 3.x – Programming Language
Binance Futures Testnet API
python-binance library

#Contributing

This project is open to improvements and enhancements.
Feel free to fork the repository and experiment with additional features.

#Author

~ Priyanka Parihar
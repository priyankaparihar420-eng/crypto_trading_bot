from bot.logger import logger
from binance.exceptions import BinanceAPIException

def place_market_order(client, symbol, side, quantity):
    try:
        logger.info(
            f"Placing MARKET order | side={side} | symbol={symbol} | qty={quantity}"
        )

        order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="MARKET",
        quantity=quantity
        )
        
        logger.info(f"MARKET order placed successfully | "
            f"orderId={order.get('orderId')} | status={order.get('status')}")
        return order
    except BinanceAPIException as e:
        logger.error(f"MARKET order failed | symbol={symbol} | error={e.message}")
        raise

def place_limit_order(client, symbol, side, quantity, price):
    try:
        logger.info(
            f"Placing LIMIT order | side={side} | symbol={symbol} | "
            f"qty={quantity} | price={price}"
        )

        order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="LIMIT",
        quantity=quantity,
        price=price,
        timeInForce="GTC"
        )

        logger.info(f"LIMIT order placed successfully | "
            f"orderId={order.get('orderId')} | status={order.get('status')}")
        return order
    except BinanceAPIException as e:
        logger.error(f"LIMIT order failed | symbol={symbol} | error={e.message}")
        raise

def place_stop_limit_order(client, symbol, side, quantity, price, stop_price):
    try:
        logger.info(f"Placing STOP-LIMIT order | side={side} | symbol={symbol} | "
            f"qty={quantity} | stop_price={stop_price} | limit_price={price}")

        order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="STOP",
        quantity=quantity,
        price=price,
        stopPrice=stop_price,
        timeInForce="GTC"
        )

        logger.info(f"STOP-LIMIT order placed successfully | "
            f"orderId={order.get('orderId')} | status={order.get('status')}")
        return order
    except BinanceAPIException as e:
        logger.error(f"STOP-LIMIT order failed | symbol={symbol} | error={e.message}")
        raise



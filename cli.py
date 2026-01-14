def get_user_input():
    symbol = input("Symbol (BTCUSDT): ").upper()
    side = input("Side (BUY/SELL): ").upper()
    order_type = input("Order Type (MARKET / LIMIT / STOP_LIMIT): ").upper()
    quantity = float(input("Quantity: "))

    if side not in ["BUY", "SELL"]:
        raise ValueError("Invalid order side")

    if order_type not in ["MARKET", "LIMIT", "STOP_LIMIT"]:
        raise ValueError("Invalid order type")

    price = None
    stop_price = None

    if order_type == "LIMIT":
        price = float(input("Limit Price: "))

    if order_type == "STOP_LIMIT":
        stop_price = float(input("Stop Price: "))
        price = float(input("Limit Price: "))    

    return symbol, side, order_type, quantity, price, stop_price

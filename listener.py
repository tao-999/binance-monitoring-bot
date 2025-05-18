import websocket
import time
import threading
import datetime
import os
import json
from config import SYMBOLS

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def prepend_log_max_100_lines(symbol, new_entry):
    filename = os.path.join(LOG_DIR, f"{symbol.lower()}_log.txt")
    new_lines = new_entry.splitlines(keepends=True)
    num_new = len(new_lines)
    old_lines = []
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            old_lines = f.readlines()
    allowed_old = max(0, 100 - num_new)
    trimmed_old = old_lines[:allowed_old]
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(new_lines + trimmed_old)

def format_symbol_for_binance(symbol):
    return symbol.upper().replace("USDT", "-USDT")

def on_close(ws, close_status_code, close_msg):
    print("[🔌 连接关闭]")

def make_on_error(exchange):
    def on_error(ws, error):
        print(f"[❌ 错误 - {exchange}]：{error}")
    return on_error

def output_trade_message(exchange, symbol, price, quantity, amount, direction, ts, message):
    print(f"\n🔥 {exchange} | {symbol.upper()} @ {ts}")
    print("[💥大单来了！]")
    print(f"方向：{direction}")
    print(f"数量：{quantity:.4f}")
    print(f"价格：{price}")
    print(f"成交金额：{amount:,.2f} USDT")
    print(f"骚话：{message}")
    print("-" * 50)

    log_entry = (
        f"💥 交易所：{exchange}\n"
        f"💥 交易对：{symbol.upper()}\n"
        f"🕒 时间：{ts}\n"
        f"📉 方向：{direction}\n"
        f"📦 数量：{quantity:.4f}\n"
        f"💰 单价：{price} USDT\n"
        f"💸 成交金额：{amount:,.2f} USDT\n"
        + "-" * 50 + "\n"
    )
    prepend_log_max_100_lines(symbol, log_entry)

def listen_to_symbol_binance(symbol):
    def on_message(ws, message):
        data = json.loads(message)
        price = float(data['p'])
        quantity = float(data['q'])
        is_buyer_maker = data['m']
        amount = price * quantity
        threshold = SYMBOLS.get(symbol, 50000)
        if amount >= threshold:
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            direction = "🟩 多单（主动买入）" if not is_buyer_maker else "🟥 空单（主动卖出）"
            output_trade_message("BINANCE", symbol, price, quantity, amount, direction, now, "币安也顶不住了，哥你还在观望？")

    url = f"wss://fstream.binance.com/ws/{symbol}@aggTrade"
    ws = websocket.WebSocketApp(
        url,
        on_message=on_message,
        on_error=make_on_error("BINANCE"),
        on_close=on_close)
    ws.run_forever()

if __name__ == "__main__":
    threads = []
    for symbol in SYMBOLS.keys():
        t1 = threading.Thread(target=listen_to_symbol_binance, args=(symbol,))
        t1.start(); threads.append(t1)
    for thread in threads:
        thread.join()

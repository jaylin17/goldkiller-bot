from flask import Flask
import yfinance as yf, time, threading, datetime, os

app = Flask(__name__)

print("✅ GoldKiller V4 Mobile LIVE - GOLD# Only")
print("Licence: XMGK-V4-CAPETOWN-2026 - XM Account: 1301968399")

def bot_loop():
    while True:
        try:
            gold = yf.download("GC=F", period="1d", interval="5m", progress=False)
            if len(gold) == 0:
                time.sleep(60)
                continue
            close = float(gold['Close'].iloc[-1])
            ma20 = float(gold['Close'].rolling(20).mean().iloc[-1])
            now = datetime.datetime.now().strftime("%H:%M:%S")
            if close > ma20:
                print(f"{now} 🟢 BUY GOLD# @ {close:.2f} SL 400 TP 500 | Account 1301968399")
            else:
                print(f"{now} 🔴 SELL GOLD# @ {close:.2f} SL 400 TP 500 | Account 1301968399")
            time.sleep(300)
        except Exception as e:
            print("Error:", e)
            time.sleep(60)

threading.Thread(target=bot_loop, daemon=True).start()

@app.route('/')
def home():
    return "GoldKiller V4 Running - GOLD# Only - Account 1301968399"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

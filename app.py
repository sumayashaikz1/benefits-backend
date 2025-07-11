from flask import Flask, jsonify
import yfinance as yf

app = Flask(__name__)

SYMBOLS = {
    "NIFTY": "^NSEI",
    "BANKNIFTY": "^NSEBANK",
    "RELIANCE": "RELIANCE.NS",
    "INFY": "INFY.NS",
    "TCS": "TCS.NS",
    "HDFCBANK": "HDFCBANK.NS"
}

@app.route("/predictions")
def get_predictions():
    output = []
    for name, symbol in SYMBOLS.items():
        try:
            ticker = yf.Ticker(symbol)
            hist = ticker.history(period="1d", interval="5m")
            close = hist["Close"]

            sl = round(close.min(), 2)
            target = round(close.max(), 2)

            prediction = {
                "symbol": name,
                "type": "PUT" if close[-1] < close.mean() else "CALL",
                "confidence": "75%",
                "sl": str(sl),
                "target": str(target),
                "analysis": "Auto-generated prediction"
            }
            output.append(prediction)
        except Exception as e:
            output.append({"symbol": name, "error": str(e)})
    return jsonify(output)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

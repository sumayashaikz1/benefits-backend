from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/predictions', methods=['GET'])
def get_predictions():
    predictions = [
        {
            "symbol": "NIFTY 50",
            "type": "CALL",
            "confidence": "85%",
            "sl": "22800",
            "target": "23200",
            "analysis": "Bullish trend based on volume and RSI."
        },
        {
            "symbol": "BANKNIFTY",
            "type": "PUT",
            "confidence": "75%",
            "sl": "48000",
            "target": "47000",
            "analysis": "Resistance at higher levels, possible pullback."
        },
        {
            "symbol": "RELIANCE",
            "type": "CALL",
            "confidence": "80%",
            "sl": "2850",
            "target": "3000",
            "analysis": "Strong buying interest seen in options data."
        },
        {
            "symbol": "INFY",
            "type": "PUT",
            "confidence": "70%",
            "sl": "1500",
            "target": "1420",
            "analysis": "Weak technical structure."
        }
    ]
    return jsonify(predictions)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

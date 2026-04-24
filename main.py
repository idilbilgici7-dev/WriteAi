import os
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Tüm istekleri kabul eder

@app.route('/')
def home():
    return "WriteAi API is Running!"

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.json
    return jsonify({
        "status": "success",
        "data": {
            "grammar_and_suggestions": {"corrected_text": "Test başarılı!"},
            "sentiment_analysis": {"scores": {"Pozitif": 100}}
        }
    })

if __name__ == "__main__":
    # Render portu otomatik atar, bu yüzden environ.get kullanmak önemlidir
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

import os
from flask import Flask, request, jsonify
from flask_cors import CORS  # 1. Burayı ekle

app = Flask(__name__)
CORS(app)  # 2. Bu satır tüm bağlantı hatalarını çözer!

@app.route('/')
def home():
    return "WriteAi API is Running!"

@app.route('/api/analyze', methods=['POST'])
def analyze():
    try:
        data = request.json
        # Örnek bir yanıt (Sen burayı kendi mantığınla doldurabilirsin)
        response_data = {
            "status": "success",
            "data": {
                "grammar_and_suggestions": {
                    "corrected_text": "API Bağlantısı Başarılı! Metniniz işlendi."
                },
                "sentiment_analysis": {
                    "scores": {"Pozitif": 85, "Nötr": 10, "Negatif": 5}
                }
            }
        }
        return jsonify(response_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

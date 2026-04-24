import os
from flask import Flask, request, jsonify
from flask_cors import CORS  # <-- Bu satır mutlaka olmalı

app = Flask(__name__)
CORS(app) # <-- Tüm sitelerden gelen isteklere izin verir

@app.route('/')
def home():
    return "WriteAi API is Running!"

@app.route('/api/analyze', methods=['POST'])
def analyze():
    try:
        data = request.json
        # ÖNEMLİ: Burada analiz işlemlerini yapmalısın. 
        # Şimdilik çalıştığını görmek için örnek bir yanıt döndürelim:
        response_data = {
            "status": "success",
            "data": {
                "grammar_and_suggestions": {
                    "corrected_text": "API Bağlantısı Başarılı! Gönderdiğin metin: " + data.get('text', '')
                },
                "sentiment_analysis": {
                    "scores": {"Mutluluk": 70, "Nötr": 20, "Üzüntü": 10}
                }
            }
        }
        return jsonify(response_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

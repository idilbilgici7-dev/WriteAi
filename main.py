from flask import Flask, request, jsonify
from flask_cors import CORS # 1. CORS'u içeri aktar

app = Flask(__name__)
# 2. Tüm kaynaklara (veya kendi GitHub linkine) izin ver
CORS(app, resources={r"/api/*": {"origins": "*"}}) 

@app.route('/api/analyze', methods=['POST'])
def analyze():
    try:
        data = request.json
        # Gelen veriyi kontrol et (Hata ayıklama için print ekle)
        print("Gelen Veri:", data)
        
        # İşlemlerini burada yap...
        
        response_data = {
            "status": "success",
            "data": {
                "grammar_and_suggestions": {
                    "corrected_text": "Düzenlenmiş metin buraya gelecek."
                },
                "sentiment_analysis": {
                    "scores": {"Mutluluk": 80, "Hüzün": 10, "Heyecan": 10}
                }
            }
        }
        return jsonify(response_data)
    except Exception as e:
        print(f"Hata oluştu: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()

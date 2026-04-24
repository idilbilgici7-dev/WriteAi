from fastapi import FastAPI
from pydantic import BaseModel
from engine import ContentEngine

# API Uygulamasını başlat
app = FastAPI(title="WriteAI Gelişmiş Analiz API", version="1.0")

# Motoru şimdilik Premium özellikleri açık şekilde başlatıyoruz
engine = ContentEngine(is_premium=True)

# Ön yüzden (Kullanıcının ekranından) gelecek verilerin şablonu
class AnalyzeRequest(BaseModel):
    text: str
    age_group: str        
    learning_level: str   
    use_case: str         

@app.post("/api/analyze")
def analyze_content(request: AnalyzeRequest):
    """
    Kullanıcıdan gelen metni ve profili alır, engine.py'a gönderir ve raporu geri döner.
    """
    user_context = {
        "age_group": request.age_group,
        "learning_level": request.learning_level,
        "use_case": request.use_case
    }
    
    # Motoru çalıştır ve raporu al
    report = engine.full_analysis_report(request.text, user_context)
    
    # Sonucu ön yüze (Frontend) başarılı bir şekilde gönder
    return {
        "status": "success", 
        "data": report
    }

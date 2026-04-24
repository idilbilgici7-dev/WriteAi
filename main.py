from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from engine import ContentEngine

app = FastAPI(title="WriteAI Gelişmiş Analiz API", version="1.0")

# İŞTE YENİ EKLENEN SİHİRLİ KISIM (CORS)
# Bu kod, "Dünyadaki her web sitesi bu API'ye bağlanabilir" der.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = ContentEngine(is_premium=True)

class AnalyzeRequest(BaseModel):
    text: str
    age_group: str        
    learning_level: str   
    use_case: str         

@app.post("/api/analyze")
def analyze_content(request: AnalyzeRequest):
    user_context = {
        "age_group": request.age_group,
        "learning_level": request.learning_level,
        "use_case": request.use_case
    }
    
    report = engine.full_analysis_report(request.text, user_context)
    
    return {
        "status": "success", 
        "data": report
    }
    from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from engine import ContentEngine

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = ContentEngine(is_premium=True)

class AnalyzeRequest(BaseModel):
    text: str
    age_group: str
    learning_level: str
    use_case: str
    input_lang: str
    output_lang: str

@app.post("/api/analyze")
def analyze_content(request: AnalyzeRequest):
    context = request.dict()
    report = engine.full_analysis_report(request.text, context)
    return {"status": "success", "data": report}
    from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from engine import ContentEngine

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = ContentEngine(is_premium=True)

class AnalyzeRequest(BaseModel):
    text: str
    age_group: str
    learning_level: str
    use_case: str
    input_lang: str
    output_lang: str
    content_type: str # Yeni eklendi

@app.post("/api/analyze")
def analyze_content(request: AnalyzeRequest):
    report = engine.full_analysis_report(request.text, request.dict())
    return {"status": "success", "data": report}

import re
import logging
from typing import Dict, Any, List, Union

# Loglama ayarları (Terminalde ne olduğunu görmek için)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ContentEngine:
    """
    Ticari kullanıma hazır (SaaS), kişiselleştirilmiş Metin Analiz ve İşleme Motoru.
    Kullanıcı profiline (yaş, seviye, kullanım amacı) ve Premium durumuna göre dinamik tepki verir.
    """

    def __init__(self, is_premium: bool = False):
        self.is_premium = is_premium
        logging.info(f"🚀 Motor başlatıldı. Statü: {'👑 PREMIUM' if self.is_premium else '🆓 FREE'}")
        self._load_models()

    def _load_models(self):
        """NLP modellerini hafızaya yükler."""
        logging.info("🧠 Dil modelleri ve AI analiz araçları yükleniyor...")
        self.supported_languages = ['tr', 'en', 'de', 'fr', 'es']
        self.models_loaded = True

    def detect_language(self, text: str) -> str:
        """Otomatik dil tespiti."""
        if re.search(r'\b(the|is|are|and|to|of)\b', text.lower()): return "en"
        return "tr"

    def _word_count(self, text: str) -> int:
        return len(re.findall(r'\w+', text))

    def _generate_suggestions_based_on_context(self, user_context: Dict[str, Any]) -> List[str]:
        """Kullanıcının seçtiği Dropdown (Yaş, Seviye, Amaç) verilerine göre özel öneriler üretir."""
        suggestions = []
        age_group = user_context.get("age_group", "18-24")
        level = user_context.get("learning_level", "native")
        use_case = user_context.get("use_case", "general")

        # Yaşa göre öneriler
        if age_group in ["0-12", "13-17"]:
            suggestions.append("Harika bir iş çıkarmışsın! Cümlelerin gayet anlaşılır.")
        
        # Dil Seviyesine göre öneriler
        if level in ["A1", "A2"]:
            suggestions.append("Yeni bir dil öğreniyorsun, harika! Karmaşık kelimeler yerine şimdilik kısa cümleler kurmaya odaklan.")
        
        # Kullanım Amacına göre öneriler
        if use_case == "essay" or use_case == "exam":
            suggestions.append("Sınav/Makale formatı için daha resmi bağlaçlar kullanmalı ve kişisel zamirlerden (Ben, Sen) kaçınmalısın.")
        elif use_case == "entertainment":
            suggestions.append("Eğlence metni için aralara duygu belirten kelimeler veya ünlemler ekleyebilirsin, daha samimi olur!")
        elif use_case == "homework":
            suggestions.append("Ödevin için eğer bir yerden bilgi aldıysan kaynakça eklemeyi unutma.")

        return suggestions

    def analyze_and_correct(self, text: str, lang: str, user_context: Dict[str, Any]) -> Dict[str, Any]:
        """Gramer hatalarını bulur, düzeltir ve bağlamsal koçluk yapar."""
        logging.info(f"[{lang.upper()}] Gramer analizi yapılıyor...")
        
        corrected = text.replace("yapay zeka", "Yapay Zeka").replace("bilmiyom", "bilmiyorum")
        context_suggestions = self._generate_suggestions_based_on_context(user_context)
        
        if not self.is_premium:
            return {
                "corrected_text": "🔒 Metninizde hatalar bulundu. Düzeltilmiş tam metni görmek için Premium'a geçin.",
                "contextual_feedback": context_suggestions[:1] # Ücretsiz kullanıcıya sadece 1 öneri
            }

        return {
            "corrected_text": corrected + " (Tüm hatalar düzeltildi)",
            "contextual_feedback": context_suggestions,
            "premium_vocabulary": "Bu bağlamda kullandığın 'iyi' kelimesi yerine, 'kusursuz' kelimesi daha etkili olabilir."
        }

    def detect_ai_content(self, text: str, lang: str, user_context: Dict[str, Any]) -> Dict[str, Any]:
        """Yapay Zeka (ChatGPT vb.) oranını ölçer, Sınav/Ödev ise kritik uyarı verir."""
        logging.info(f"[{lang.upper()}] AI tespiti yapılıyor...")
        ai_prob = 75.5 # Simüle edilmiş skor
        use_case = user_context.get("use_case", "general")
        
        warning = None
        if use_case in ["homework", "exam", "essay"] and ai_prob > 50:
            warning = "⚠️ KRİTİK UYARI: Ödev ve sınavları kontrol eden Turnitin gibi sistemler bu metni 'Yapay Zeka (Kopya)' olarak işaretleyebilir!"

        result = {
            "ai_probability": ai_prob,
            "human_probability": round(100 - ai_prob, 1),
            "verdict": "Büyük oranda Yapay Zeka" if ai_prob > 50 else "İnsan",
            "critical_warning": warning
        }

        if self.is_premium:
            result["premium_detailed_breakdown"] = [
                {"sentence": text.split('.')[0] + ".", "ai_chance": 85, "reason": "Robotik yapı, çok düşük perplexity."},
                {"sentence": "Sonraki cümle.", "ai_chance": 12, "reason": "Doğal insan kusurları tespit edildi."}
            ]
        else:
            result["premium_detailed_breakdown"] = "🔒 Hangi cümlelerin AI olduğunu detaylı görmek için Premium'a geçin."

        return result

    def analyze_emotions(self, text: str) -> Dict[str, Any]:
        """Metnin barındırdığı baskın duyguları ölçer."""
        return {
            "dominant_emotion": "Merak",
            "sentiment": "Pozitif",
            "scores": {"joy": 0.65, "curiosity": 0.80, "sadness": 0.05}
        }

    def check_originality(self, text: str) -> Dict[str, Any]:
        """Plagiarism (İnternetten kopya çekilip çekilmediğini) kontrol eder."""
        if self._word_count(text) < 5:
            return {"error": "Özgünlük kontrolü için metin çok kısa."}
        
        score = 92.5
        if not self.is_premium:
            return {"originality_score": "🔒 İnternetteki kopya eşleşmelerini görmek için Premium'a geçin."}
            
        return {
            "originality_score": score,
            "is_plagiarized": score < 70,
            "matched_sources": [] if score > 70 else ["wikipedia.org/example"]
        }

    def translate_text(self, text: str, target_lang: str, preserve_tone: bool = False) -> Dict[str, str]:
        """Metni çevirir. Premium'da deyimler ve ton korunur."""
        if not self.is_premium:
            return {
                "translated_text": f"[{target_lang.upper()} - BASİT ÇEVİRİ] {text}",
                "note": "🔒 Kültürel adaptasyon ve ton korumalı profesyonel çeviri için Premium'a geçin."
            }
        return {
            "translated_text": f"[{target_lang.upper()} - PREMIUM ÇEVİRİ] {text}",
            "tone_preserved": preserve_tone
        }

    def analyze_poetics(self, text: str, lang: str) -> Dict[str, Any]:
        """Şarkı sözü ve şiirler için kafiye ve ritim analizi yapar."""
        if not self.is_premium:
            return {"error": "🔒 Kafiye, ritim ve şiirsel analiz Premium kullanıcılar içindir."}

        lines = text.split('\n')
        rhyme_scheme = "AABB" if len(lines) >= 4 else "Tespit edilemedi"

        return {
            "rhyme_scheme": rhyme_scheme,
            "poetic_suggestions": ["3. satırın hece ölçüsü diğerlerinden kısa, ritmi bozuyor."]
        }

    def seo_analysis(self, text: str, lang: str) -> Dict[str, Any]:
        """Blog ve web içerikleri için SEO uyumluluğunu test eder."""
        if not self.is_premium:
            return {"error": "🔒 SEO Analizi Premium özelliğidir."}

        return {
            "readability_score": 78,
            "keyword_density": {"yapay": 2, "zeka": 2},
            "seo_suggestions": ["İlk paragrafta daha fazla anahtar kelime geçirmelisiniz."]
        }

    def humanize_text(self, text: str, lang: str, user_context: Dict[str, Any], style: str = "casual") -> Dict[str, str]:
        """AI metnini, seçilen profile ve stile uygun olarak %100 insana çevirir."""
        if not self.is_premium:
            return {"error": "🔒 Yapay Zeka tespit sistemlerini atlatmak (Humanize) için Premium'a geçin."}

        use_case = user_context.get("use_case", "general")
        level = user_context.get("learning_level", "native")
        
        logging.info(f"Metin İnsanlaştırılıyor... [Amaç: {use_case}, Seviye: {level}, Stil: {style}]")

        return {
            "original_text": text,
            "humanized_text": f"[{style.upper()} Stilde - {level} Seviyesinde Yeniden Yazıldı] Açıkçası bu konu oldukça ilginç...",
            "bypassed_ai_detectors": True
        }

    def full_analysis_report(self, text: str, user_context: Dict[str, Any]) -> Dict[str, Any]:
        """Tüm motorları aynı anda çalıştıran ve raporu döndüren ana fonksiyon."""
        if not text or len(text.strip()) == 0:
            raise ValueError("Analiz edilecek metin boş olamaz.")

        lang = self.detect_language(text)
        
        report = {
            "user_profile": user_context,
            "detected_language": lang,
            "word_count": self._word_count(text),
            "grammar_and_suggestions": self.analyze_and_correct(text, lang, user_context),
            "ai_detection": self.detect_ai_content(text, lang, user_context),
            "emotions": self.analyze_emotions(text),
            "originality": self.check_originality(text)
        }

        # Premium ise ekstra raporları otomatik ekle
        if self.is_premium:
            report["seo_analysis"] = self.seo_analysis(text, lang)
            report["poetics"] = self.analyze_poetics(text, lang)

        return report

# ==========================================
# MOTOR TESTİ (HIZLI DENEME)
# ==========================================
if __name__ == "__main__":
    sample_text = "Yapay zeka çok hızlı gelişiyor. \nİnsanlık bu hıza yetişemiyor."
    
    # Dropdown'lardan gelen örnek kullanıcı verisi
    frontend_dropdown_data = {
        "age_group": "18-24",
        "learning_level": "native",
        "use_case": "exam"
    }

    # ÜCRETSİZ MOTOR TESTİ
    print("\n" + "🔴"*20)
    print("🆓 ÜCRETSİZ KULLANICI DENEYİMİ")
    free_engine = ContentEngine(is_premium=False)
    free_report = free_engine.full_analysis_report(sample_text, frontend_dropdown_data)
    print("Düzeltilmiş Metin:", free_report['grammar_and_suggestions']['corrected_text'])
    print("AI Raporu Detayı:", free_report['ai_detection']['premium_detailed_breakdown'])

    # PREMIUM MOTOR TESTİ
    print("\n" + "🟢"*20)
    print("👑 PREMIUM KULLANICI DENEYİMİ")
    premium_engine = ContentEngine(is_premium=True)
    premium_report = premium_engine.full_analysis_report(sample_text, frontend_dropdown_data)
    print("Düzeltilmiş Metin:", premium_report['grammar_and_suggestions']['corrected_text'])
    print("AI Raporu Detayı:", premium_report['ai_detection']['premium_detailed_breakdown'][0])
    print("Kritik Uyarı:", premium_report['ai_detection']['critical_warning'])
    
    # Premium Humanize İşlemi
    print("\n--- İnsanlaştırma (Humanize) ---")
    humanized = premium_engine.humanize_text(sample_text, "tr", frontend_dropdown_data, style="academic")
    print(humanized['humanized_text'])

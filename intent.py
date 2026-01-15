import re

class SimpleIntentClassifier:
    def classify(self, text: str):
        text_lower = text.lower()
        
        # Rule-based classification (NO transformers needed!)
        if re.search(r'^(hi|hello|hey|greetings|good morning|good afternoon)', text_lower):
            return {"primary_intent": "casual_greeting", "confidence": 0.95}
        
        if re.search(r'(sign up|buy|purchase|subscribe|ready to|want to try|my (youtube|instagram|tiktok|channel))', text_lower):
            return {"primary_intent": "high_intent_lead", "confidence": 0.90}
        
        if re.search(r'(price|cost|plan|how much|feature|what does|tell me about|refund|policy|support)', text_lower):
            return {"primary_intent": "product_inquiry", "confidence": 0.85}
        
        # Default
        return {"primary_intent": "product_inquiry", "confidence": 0.60}
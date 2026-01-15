import json

class SimpleRAG:
    def __init__(self):
        # Direct knowledge (NO sentence-transformers needed!)
        self.knowledge = {
            "pricing": {
                "Basic Plan": "$29/month - 10 videos/month - 720p",
                "Pro Plan": "$79/month - Unlimited videos - 4K - AI captions"
            },
            "policies": {
                "refund": "No refunds after 7 days",
                "support": "24/7 support available only on Pro plan"
            },
            "features": "AutoStream: Automated video editing for creators. AI captions, 4K support, unlimited exports (Pro)."
        }
    
    def get_answer(self, question: str) -> str:
        question_lower = question.lower()
        
        if "price" in question_lower or "cost" in question_lower or "plan" in question_lower:
            response = "*Pricing Plans:*\n\n"
            for plan, details in self.knowledge["pricing"].items():
                response += f"📦 {plan}: {details}\n"
            response += f"\n*Policies:*\n• {self.knowledge['policies']['refund']}\n• {self.knowledge['policies']['support']}"
            return response
        
        elif "feature" in question_lower or "what does" in question_lower or "capability" in question_lower:
            return f"*Features:*\n{self.knowledge['features']}"
        
        elif "refund" in question_lower or "policy" in question_lower or "support" in question_lower:
            return f"*Policies:*\n• {self.knowledge['policies']['refund']}\n• {self.knowledge['policies']['support']}"
        
        else:
            return "I can help with pricing, features, or signing up. What would you like to know?"
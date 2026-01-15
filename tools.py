import json
from datetime import datetime

def mock_lead_capture(name: str, email: str, platform: str):
    """Simple lead capture function"""
    print("\n" + "="*50)
    print("✅ LEAD CAPTURED!")
    print("="*50)
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Platform: {platform}")
    print(f"Time: {datetime.now().strftime('%H:%M:%S')}")
    print("="*50)
    
    # Save to file
    lead = {
        "name": name,
        "email": email,
        "platform": platform,
        "timestamp": datetime.now().isoformat()
    }
    
    try:
        with open("leads.json", "a") as f:
            f.write(json.dumps(lead) + "\n")
    except:
        pass
    
    return True

class SimpleLeadTool:
    def _init_(self):
        self.data = {}
    
    def add_info(self, field: str, value: str):
        self.data[field] = value
        print(f"✅ Collected {field}")
    
    def is_complete(self):
        return all(f in self.data for f in ["name", "email", "platform"])
    
    def execute(self):
        if not self.is_complete():
            return False
        
        return mock_lead_capture(
            self.data["name"],
            self.data["email"],
            self.data["platform"]
        )
    
    def reset(self):
        self.data = {}
class SimpleState:
    def _init_(self):
        self.conversation = []
        self.current_step = "start"
        self.lead_data = {}
    
    def add_message(self, user: str, agent: str):
        self.conversation.append({"user": user, "agent": agent})
        
        # Keep only last 5 messages
        if len(self.conversation) > 5:
            self.conversation = self.conversation[-5:]
    
    def get_last_messages(self, count: int = 3):
        return self.conversation[-count:] if self.conversation else []
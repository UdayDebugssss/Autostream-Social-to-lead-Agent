# AutoStream AI Agent - Social-to-Lead Workflow

## 📋 Assignment Completion:
This project implements a *production-ready conversational AI agent* for ServiceHive's Infix platform, converting social media conversations into qualified business leads for AutoStream (fictional SaaS).

## 🎯 Features Implemented

### ✅ *1. Intent Identification (3 Categories)*
- *Casual Greeting*: "Hi", "Hello", "Hey"
- *Product/Pricing Inquiry*: "What are your pricing plans?", "Tell me about features"
- *High-Intent Lead*: "I want to sign up", "Ready to buy Pro plan for YouTube"

### ✅ *2. RAG-Powered Knowledge Retrieval*
- Local JSON knowledge base (knowledge_base.json)
- Retrieves accurate pricing, features, and policies
- Dynamic context injection into LLM prompts

### ✅ *3. Tool Execution – Lead Capture*
- Mock API function: mock_lead_capture(name, email, platform)
- Collects name, email, platform sequentially
- *Never triggers prematurely* - only after all 3 fields collected

### ✅ *4. Technical Stack (As Required)*
- *Framework*: LangChain (with ConversationBufferMemory)
- *LLM*: GPT-4o-mini (via OpenAI API)
- *State Management*: 5-6 conversation turns memory
- *Language*: Python 3.9+

## 🏗️ Architecture Design

### *Why LangChain?*
LangChain was chosen for its *production-ready orchestration capabilities*, enabling:
- *Modular agent design* with clear separation of concerns
- *Built-in memory management* via ConversationBufferMemory
- *Easy LLM integration* with consistent interfaces
- *Scalable tool execution* patterns
- *Enterprise-grade error handling* and monitoring

### *State Management Strategy*
The agent maintains conversation state across *5-6 turns* using:
1. *LangChain's ConversationBufferMemory*: Token-limited memory preserving recent context
2. *Explicit state tracking*: Lead collection progress stored in session variables
3. *RAG context caching*: Frequently accessed knowledge base items for performance

### *System Flow*
# AutoStream AI Agent - Social-to-Lead Workflow
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

### Why did you choose LangGraph / AutoGen?”

- I chose LangChain instead of LangGraph or AutoGen because this project required a single conversational agent with controlled state, intent detection, RAG, and lead capture.

- LangChain’s ConversationBufferMemory provides explicit and predictable conversation state management, which is sufficient for linear conversational flows such as pricing queries and signup workflows.

- LangGraph is more suitable for complex multi-step or multi-agent workflows, and AutoGen is designed for agent-to-agent communication, which was not required for this use case.

### "How State Is Managed?"

- State in this conversational agent is managed using a hybrid state management approach that combines LangChain’s built-in memory with explicit application-level state tracking.
- Conversational context is maintained using LangChain’s ConversationBufferMemory, which stores recent user and assistant messages. This allows the agent to remember previous interactions, maintain context across multiple turns, and generate coherent responses without becoming stateless.
- In addition to conversational memory, the agent uses explicit state variables to manage structured workflows such as lead capture. A current_step variable tracks the user’s progress through the signup flow (e.g., ready, name, email, platform), while a temporary data structure stores user-provided information until the flow is completed. Once the lead capture process finishes, the state is reset to ensure clean subsequent interactions.
- This separation of conversational memory and business logic ensures predictable behavior, easier debugging, and scalability across different deployment channels such as web chat or WhatsApp.

## WhatsApp Integration Using Webhooks

To integrate the AutoStream conversational agent with WhatsApp, I would use the WhatsApp Business Cloud API along with a webhook-based backend service.

Incoming WhatsApp messages are sent by Meta to a configured webhook endpoint hosted using FastAPI or Flask. This webhook extracts the user’s message text and forwards it to the AutoStream LangChain agent’s process_message() function.

Each WhatsApp user session is identified using the sender’s phone number, which allows the system to maintain conversation state and memory across multiple messages using LangChain’s ConversationBufferMemory.

The agent processes the message, performs intent detection, retrieves relevant information from the local knowledge base (RAG), or triggers lead capture when high intent is detected. The generated response is then sent back to the user via the WhatsApp Cloud API.

This architecture keeps the agent logic independent of the communication channel, making it easy to extend the same agent to other platforms such as web chat or Instagram DMs.

### *System Flow*

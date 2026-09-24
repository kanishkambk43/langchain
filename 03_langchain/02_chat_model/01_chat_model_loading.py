import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

# Load the model
llm = ChatOpenAI(
    model="gpt-5-mini",
    api_key=os.getenv("OPENAI_API_KEY")
)

# Use the model with custom prompts or query
response = llm.invoke("Explain embeddings in simple English.")

print(response.content)
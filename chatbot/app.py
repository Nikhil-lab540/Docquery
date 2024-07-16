from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langserve import add_routes  # Assuming langserve is correctly imported
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set environment variables for Langsmith
os.environ["LANGCHAIN_TRACKING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Initialize FastAPI app
app = FastAPI(
    title="langchain Server",
    version="1.0",
    description="A simple API server"
)



llm = Ollama(model = "llama3")

prompt1 =ChatPromptTemplate.from_template(" Get top 10 books on {topic}. Reply in only the names of the books")

prompt2 = ChatPromptTemplate.from_template("Give me a small information about {book}.")

add_routes(
    app,
    prompt2|llm,
    path="/essay/info"
)

add_routes(
    app,
    prompt1|llm,
    path="/essay")

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port =8000)

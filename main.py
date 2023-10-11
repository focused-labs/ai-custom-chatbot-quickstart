import logging
import os
import sys
from contextlib import asynccontextmanager

import openai
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from import_service import import_web_scrape_data
from models.imported_urls import ImportedUrls
from models.question import Question
from query_service import QueryService

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

allowed_origins = [
    "http://localhost:3000",
]

query_service = QueryService()


def init_logging():
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_logging()

    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"Hello World!"}


@app.post("/load-website-docs")
def load_web_scrape_documents(website: ImportedUrls):
    print(f"Loading the following web scraped docs: {website.page_urls}")
    import_web_scrape_data(website.page_urls)
    return {"status": "Complete - Website Docs Loaded"}


@app.post("/search-database/")
async def search_database(question: Question):
    return query_service.search_vector_database(question=question.text)


@app.post("/ask-agent/")
async def ask_agent(question: Question):
    return query_service.ask_agent(question=question.text)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

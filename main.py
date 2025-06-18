# main.py
from fastapi import FastAPI, UploadFile, File, Form
from pydantic import BaseModel
from typing import Optional, List
import base64
import json
import os
from utils import find_answer_from_corpus

app = FastAPI()

class QueryRequest(BaseModel):
    question: str
    image: Optional[str] = None

class Link(BaseModel):
    url: str
    text: str

class QueryResponse(BaseModel):
    answer: str
    links: List[Link]

@app.post("/api/", response_model=QueryResponse)
def answer_question(request: QueryRequest):
    # Load corpus
    with open("tds_discourse_posts.json", "r", encoding="utf-8") as f:
        discourse_data = json.load(f)
    with open("tds_course_notes.json", "r", encoding="utf-8") as f:
        course_data = json.load(f)
    
    # Process
    answer, sources = find_answer_from_corpus(request.question, discourse_data, course_data)
    return QueryResponse(
        answer=answer,
        links=sources
    )

@app.get("/")
def read_root():
    return {"message": "Virtual TA is working!"}


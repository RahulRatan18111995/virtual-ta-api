# utils.py

import json
import base64
import os
from typing import Optional, List
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def load_knowledge_base() -> List[dict]:
    """Loads Discourse posts and optionally course content."""
    kb = []

    # Load scraped Discourse posts
    if os.path.exists("tds_discourse_posts.json"):
        with open("tds_discourse_posts.json", "r", encoding="utf-8") as f:
            kb.extend(json.load(f))

    # Optional: Load static course notes
    if os.path.exists("tds_course_notes.json"):
        with open("tds_course_notes.json", "r", encoding="utf-8") as f:
            kb.extend(json.load(f))

    return kb

def decode_base64_image(base64_str: str, filename: str = "temp_image.webp") -> Optional[str]:
    """Saves base64 string to file and returns filename."""
    try:
        image_data = base64.b64decode(base64_str)
        with open(filename, "wb") as f:
            f.write(image_data)
        return filename
    except Exception as e:
        print(f"Error decoding base64 image: {e}")
        return None

def generate_answer(question: str, context_docs: List[dict]) -> dict:
    """Calls OpenAI to generate an answer using given context."""
    context_text = "\n\n".join([f"{doc['title']}\n{doc['content']}" for doc in context_docs[:5]])
    prompt = f"""
Answer the question based only on the below context.

Context:
{context_text}

Question: {question}
Answer:
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    return {
        "answer": response.choices[0].message.content.strip(),
        "links": [{"url": doc["url"], "text": doc["title"]} for doc in context_docs[:2]]
    }

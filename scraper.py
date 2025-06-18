import os
import json
from dotenv import load_dotenv
import requests

load_dotenv()  # Load .env variables

url = f"{os.getenv('DISCOURSE_URL')}/latest.json"

headers = {
    "x-csrf-token": os.getenv("DISCOURSE_CSRF"),
    "cookie": os.getenv("DISCOURSE_COOKIE"),
    "user-agent": os.getenv("DISCOURSE_USER_AGENT"),
}

response = requests.get(url, headers=headers)
response.raise_for_status()

data = response.json()

# Save JSON to file
with open("tds_discourse_posts.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Scraped data saved to tds_discourse_posts.json")

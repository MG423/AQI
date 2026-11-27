import os
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

print("Testing /api/v1/agents/chat endpoint...")

payload = {
    "message": "Hello! What can you do?"
}

response = client.post("/api/v1/agents/chat", json=payload)

print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")

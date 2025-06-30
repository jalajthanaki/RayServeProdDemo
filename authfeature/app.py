from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .key_manager import APIKeyManager
from typing import List

app = FastAPI(title="API Key Management Service", description="RESTful API for managing API keys with usage tracking.", version="1.0.0")

class KeyResponse(BaseModel):
    key: str

class KeysListResponse(BaseModel):
    keys: List[str]

class UsageResponse(BaseModel):
    key: str
    usage: int

@app.post("/create", response_model=KeyResponse)
def create_key():
    key = APIKeyManager.create_key()
    return {"key": key}

@app.get("/list", response_model=KeysListResponse)
def list_keys():
    keys = APIKeyManager.list_keys()
    return {"keys": keys}

@app.delete("/delete/{key}")
def delete_key(key: str):
    deleted = APIKeyManager.delete_key(key)
    if not deleted:
        raise HTTPException(status_code=404, detail="Key not found.")
    return {"status": "deleted"}

@app.post("/increment/{key}", response_model=UsageResponse)
def increment_usage(key: str):
    usage = APIKeyManager.increment_usage(key)
    if usage == -1:
        raise HTTPException(status_code=404, detail="Key not found.")
    return {"key": key, "usage": usage}

@app.get("/usage/{key}", response_model=UsageResponse)
def get_usage(key: str):
    usage = APIKeyManager.get_usage(key)
    return {"key": key, "usage": usage}

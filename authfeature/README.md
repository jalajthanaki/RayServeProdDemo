# AuthFeature: API Key Management with Redis

This module provides RESTful API and a minimal Gradio UI for API key management with usage tracking using Redis.

## Features
- Generate API keys (UUID4)
- List all keys
- Delete/revoke keys
- Track usage count for each key
- Increment usage count
- RESTful API (FastAPI, OpenAPI docs)
- Minimal Gradio UI
- Unit tests for key creation, listing, and usage increment

## Prerequisites
- Python 3.8+
- Redis running locally (Docker recommended)

### Start Redis with Docker:
```bash
docker run -d --name redis -p 6379:6379 redis
```

## Install dependencies
```bash
pip install fastapi gradio redis uvicorn
```

## Run RESTful API (FastAPI)
```bash
uvicorn authfeature.app:app --reload
```
- OpenAPI docs: [http://localhost:8000/docs](http://localhost:8000/docs)

## Run Gradio UI
```bash
python -m authfeature.gradio_app
```
- The UI will open in your browser.

## Run Unit Tests
```bash
python -m unittest authfeature.test_key_manager
```

---

- `authfeature/app.py`: FastAPI REST API
- `authfeature/gradio_app.py`: Gradio UI
- `authfeature/key_manager.py`: Key logic
- `authfeature/redis_client.py`: Redis connection
- `authfeature/test_key_manager.py`: Unit tests

---

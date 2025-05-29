# Ray Serve LLM Production Demo

This directory contains a production-grade LLM deployment using Ray Serve with an OpenAI-compatible API endpoint.

## Quick Start

1. Start the Ray Serve deployment:
```bash
serve run config.yaml
```

2. Monitor deployment status until it's running and healthy:
```bash
serve status
```

Wait until the deployment shows:
- Status: RUNNING
- All services are in healthy state

3. Use the OpenAI-compatible client:
```bash
python3 openai_client_qwen.py
```

## Project Structure

- `config.yaml`: Ray Serve deployment configuration
- `openai_client_qwen.py`: OpenAI-compatible client for interacting with the LLM
- `openai_chat.js`: k6 load testing script for performance testing

## Load Testing and GPU Scaling

This deployment supports GPU scaling when GPUs are available. To test the scaling behavior:

1. Install k6:
```bash
brew install k6
```

2. Run the load test:
```bash
k6 run openai_chat.js
```

3. Monitor GPU scaling:
   - Use `serve status` to check replica counts
   - View the Ray Dashboard at http://localhost:8265
   - Check the number of GPU replicas scaling up and down based on load

When GPUs are available, the deployment will automatically scale GPU replicas based on incoming request load, allowing for efficient resource utilization during peak usage.

## Client Usage

The `openai_client_qwen.py` provides an OpenAI-compatible interface to interact with the deployed LLM. It uses:
- Base URL: `http://localhost:8000/v1`
- Model: `qwen-1.5b`
- Supports streaming responses

## Notes

- Ensure the deployment is in RUNNING and healthy state before using the client
- The client uses a fake API key as authentication is handled by Ray Serve
- The endpoint supports OpenAI-compatible API calls for seamless integration

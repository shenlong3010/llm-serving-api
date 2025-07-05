from fastapi import FastAPI, Request
from prometheus_client import Counter, Histogram, generate_latest
from fastapi.responses import PlainTextResponse
from .model import generate

app = FastAPI()

REQ_COUNT = Counter("llm_requests_total", "Total LLM requests")
REQ_LATENCY = Histogram("llm_request_duration_seconds", "Request latency")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/generate")
@REQ_LATENCY.time()
def generate_text(prompt: str, max_tokens: int = 128) -> str:
    REQ_COUNT.inc()
    result = generate(prompt, max_tokens)
    return {"result": result}

@app.get("/metrics")
def metrics():
    return PlainTextResponse(generate_latest(), media_type="text/plain")
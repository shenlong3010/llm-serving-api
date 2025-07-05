# LLM Serving API (FastAPI + HuggingFace + Docker)
This project demonstrates how to build a production-ready LLM inference API using:
- HuggingFace Transformers for text generation
- FastAPI for serving and REST interface
- Prometheus metrics for observability
- Docker for isolated deployment
- CPU-only setup (GPU-ready upgrade available)

🚀 Features
- /generate - perform text generation
- /metrics - Prometheus-compatible metrics (latency, request count)
- /health - health check
- Minimal setup — runs on CPU or scales to GPU
- Easily extendable with larger models, streaming, or batching

📦 Model
- Default model: sshleifer/tiny-gpt2
- Lightweight GPT-2 variant
- CPU-friendly, zero-cost
- Intended for pipeline testing — not semantic quality

✅ You can upgrade to larger CPU-compatible models like:
EleutherAI/gpt-neo-125M
tiiuae/falcon-rw-1b
(all hosted on HuggingFace Hub — free to use)

🛠 Tech Stack
- FastAPI, Transformers, torch, uvicorn, prometheus_client
- Dockerized for reproducibility

📈 Example Usage
Generate text:
curl "http://localhost:8000/generate?prompt=What+is+AI&max_tokens=64"

Metrics:
http://localhost:8000/metrics

🧠 Future Extensions
- Replace model with quantized Mistral or LLaMA
- Add OpenTelemetry for request tracing
- Add request batching or streaming
- Serve via Triton Inference Server or BentoML

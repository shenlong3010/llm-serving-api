from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.1")
model = AutoModelForCausalLM.from_pretrained(
    "mistralai/Mistral-7B-Instruct-v0.1",
    torch_dtype="auto",
    device_map="auto",
)
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

def generate(prompt: str, max_tokens: int = 128) -> str:
    return generator(prompt, max_new_tokens=max_tokens)[0]["generated_text"]
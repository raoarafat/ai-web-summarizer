import openai  # type: ignore
import ollama
from utils.config import Config

# Initialize OpenAI client with API key
client = openai.Client(api_key=Config.OPENAI_API_KEY)

# Ollama model configuration
OLLAMA_MODEL = "deepseek-r1:1.5B"

def summarize_with_openai(text):
    """Summarize text using OpenAI's GPT model."""
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes web pages."},
                {"role": "user", "content": f"Summarize the following text: {text}"}
            ],
            max_tokens=300,
            temperature=0.7
        )
        summary = response.choices[0].message.content
        return summary
    except Exception as e:
        print(f"Error during OpenAI summarization: {e}")
        return None

def summarize_with_ollama(text):
    """Summarize text using Ollama's deepseek-r1 model."""
    try:
        messages = [
            {"role": "system", "content": "You are a helpful assistant that summarizes web pages."},
            {"role": "user", "content": f"Summarize the following text: {text}"}
        ]
        response = ollama.chat(model=OLLAMA_MODEL, messages=messages)
        summary = response['message']['content']
        return summary
    except Exception as e:
        print(f"Error during Ollama summarization: {e}")
        return None

def summarize_text(text, engine="openai"):
    """Generic function to summarize text using the specified engine (openai/ollama)."""
    if engine == "openai":
        return summarize_with_openai(text)
    elif engine == "ollama":
        return summarize_with_ollama(text)
    else:
        print("Invalid engine specified. Use 'openai' or 'ollama'.")
        return None

if __name__ == "__main__":
    sample_text = "Artificial intelligence (AI) is intelligence demonstrated by machines, as opposed to the natural intelligence displayed by animals and humans."

    # Summarize using OpenAI
    openai_summary = summarize_text(sample_text, engine="openai")
    print("OpenAI Summary:", openai_summary)

    # Summarize using Ollama
    ollama_summary = summarize_text(sample_text, engine="ollama")
    print("Ollama Summary:", ollama_summary)

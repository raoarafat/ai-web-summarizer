import openai # type: ignore
from utils.config import Config

# Initialize OpenAI client with API key
client = openai.Client(api_key=Config.OPENAI_API_KEY)

def summarize_text(text):
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
        
        # Accessing response content using the new API format
        summary = response.choices[0].message.content
        return summary
    except Exception as e:
        print(f"Error during summarization: {e}")
        return None

if __name__ == "__main__":
    sample_text = "Artificial intelligence (AI) is intelligence demonstrated by machines, as opposed to the natural intelligence displayed by animals and humans."
    summary = summarize_text(sample_text)
    print("Summary:", summary)

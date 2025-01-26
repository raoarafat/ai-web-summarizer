# AI Web Page Summarizer

This project is a simple AI-powered web page summarizer that uses OpenAI's GPT models to generate concise summaries of given text. The goal is to create a "Reader's Digest of the Internet" by summarizing web content efficiently.

## Features

- Summarize text using OpenAI's GPT models.
- Simple and modular code structure.
- Error handling for better reliability.

## Project Structure

```
ai-summarizer/
│-- summarizer/
│   │-- __init__.py
│   │-- summarizer.py   # Main summarization logic
│-- utils/
│   │-- __init__.py
│   │-- config.py       # Configuration settings
│-- main.py             # Entry point of the app
│-- .env                # Environment variables
│-- requirements.txt    # Python dependencies
│-- README.md           # Project documentation
```

## Prerequisites

- Python 3.8 or higher
- OpenAI API Key (You can obtain it from [OpenAI](https://platform.openai.com/signup))
- `conda` for managing environments (optional)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/ai-summarizer.git
   cd ai-summarizer
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   conda create --name summarizer-env python=3.9
   conda activate summarizer-env
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   Create a `.env` file in the project root and add your OpenAI API key:

   ```env
   OPENAI_API_KEY=your-api-key-here
   ```

## Usage

1. **Run the summarizer:**

   ```bash
   python main.py
   ```

2. **Sample Output:**
   ```shell
   Summary: AI refers to machines demonstrating intelligence similar to humans and animals.
   ```

## Configuration

You can modify the model, max tokens, and temperature in `summarizer/summarizer.py`:

```python
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[...],
    max_tokens=300,
    temperature=0.7
)
```

## Error Handling

If any issues occur, the script will print an error message, for example:

```
Error during summarization: Invalid API key or quota exceeded.
```

## Dependencies

The required dependencies are listed in `requirements.txt`:

```
openai
python-dotenv
```

Install them using:

```bash
pip install -r requirements.txt
```

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For any inquiries, please reach out to:

- Linkedin: https://www.linkedin.com/in/khanarafat/
- GitHub: https://github.com/raoarafat

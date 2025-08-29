# ScrapeAI 🕷️🤖

An intelligent web scraper powered by AI that can extract and parse specific information from websites using natural language descriptions.

## Features

- **Smart Web Scraping**: Uses Selenium with Bright Data proxy for reliable web scraping
- **CAPTCHA Handling**: Automatic CAPTCHA solving capabilities
- **AI-Powered Parsing**: Leverages Ollama's Llama 3.1 model to extract specific information using natural language queries
- **User-Friendly Interface**: Built with Streamlit for an intuitive web interface
- **Content Cleaning**: Automatically removes scripts, styles, and cleans HTML content
- **Batch Processing**: Splits large content into manageable chunks for efficient AI processing

## Prerequisites

- Python 3.7+
- Ollama installed and running locally
- Llama 3.1 model downloaded in Ollama
- Bright Data account (for web scraping proxy)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/ScrapeAI.git
cd ScrapeAI
```

2. Create a virtual environment:
```bash
python -m venv ai
source ai/bin/activate  # On Windows: ai\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Install and set up Ollama:
   - Download Ollama from [https://ollama.ai](https://ollama.ai)
   - Install the Llama 3.1 model:
   ```bash
   ollama pull llama3.1
   ```

## Configuration

⚠️ **Important**: You need to update the Bright Data connection string in `scrape.py`:

1. Sign up for a Bright Data account
2. Replace the `SBR_WEBDRIVER` variable in `scrape.py` with your own credentials:
```python
SBR_WEBDRIVER = 'https://brd-customer-YOUR_CUSTOMER_ID-zone-YOUR_ZONE:YOUR_PASSWORD@brd.superproxy.io:9515'
```

## Usage

1. Start the Ollama service:
```bash
ollama serve
```

2. Run the Streamlit application:
```bash
streamlit run main.py
```

3. Open your browser and navigate to the displayed local URL (usually `http://localhost:8501`)

4. Enter a website URL and click "Scrape Website"

5. Once scraping is complete, describe what information you want to extract from the page

6. Click "Parse Content" to get AI-powered extraction results

## How It Works

1. **Web Scraping**: The application uses Selenium with Bright Data's proxy service to fetch web pages, handling JavaScript rendering and CAPTCHAs automatically.

2. **Content Processing**: The raw HTML is processed to extract only the body content, remove scripts and styles, and clean the text.

3. **Content Chunking**: Large content is split into 6000-character chunks to work efficiently with the AI model.

4. **AI Parsing**: Each chunk is processed by Ollama's Llama 3.1 model using a custom prompt that extracts only the requested information.

## File Structure

```
ScrapeAI/
├── main.py          # Streamlit web interface
├── scrape.py        # Web scraping functionality
├── parse.py         # AI parsing with Ollama
├── requirements.txt # Python dependencies
└── README.md        # This file
```

## Dependencies

- `streamlit` - Web interface framework
- `selenium` - Web browser automation
- `beautifulsoup4` - HTML parsing
- `langchain` - AI/LLM framework
- `langchain_ollama` - Ollama integration for LangChain

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Disclaimer

This tool is for educational and research purposes. Always respect websites' robots.txt files and terms of service. Use responsibly and ensure you have permission to scrape the target websites.

## Troubleshooting

### Common Issues

1. **Ollama connection error**: Make sure Ollama is running (`ollama serve`) and the Llama 3.1 model is installed (`ollama pull llama3.1`)

2. **Selenium/ChromeDriver issues**: The application uses Bright Data's remote browser, so you don't need to manage ChromeDriver locally

3. **Import errors**: Make sure all dependencies are installed in your virtual environment

### Support

If you encounter any issues, please open an issue on GitHub with:
- Error message
- Steps to reproduce
- Your operating system and Python version

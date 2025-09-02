# ScrapeAI Personal Project

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

## Code help from Tec With Tim

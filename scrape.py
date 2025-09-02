# Web Scraping Module
# This module handles web scraping using Selenium WebDriver with Bright Data proxy
# and BeautifulSoup for HTML parsing and content extraction

from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

# Load environment variables from .env file
# This includes sensitive credentials like Bright Data proxy settings
load_dotenv()

# Get Bright Data connection string from environment variable
# Default placeholder URL is provided for reference - users must configure their own credentials
SBR_WEBDRIVER = os.getenv('SBR_WEBDRIVER', 'https://brd-customer-YOUR_CUSTOMER_ID-zone-YOUR_ZONE:YOUR_PASSWORD@brd.superproxy.io:9515')

# Validate that users have configured their own Bright Data credentials
# Prevents accidental usage of placeholder credentials
if 'YOUR_CUSTOMER_ID' in SBR_WEBDRIVER:
    raise ValueError("Please configure your Bright Data credentials in the .env file or environment variables")

# Main web scraping function using Selenium WebDriver
# Utilizes Bright Data's proxy service for reliable scraping and CAPTCHA handling

def scrape_website(website):
    """
    Scrape website content using Selenium WebDriver through Bright Data proxy.
    
    Args:
        website (str): URL of the website to scrape
    
    Returns:
        str: Raw HTML content of the scraped website
    """
    print("Launching chrome browser...")

    # Establish connection to Bright Data's Chrome browser service
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    
    # Use context manager to ensure proper cleanup of browser resources
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        # Navigate to the target website
        driver.get(website)
        
        # CAPTCHA handling using Bright Data's automatic CAPTCHA solver
        # This waits for and automatically solves CAPTCHAs if they appear
        print('Waiting captcha to solve...')
        solve_res = driver.execute('executeCdpCommand', {
             'cmd': 'Captcha.waitForSolve',
             'params': {'detectTimeout': 10000},  # 10 second timeout for CAPTCHA detection
         })
        print('Captcha solve status:', solve_res['value']['status'])
        print('Navigated! Scraping page content...')
        
        # Extract the complete HTML source code from the loaded page
        html = driver.page_source
        return html


def extract_body_content(html_content):
    """
    Extract only the body content from raw HTML.
    
    Args:
        html_content (str): Raw HTML content from scraped website
    
    Returns:
        str: Body content as string, or empty string if no body found
    """
    # Parse HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")
    # Extract only the body tag content (excludes head, meta tags, etc.)
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    """
    Clean and format body content for AI processing.
    Removes scripts, styles, and unnecessary whitespace.
    
    Args:
        body_content (str): Raw body HTML content
    
    Returns:
        str: Cleaned text content ready for AI processing
    """
    # Parse the body content with BeautifulSoup
    soup = BeautifulSoup(body_content, "html.parser") 
    
    # Remove script and style tags as they contain code, not readable content
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    # Extract plain text with newlines as separators
    cleaned_content = soup.get_text(separator="\n")
    # Remove empty lines and strip whitespace from each line
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())

    return cleaned_content 
# Content chunking for LLM processing
# Split large content into manageable chunks to avoid token limits
# Using 6000 characters per chunk (conservative limit for most LLMs)

def split_dom_content(dom_content, max_length=6000):
    """
    Split large DOM content into smaller chunks for LLM processing.
    
    Args:
        dom_content (str): Cleaned text content from website
        max_length (int): Maximum characters per chunk (default: 6000)
    
    Returns:
        list: List of text chunks, each within the specified length limit
    """
    # Split content into chunks of specified maximum length
    # This ensures each chunk fits within LLM token limits
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]
# updated comments
from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

#Get Bright Data connection string from environment variable(not using mine since this is a public repo lol)
SBR_WEBDRIVER = os.getenv('SBR_WEBDRIVER', 'https://brd-customer-YOUR_CUSTOMER_ID-zone-YOUR_ZONE:YOUR_PASSWORD@brd.superproxy.io:9515')

# Validate that credentials are configured
if 'YOUR_CUSTOMER_ID' in SBR_WEBDRIVER:
    raise ValueError("Please configure your Bright Data credentials in the .env file or environment variables")

#im using selenium to grab content from a website

# Scrape website content using Selenium
def scrape_website(website):
    print("Launching chrome browser...")

    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        driver.get(website)
        #CAPTCHA handling: If you're expecting a CAPTCHA on the target page, use the following code snippet to check the status of Browser API's automatic CAPTCHA solver
        print('Waiting captcha to solve...')
        solve_res = driver.execute('executeCdpCommand', { #this function solves captchas 
             'cmd': 'Captcha.waitForSolve',
             'params': {'detectTimeout': 10000},
         })
        print('Captcha solve status:', solve_res['value']['status'])
        print('Navigated! Scraping page content...')
        html = driver.page_source
        return html

# Extract body content from HTML
def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

# Clean body content by removing scripts and styles
def clean_body_content(body_content): #i'm taking in body content as a parameter and im going to clean it 
    soup = BeautifulSoup(body_content, "html.parser") 
    
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator="\n") #removing the empty lines 
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())

    return cleaned_content 
#I'm going to feed the LLM one batch of 6000 characters at a time. Its usually 8000 but im going with 6k to be safe

# Split DOM content into chunks for LLM processing
def split_dom_content(dom_content, max_length=6000):
    #i grab 6000 characters at at time and then loop through untill i get to the end of the dom content  
    return [
    dom_content[i : i +max_length] for i in range(0, len(dom_content), max_length)
    ]
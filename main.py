# AI Web Scraper - Main Application
# This is the main Streamlit application that provides a user interface
# for web scraping and AI-powered content parsing

import streamlit as st
from scrape import (
    scrape_website,
    extract_body_content,
    clean_body_content,
    split_dom_content,
)
from parse import parse_with_ollama

# Initialize Streamlit UI components
st.title("AI Web Scraper")
url = st.text_input("Enter Website URL")

# Step 1: Website Scraping Section
# This section handles the initial scraping of the website
if st.button("Scrape Website"):
    if url:
        st.write("Scraping the website...")

        # Execute the web scraping pipeline
        # 1. Scrape the raw HTML content from the website
        dom_content = scrape_website(url)
        # 2. Extract only the body content from the HTML
        body_content = extract_body_content(dom_content)
        # 3. Clean and format the content for processing
        cleaned_content = clean_body_content(body_content)

        # Store the processed DOM content in Streamlit session state
        # This allows the content to persist between user interactions
        st.session_state.dom_content = cleaned_content

        # Display the scraped content in an expandable text area
        # Users can view the raw content that will be processed
        with st.expander("View DOM Content"):
            st.text_area("DOM Content", cleaned_content, height=300)


# Step 2: Content Parsing Section
# This section allows users to extract specific information from the scraped content
# using AI-powered natural language queries
if "dom_content" in st.session_state:
    # Text area for user to describe what information they want to extract
    parse_description = st.text_area("Describe what you want to parse")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content...")

            # Process the content through AI parsing pipeline
            # 1. Split the DOM content into manageable chunks for the LLM
            dom_chunks = split_dom_content(st.session_state.dom_content)
            # 2. Send chunks to Ollama LLM with user's parsing instructions
            parsed_result = parse_with_ollama(dom_chunks, parse_description)
            # 3. Display the extracted information to the user
            st.write(parsed_result)
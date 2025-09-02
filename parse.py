# AI Content Parser Module
# This module handles the AI-powered parsing of scraped web content
# using Ollama LLM through LangChain framework

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Template for instructing the AI model on how to extract information
# This prompt ensures consistent, focused extraction of only the requested data
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
    
)

# Initialize the Ollama LLM model
# Using Llama 3.1 for content extraction and parsing tasks
model = OllamaLLM(model="llama3.1")

def parse_with_ollama(dom_chunks, parse_description):
    """
    Parse DOM content using Ollama LLM to extract specific information.
    
    Args:
        dom_chunks (list): List of text chunks from the scraped website content
        parse_description (str): User description of what information to extract
    
    Returns:
        str: Combined parsed results from all chunks
    """
    # Create a chat prompt template using our predefined instruction template
    prompt = ChatPromptTemplate.from_template(template)
    # Create a processing chain: prompt -> model
    chain = prompt | model 

    # Store results from each chunk processing
    parsed_results = []

    # Process each chunk of content individually
    # This prevents token limit issues with large content
    for i, chunk in enumerate(dom_chunks, start=1):
        # Send the chunk and user description to the AI model
        response = chain.invoke({"dom_content": chunk, "parse_description": parse_description}
        )

        # Provide progress feedback for long processing tasks
        print(f"Parsed batch {i} of {len(dom_chunks)}")
        parsed_results.append(response)

    # Combine all parsed results into a single response
    return "\n".join(parsed_results)

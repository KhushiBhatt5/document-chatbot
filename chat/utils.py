import os
import google.generativeai as genai
from pypdf import PdfReader
from django.conf import settings

def extract_text_from_pdf(file_path):
    """Extract text content from a PDF file."""
    try:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            # Handle Unicode errors by replacing problematic characters
            if page_text:
                # Remove or replace problematic Unicode characters
                page_text = page_text.encode('utf-8', errors='ignore').decode('utf-8')
                text += page_text + "\n"
        return text if text.strip() else "Error: Could not extract readable text from PDF."
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return f"Error: Could not extract text from PDF. {str(e)}"

def extract_text_from_txt(file_path):
    """Extract text content from a TXT file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except UnicodeDecodeError:
        # Try with different encoding if UTF-8 fails
        try:
            with open(file_path, 'r', encoding='latin-1') as file:
                return file.read()
        except Exception as e:
            print(f"Error reading TXT file: {e}")
            return f"Error: Could not read text file. {str(e)}"
    except Exception as e:
        print(f"Error reading TXT file: {e}")
        return f"Error: Could not read text file. {str(e)}"

def get_llm_response(history, context):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or api_key == "YOUR_API_KEY_HERE":
        return "Error: Gemini API Key not configured. Please set it in the .env file."

    genai.configure(api_key=api_key)
    
    # Use gemini-flash-latest which is available and supports generateContent
    model = genai.GenerativeModel('gemini-flash-latest')
    
    # Construct the prompt with context
    system_instruction = "You are a helpful assistant. Answer the user's question based on the provided context from the uploaded files. If the answer is not in the context, say so."
    
    if context:
        system_instruction += f"\n\nContext from files:\n{context}"
    
    # Get the last message from history
    last_message = history[-1]['parts'][0] if history else ""
    
    # Combine system instruction, context, and user question into one prompt
    full_prompt = f"{system_instruction}\n\nUser Question: {last_message}\n\nAssistant:"
    
    try:
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"Error generating response: {str(e)}"

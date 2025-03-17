import google.generativeai as genai
from config import GEMINI_API_KEY  # Import API key from config.py

# Configure the AI model with API Key
genai.configure(api_key=GEMINI_API_KEY)

def get_financial_advice(summary):
    """Generates financial advice using Google's Gemini AI."""
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    
    prompt = f"""
    I have the following monthly spending:
    {summary}
    Format your response as an HTML-styled report for Canadian end users with:
    - Budgeting Strategies
    -- Key insights based on my Canadian spending pattern
    -- Potential cost-cutting recommendations in Toronto
    - Canadian Savings & Investment Suggestions
    -- Emergency fund recommendations
    -- Where to allocate my savings efficiently
    - Canadian Cashback & CanadianCredit Card Optimization
    -- How to optimize cashback rewards based on spending habits
    -- Best financial products or strategies available
    - Avoid adding code block markers like ```html or ``` in your response
    """

    response = model.generate_content(prompt)
    return response.text


from flask import Flask, request, jsonify, render_template
import os
import pandas as pd
import PyPDF2
import google.generativeai as genai
from config import GEMINI_API_KEY
from process_pdf import extract_pdf_text
from gemini_ai import get_financial_advice
from data_analysis import analyze_transactions

app = Flask(__name__)

# Configure Gemini AI API
genai.configure(api_key=GEMINI_API_KEY)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'files' not in request.files:
        return jsonify({"error": "No files uploaded"}), 400
    
    files = request.files.getlist('files')
    if len(files) > 10:
        return jsonify({"error": "You can upload a maximum of 10 PDF files."}), 400
    
    all_transactions = []
    for file in files:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        
        # Extract transactions from each PDF
        text = extract_pdf_text(file_path)
        transactions = [
            {"category": "Retail & Grocery", "amount": 150.0},
            {"category": "Transportation", "amount": 50.0},
            {"category": "Insurance", "amount": 400.0},
        ]
        all_transactions.extend(transactions)
    
    spending_summary = analyze_transactions(all_transactions)
    advice = get_financial_advice(spending_summary)
    
    return render_template("results.html", summary=spending_summary, advice=advice)

if __name__ == '__main__':
    app.run(debug=True)


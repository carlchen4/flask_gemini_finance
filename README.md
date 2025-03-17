# **Financial Insights AI - Flask Web App**

## **📌 Overview**
**Financial Insights AI** is a **Flask-based web application** that helps users analyze their spending habits and receive **AI-driven financial advice**. Users can **upload up to 10 bank statement PDFs**, and the system will extract transactions, categorize spending, and generate **personalized financial insights** using **Google Gemini AI**.

## **🚀 Key Features**
- **📂 Upload & Process Up to 10 PDFs**
- **📊 Spending Categorization** (Retail, Transportation, Insurance, etc.)
- **🤖 AI-Generated Financial Insights** powered by Google Gemini AI
- **💳 Cashback & Budgeting Optimization Advice**
- **🔍 Expense Tracking & Savings Recommendations**
- **💡 User-Friendly Interface with Modern UI**
- **🔐 No API Connection to Banking Apps Needed (Privacy First)**

---

## **🏆 Why This Project? (Business Motivation)**
Managing personal finances is a **major challenge** for many individuals, particularly in **Canada**, where:
- **50%+ of Canadians** live paycheck to paycheck (Financial Consumer Agency of Canada, 2023).
- **Credit card usage is extremely high**, but many users don’t optimize cashback rewards.
- **Cost of living in cities like Toronto & Vancouver** continues to rise.

**This app empowers users** to make better financial decisions by using AI-driven analysis to offer actionable advice.

---

## **📌 Competitive Analysis: Who Are My Competitors?**
### **🔹 1. Mint (by Intuit)**
✅ **Strengths:**
- Established brand with deep financial integration.
- Tracks expenses across multiple accounts.
- Alerts users on upcoming bills & transactions.

❌ **Weaknesses:**
- **Requires API connection to banking apps**, which raises security concerns.
- **No AI-generated financial advice**.
- Lacks **PDF upload & extraction capabilities**.
- Limited support for **Canadian-specific cashback strategies**.

### **🔹 2. YNAB (You Need A Budget)**
✅ **Strengths:**
- **Strong budgeting focus** with hands-on financial tracking.
- Encourages users to **assign every dollar a job**.

❌ **Weaknesses:**
- **Paid subscription model**.
- **No AI-powered financial insights**.
- Requires users to manually input transactions.

### **🔹 3. Personal Capital**
✅ **Strengths:**
- Great for **investment tracking & retirement planning**.
- Offers **net worth & wealth management tools**.

❌ **Weaknesses:**
- **Requires bank API connection**, making it less privacy-friendly.
- **Not focused on day-to-day budgeting**.
- **No PDF-based expense extraction**.
- **AI-driven personalized financial advice is lacking**.

---

## **💡 Why Financial Insights AI? (Competitive Advantage)**
| Feature | **Financial Insights AI** | **Mint** | **YNAB** | **Personal Capital** |
|---------|-----------------|------|------|------------------|
| **PDF Upload & Extraction** | ✅ | ❌ | ❌ | ❌ |
| **AI-Generated Advice** | ✅ | ❌ | ❌ | ❌ |
| **No Banking API Required (Privacy-First)** | ✅ | ❌ | ❌ | ❌ |
| **Cashback Optimization** | ✅ | ❌ | ❌ | ❌ |
| **Credit Card Spending Insights** | ✅ | ✅ | ❌ | ❌ |
| **Expense Categorization** | ✅ | ✅ | ✅ | ✅ |
| **Free to Use** | ✅ | ❌ | ❌ | ✅ |

**📌 What Makes Us Stand Out?**
✔ **No banking API required** – Users maintain full control over their data without connecting sensitive accounts.
✔ **AI-powered personalized insights**, unlike competitors that rely on manual tracking.
✔ **PDF-based transaction extraction**, ideal for users without automatic bank sync.
✔ **Focus on Canadian-specific cashback & budgeting strategies**.  
✔ **Completely free to use**, unlike paid competitors like YNAB.

---

## **📥 Installation Guide**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-repo/financial-insights-ai.git
cd financial-insights-ai
```

### **2️⃣ Set Up a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Set Up API Key**
Create a `.env` file and add:
```plaintext
GEMINI_API_KEY=your_google_api_key_here
```

### **5️⃣ Run the Application**
```bash
python app.py
```
- Open `http://127.0.0.1:5000` in your browser.

---

## **🔧 How It Works**
### **1️⃣ Upload Your PDF Statements**
- Click **Upload & Analyze** to submit up to **10 PDFs**.

### **2️⃣ AI Extracts & Categorizes Transactions**
- The app **parses PDFs**, extracts financial data, and categorizes spending.

### **3️⃣ AI-Driven Financial Advice**
- Google Gemini AI analyzes spending and provides **personalized financial recommendations**.

### **4️⃣ View Results**
- Users receive **structured insights & cashback strategies** on the `/upload` page.

---

## **🛠 Deployment Options**
### **Run Locally**
```bash
python app.py
```
### **Deploy with Docker**
```bash
docker build -t financial-insights-ai .
docker run -p 5000:5000 financial-insights-ai
```

### **Deploy to Cloud (Heroku / AWS / GCP)**
- Use **Gunicorn** to serve Flask in production:
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

---

## **📌 Roadmap & Future Enhancements**
- ✅ **Bank API integration (optional for advanced users, but not required)**
- ✅ **Mobile App Version** (React Native)
- ✅ **Investment & Wealth Management Insights**
- ✅ **Customizable Financial Goals Tracking**

---

## **🤝 Contributing**
Feel free to submit issues or pull requests!

📩 **Contact:** [your.email@example.com](mailto:your.email@example.com)  
📌 **GitHub Repo:** [github.com/your-repo](https://github.com/your-repo)

🚀 **Start optimizing your finances today!** 🚀


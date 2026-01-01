# 📊 Ledger Agent

**Intelligent Financial Reconciliation & Anomaly Detection using Google Gemini**

![Status](https://img.shields.io/badge/Status-Active-success)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red)
![Gemini](https://img.shields.io/badge/AI-Google_Gemini-orange)
![LangChain](https://img.shields.io/badge/LangChain-1.0+-blue)
![Pandas](https://img.shields.io/badge/Pandas-1.0+-blue)

## 📝 Overview

The **Ledger Agent** is a powerful AI-driven tool designed to help finance teams ensure the accuracy of their financial records. By leveraging **Google Gemini**, the agent autonomously monitors, classifies, and reconciles ledger entries (debits/credits) to detect discrepancies and anomalies.

### Key Features
- **Automated Reconciliation**: Checks if debits equal credits instantly.
- **Anomaly Detection**: Identifies potential errors, missing entries, or suspicious transactions.
- **Natural Language Explanations**: Generates clear, human-readable audit reports.
- **Interactive UI**: Built with Streamlit for a seamless user experience.

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.12 or higher installed. You will also need a [Google AI Studio API Key](https://aistudio.google.com/).

### Installation

1. **Clone the repository** (if applicable) or navigate to your project folder.

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Setup**:
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Open `.env` and add your **Google API Key**:
     ```ini
     GOOGLE_API_KEY=your_actual_api_key_here
     ```

---

## 💻 Usage

1. **Run the Streamlit App**:
   ```bash
   streamlit run app.py
   ```

2. **Access the Agent**:
   - Open your browser (usually `http://localhost:8501`).
   - If you set your API key in `.env`, it will load automatically.
   - Otherwise, enter it Manually in the sidebar.

3. **Analyze**:
   - View the mock ledger data on the left.
   - Click **"Analyze Ledger"** to receive an instant AI audit report.

---

## 🧰 Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **AI/LLM**: [Google Gemini](https://deepmind.google/technologies/gemini/) via [LangChain](https://www.langchain.com/)
- **Data Processing**: [Pandas](https://pandas.pydata.org/)
- **Language**: Python

---

## 🧪 Example Data

The agent currently uses a mock dataset for demonstration:
| Date | Description | Account | Debit | Credit |
|------|-------------|---------|-------|--------|
| 2025-07-01 | Customer Payment | Accounts Receivable | 0 | 500 |
| 2025-07-01 | Revenue Recorded | Revenue | 500 | 0 |
| ... | ... | ... | ... | ... |

*(You can modify `ledger_data.py` to connect to real data sources)*

---

## 📄 License

This project is licensed under the MIT License.
import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from ledger_agent import run_ledger_analysis
from ledger_data import get_ledger

# Load environment variables
load_dotenv()

# Page Config
st.set_page_config(
    page_title="Ledger Agent | Financial Analysis AI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Professional Styling
st.markdown("""
<style>
    /* Global Background */
    .stApp {
        background-color: #f8f9fa;
    }
    
    /* Headers */
    h1, h2, h3 {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        color: #2c3e50;
    }
    
    /* Buttons */
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #4b6cb7 0%, #182848 100%);
        color: white;
        border: none;
        border-radius: 8px;
        height: 3em;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* Dataframe */
    .stDataFrame {
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        background-color: white;
        padding: 10px;
    }
    
    /* Result Box */
    .result-box {
        background-color: white;
        padding: 25px;
        border-radius: 10px;
        border-left: 5px solid #4CAF50;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        font-size: 1.1em;
        line-height: 1.6;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2704/2704029.png", width=100)
    st.title("Configuration")
    st.markdown("---")
    
    # Check if API Key is in env
    env_api_key = os.getenv("GOOGLE_API_KEY")
    
    if env_api_key:
        st.success("✅ API Key loaded from environment")
        api_key = env_api_key
    else:
        api_key = st.text_input(
            "🔑 Google API Key", 
            type="password", 
            help="Enter your Google Gemini API Key."
        )
        if not api_key:
            st.warning("⚠️ API Key not found. Please enter it here or set GOOGLE_API_KEY in .env")
    
    st.markdown("### ℹ️ About")
    st.info(
        """
        **Ledger Agent** uses **Google Gemini** to analyze financial transactions found in the ledger.
        
        It detects:
        - Imbalances
        - Anomalies
        - Missing entries
        """
    )
    
    st.markdown("---")
    st.caption("v1.0.0 | Built with Streamlit & Gemini")

# Main Content
st.title("📊 Ledger Analysis Agent")
st.markdown("### Intelligent Financial Reconciliation & Anomaly Detection")
st.markdown(
    """
    <div style='background-color: #e3f2fd; padding: 15px; border-radius: 10px; border-left: 5px solid #2196f3; margin-bottom: 25px;'>
        <strong>Welcome!</strong> This agent helps finance teams ensure accuracy by automatically auditing ledger entries.
    </div>
    """, 
    unsafe_allow_html=True
)

# Layout: Two columns
col1, col2 = st.columns([1.5, 1], gap="large")

with col1:
    st.subheader("🧾 Current Ledger Data")
    # Display preview
    df_preview = get_ledger()
    st.dataframe(df_preview, width='stretch', height=400)

with col2:
    st.subheader("🔍 Operations")
    st.write("Ready to audit the current ledger? Click below to start the AI analysis.")
    
    analyze_btn = st.button("🚀 Analyze Ledger", help="Run the AI analysis on the current mock data.")
    
    if analyze_btn:
        with st.spinner("🤖 AI Analyst is auditing the ledger..."):
            df, result = run_ledger_analysis(api_key)
            
        if "Error" in str(result):
             st.error("🚨 Analysis Failed")
             st.error(result)
        else:
            st.success("✅ Analysis Complete!")
            st.markdown("### 📝 Audit Report")
            st.markdown(f"""
            <div class="result-box">
                {result}
            </div>
            """, unsafe_allow_html=True)

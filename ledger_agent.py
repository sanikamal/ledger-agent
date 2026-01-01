import pandas as pd
from langchain_google_genai import ChatGoogleGenerativeAI
from ledger_prompt import ledger_template
from ledger_data import get_ledger

def run_ledger_analysis(api_key):
    if not api_key:
        return get_ledger(), "Please provide a valid Google API Key in the sidebar."

    try:
        df = get_ledger()
        ledger_table = df.to_string(index=False)
        
        prompt = ledger_template.format(ledger_table=ledger_table)
        
        # Initialize Gemini
        llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=api_key, temperature=0.2)
        
        response = llm.invoke(prompt)
        return df, response.content
        
    except Exception as e:
        # Return dataframe even if analysis fails, so user can see data
        try:
            df = get_ledger()
        except:
            df = pd.DataFrame()
        return df, f"Error running analysis: {str(e)}"

import streamlit as st
import pandas as pd
import os

# Page config
st.set_page_config(
    page_title="Simple Evergreen Dashboard",
    page_icon="🌲",
    layout="wide"
)

st.title("🌲 Simple Evergreen Dashboard")
st.write("Testing if the basic dashboard works...")

# Try to load the CSV file
try:
    if os.path.exists('validation_data.csv'):
        df = pd.read_csv('validation_data.csv')
        st.success(f"✅ Successfully loaded {len(df)} articles from CSV")
        st.write(f"Columns: {list(df.columns)}")
        
        # Show first few rows
        st.subheader("First 3 articles:")
        st.dataframe(df.head(3))
        
    else:
        st.error("❌ validation_data.csv not found")
        
except Exception as e:
    st.error(f"❌ Error loading CSV: {str(e)}")

st.write("If you can see this, the basic dashboard is working!") 
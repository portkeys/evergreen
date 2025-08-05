import streamlit as st
import pandas as pd
import os
from datetime import datetime
import json

# Page config
st.set_page_config(
    page_title="Debug Evergreen Dashboard",
    page_icon="🌲",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🌲 Debug Evergreen Dashboard")
st.write("Step 1: Basic setup works")

# Load data
try:
    df = pd.read_csv('validation_data.csv')
    st.success(f"✅ Step 2: CSV loaded - {len(df)} articles")
except Exception as e:
    st.error(f"❌ CSV error: {str(e)}")
    st.stop()

# Test basic data operations
try:
    total_articles = len(df)
    disagreements = len(df[~df['agreement']])
    agreements = len(df[df['agreement']])
    st.success(f"✅ Step 3: Data processing works - {agreements} agreements, {disagreements} disagreements")
except Exception as e:
    st.error(f"❌ Data processing error: {str(e)}")
    st.stop()

# Test sidebar
try:
    st.sidebar.header("📊 Test Sidebar")
    st.sidebar.metric("Total Articles", total_articles)
    st.success("✅ Step 4: Sidebar works")
except Exception as e:
    st.error(f"❌ Sidebar error: {str(e)}")
    st.stop()

# Test voter input
try:
    voter_name = st.sidebar.text_input("Your Name/ID", placeholder="e.g., john_doe")
    st.success("✅ Step 5: Text input works")
except Exception as e:
    st.error(f"❌ Text input error: {str(e)}")
    st.stop()

# Test data filtering
try:
    if voter_name:
        filtered_df = df[~df['agreement']]  # Show only disagreements
        st.success(f"✅ Step 6: Filtering works - {len(filtered_df)} disagreements to show")
    else:
        st.warning("⚠️ Enter a name to continue testing")
        st.stop()
except Exception as e:
    st.error(f"❌ Filtering error: {str(e)}")
    st.stop()

# Test displaying first article
try:
    if len(filtered_df) > 0:
        first_row = filtered_df.iloc[0]
        st.subheader("Step 7: Displaying first disagreement")
        st.write(f"**Title:** {first_row['title']}")
        st.write(f"**Category:** {first_row['category']}")
        st.write(f"**Human Label:** {'Evergreen' if first_row['human_label'] else 'Not Evergreen'}")
        st.write(f"**Model Prediction:** {'Evergreen' if first_row['model_prediction'] else 'Not Evergreen'}")
        st.success("✅ Step 7: Article display works")
    else:
        st.warning("No disagreements to display")
except Exception as e:
    st.error(f"❌ Article display error: {str(e)}")
    st.stop()

st.success("🎉 All steps completed! The issue is likely in the original dashboard's more complex components.") 
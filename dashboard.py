#!/usr/bin/env python3
"""
Evergreen Content Label Validation Dashboard

This dashboard allows editors and engineers to vote on whether model predictions
are more reasonable than human labels for disagreements.

Usage: streamlit run dashboard.py
"""

import streamlit as st
import pandas as pd
import os
from datetime import datetime
import json

# Page config
st.set_page_config(
    page_title="Evergreen Content Label Validation",
    page_icon="🌲",
    layout="wide",
    initial_sidebar_state="expanded"
)

def load_validation_data():
    """Load validation data from CSV"""
    if os.path.exists('validation_data.csv'):
        return pd.read_csv('validation_data.csv')
    else:
        st.error("❌ validation_data.csv not found. Please run the notebook experiment first.")
        st.stop()

def load_votes():
    """Load existing votes from JSON file"""
    if os.path.exists('validation_votes.json'):
        with open('validation_votes.json', 'r') as f:
            return json.load(f)
    return {}

def save_vote(article_id, voter_name, vote, reasoning=""):
    """Save a vote to JSON file"""
    votes = load_votes()
    
    if str(article_id) not in votes:
        votes[str(article_id)] = []
    
    vote_record = {
        'voter': voter_name,
        'vote': vote,  # 'human_better', 'model_better', 'both_wrong'
        'reasoning': reasoning,
        'timestamp': datetime.now().isoformat()
    }
    
    votes[str(article_id)].append(vote_record)
    
    with open('validation_votes.json', 'w') as f:
        json.dump(votes, f, indent=2)

def get_vote_summary(votes):
    """Calculate voting statistics"""
    total_votes = 0
    human_better = 0
    model_better = 0
    
    for article_votes in votes.values():
        for vote in article_votes:
            total_votes += 1
            if vote['vote'] == 'human_better':
                human_better += 1
            elif vote['vote'] == 'model_better':
                model_better += 1
    
    return {
        'total_votes': total_votes,
        'human_better': human_better,
        'model_better': model_better
    }

def main():
    # Title and description
    st.title("🌲 Evergreen Content Label Validation")
    st.markdown("""
    **Help us improve our evergreen content classification!**
    
    Below are articles where our AI model disagrees with human labels. 
    Please vote on which classification you think is more accurate.
    """)
    
    # Load data
    df = load_validation_data()
    votes = load_votes()
    
    # Sidebar with statistics
    st.sidebar.header("📊 Validation Progress")
    
    total_articles = len(df)
    disagreements = len(df[~df['agreement']])
    agreements = len(df[df['agreement']])
    
    st.sidebar.metric("Total Articles", total_articles)
    st.sidebar.metric("Agreements", agreements)
    st.sidebar.metric("Disagreements", disagreements)
    
    vote_stats = get_vote_summary(votes)
    st.sidebar.markdown("### 🗳️ Voting Summary")
    st.sidebar.metric("Total Votes", vote_stats['total_votes'])
    st.sidebar.metric("Human Label Better", vote_stats['human_better'])
    st.sidebar.metric("Model Prediction Better", vote_stats['model_better'])

    
    # Voter name input
    st.sidebar.markdown("### 👤 Voter Information")
    voter_name = st.sidebar.text_input("Your Name/ID", placeholder="e.g., john_doe")
    
    if not voter_name:
        st.warning("⚠️ Please enter your name in the sidebar to start voting.")
        st.stop()
    
    # Filter options
    st.sidebar.markdown("### 🔍 Filters")
    show_voted = st.sidebar.checkbox("Show already voted articles", value=False)
    
    # Filter data - show only disagreements
    filtered_df = df[~df['agreement']]
    
    if not show_voted:
        # Filter out articles already voted by this user
        already_voted = []
        for article_id, article_votes in votes.items():
            if any(vote['voter'] == voter_name for vote in article_votes):
                already_voted.append(int(article_id))
        filtered_df = filtered_df[~filtered_df['article_id'].isin(already_voted)]
    
    st.markdown(f"### Showing {len(filtered_df)} disagreement articles")
    
    # Display articles
    for idx, row in filtered_df.iterrows():
        article_id = row['article_id']
        
        # Article container with clear styling
        st.markdown("---")
        st.markdown(f"## 🔥 {row['title']}")
        
        # Article info
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown(f"**Source:** {row['source']}")
            if pd.notna(row['url']):
                st.markdown(f"**URL:** [View Article]({row['url']})")
            
            # Content preview
            with st.expander("📄 Content Preview"):
                st.text(row['body_content'])
        
        with col2:
            # Labels comparison
            st.markdown("#### Current Labels")
            
            # Human label
            human_label_text = "✅ Evergreen" if row['human_label'] else "❌ Not Evergreen"
            human_color = "green" if row['human_label'] else "red"
            st.markdown(f"**Human Label:** :{human_color}[{human_label_text}]")
            
            # Model prediction
            model_label_text = "✅ Evergreen" if row['model_prediction'] else "❌ Not Evergreen"
            model_color = "green" if row['model_prediction'] else "red"
            st.markdown(f"**Model Prediction:** :{model_color}[{model_label_text}]")
            
            st.markdown(f"**Confidence:** {row['model_confidence']}")
            
            # Model reasoning
            with st.expander("🤖 Model Reasoning"):
                st.text(row['model_reasoning'])
        
        # Voting section
        st.markdown("#### 🗳️ Which label is more accurate?")
        
        col_vote1, col_vote2 = st.columns(2)
        
        with col_vote1:
            if st.button(f"👤 Human Label Better", key=f"human_{article_id}", use_container_width=True):
                save_vote(article_id, voter_name, 'human_better')
                st.success("Vote recorded: Human label is better!")
                st.rerun()
        
        with col_vote2:
            if st.button(f"🤖 Model Prediction Better", key=f"model_{article_id}", use_container_width=True):
                save_vote(article_id, voter_name, 'model_better')
                st.success("Vote recorded: Model prediction is better!")
                st.rerun()
        
        # Show existing votes for this article
        if str(article_id) in votes:
            st.markdown("#### 📝 Previous Votes")
            for i, vote in enumerate(votes[str(article_id)]):
                vote_text = {
                    'human_better': '👤 Human Better',
                    'model_better': '🤖 Model Better'
                }.get(vote['vote'], vote['vote'])
                
                st.text(f"{vote['voter']}: {vote_text} ({vote['timestamp'][:10]})")
    
    # Export results
    st.sidebar.markdown("### 📤 Export")
    if st.sidebar.button("Download Votes CSV"):
        # Convert votes to DataFrame
        vote_records = []
        for article_id, article_votes in votes.items():
            for vote in article_votes:
                vote_records.append({
                    'article_id': article_id,
                    'voter': vote['voter'],
                    'vote': vote['vote'],
                    'reasoning': vote.get('reasoning', ''),
                    'timestamp': vote['timestamp']
                })
        
        if vote_records:
            votes_df = pd.DataFrame(vote_records)
            csv = votes_df.to_csv(index=False)
            st.sidebar.download_button(
                label="Download validation_votes.csv",
                data=csv,
                file_name="validation_votes.csv",
                mime="text/csv"
            )
        else:
            st.sidebar.info("No votes to export yet.")

if __name__ == "__main__":
    main()
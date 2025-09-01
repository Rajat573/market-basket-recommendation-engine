import streamlit as st
import pandas as pd
import pickle

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Personalized Recommendation Engine", layout="wide")

# --- LOAD DATA ---
# Load the dictionary of rules from the file
try:
    with open('cluster_rules.pkl', 'rb') as f:
        all_rules = pickle.load(f)
except FileNotFoundError:
    st.error("Rules file 'cluster_rules.pkl' not found. Please run the analysis notebook first.")
    st.stop()

# --- PERSONA DEFINITIONS ---
# You can write a short, descriptive persona for each cluster
persona_map = {
    0: {
        "name": "Core Organic Buyers",
        "description": "These customers are loyal, frequent shoppers who prioritize organic produce. Their baskets often contain combinations of organic fruits and vegetables."
    },
    1: {
        "name": "General Fresh Produce Shoppers",
        "description": "These shoppers focus on fresh fruits and vegetables. Their recommendations center around popular produce staples."
    },
    2: {
        "name": "General Fresh Produce Shoppers II",
        "description": "Similar to the other fresh produce group, these customers frequently purchase common fruits and vegetables."
    },
    3: {
        "name": "Sparkling Water Enthusiasts",
        "description": "This highly specific persona has a strong preference for sparkling water, often buying multiple flavors together. Recommendations for this group are very targeted."
    }
}


# --- UI LAYOUT ---
st.title("🛒 Customer Persona-Based Recommendation Engine")
st.markdown("This app showcases product recommendations tailored to different customer personas.")

# Sidebar for persona selection
st.sidebar.title("Select a Persona")
selected_persona_id = st.sidebar.selectbox(
    'Choose a customer persona to see their top recommendations:',
    options=list(persona_map.keys()),
    format_func=lambda x: f"Cluster {x}: {persona_map[x]['name']}"
)

# --- DISPLAY RESULTS ---
persona_info = persona_map[selected_persona_id]
st.header(f"Persona: {persona_info['name']}")
st.write(persona_info['description'])

st.subheader("Top 10 Product Recommendations (Association Rules)")

if selected_persona_id in all_rules and not all_rules[selected_persona_id].empty:
    rules_df = all_rules[selected_persona_id]
    
    # Clean up the frozensets for better display
    rules_df['antecedents'] = rules_df['antecedents'].apply(lambda a: ', '.join(list(a)))
    rules_df['consequents'] = rules_df['consequents'].apply(lambda a: ', '.join(list(a)))
    
    # Display the rules in a clean table
    st.dataframe(
        rules_df[['antecedents', 'consequents', 'confidence', 'lift']].head(10),
        use_container_width=True
    )
else:
    st.warning("No significant rules were found for this customer persona.")
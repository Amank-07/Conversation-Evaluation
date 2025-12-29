import streamlit as st
import json
import pandas as pd
from scorer import SCORER
from model_loader import load_model
from facet_engine import FacetEngine
from loader import load_facets
from preprocessor import preprocess_facets

st.set_page_config(page_title="Ahoum Conversation Evaluator", layout="wide")

st.title("Ahoum Conversation Evaluation Benchmark")

# Load facets
@st.cache_resource
def load_engine():
    df = load_facets("data/Facets Assignment - Facets Assignment.csv")
    df = preprocess_facets(df)
    engine = FacetEngine(df)
    return engine

engine = load_engine()

# Load model
@st.cache_resource
def load_scorer():
    model, tokenizer = load_model()
    return SCORER(model, tokenizer, batch_size=3)

scorer = load_scorer()

st.sidebar.header("Settings")
selected_facets = st.sidebar.slider("Number of facets to evaluate", 10, 300, 50)

conversation = st.text_area(
    "Enter a conversation",
    height=150,
    placeholder="User: I feel overwhelmed today. Assistant: I'm here to help you."
)

if st.button("Evaluate Conversation"):
    if conversation.strip():
        with st.spinner("Evaluating..."):
            facets = engine.get_facets()["facet"][:selected_facets]
            results = scorer.score(conversation, facets)

            df = pd.DataFrame(results)
            st.success(f"Evaluation complete — {len(df)} facets scored")
            st.dataframe(df, use_container_width=True)

            st.download_button(
                "Download Results",
                data=df.to_csv(index=False),
                file_name="evaluation_results.csv"
            )
    else:
        st.warning("Please enter a conversation.")

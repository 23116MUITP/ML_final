
import streamlit as st
import pandas as pd
from modules.data_loader import load_data
from modules.trend_logic import prepare_trend_data
from modules.visuals import plot_trend_chart, plot_top_topics

st.set_page_config(layout="wide")
st.title("📊 Content Trend Dashboard")

# Sidebar controls
uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])
granularity = st.sidebar.selectbox("Select Time Granularity", ["D", "W", "M"])

if uploaded_file:
    df = load_data(uploaded_file)
    st.success("Data loaded successfully!")

    # Flatten hashtag list and get unique tags
    all_tags = sorted(set(tag for sublist in df["hashtags"] for tag in sublist))
    selected_hashtag = st.sidebar.selectbox("Select a Hashtag to View", options=all_tags)

    # Filter data based on selected hashtag
    trend_df = prepare_trend_data(df, "timestamp", "hashtags", granularity, [selected_hashtag])

    st.subheader(f"📈 Frequency Over Time for #{selected_hashtag}")
    st.altair_chart(plot_trend_chart(trend_df, interactive=True), use_container_width=True)

    st.subheader("🏆 Top Hashtags Overall")
    st.altair_chart(plot_top_topics(df), use_container_width=True)
else:
    st.warning("Upload a CSV file to begin.")

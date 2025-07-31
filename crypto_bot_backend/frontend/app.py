import streamlit as st
import pandas as pd
import requests
import altair as alt

# --- Page Config ---
st.set_page_config(page_title="Crypto Trading Bot", page_icon="📈", layout="wide")

# --- Custom CSS for Fresh Look ---
st.markdown(
    """
    <style>
    .main {
        background: #f8f9fa;
        font-family: 'Segoe UI', sans-serif;
    }
    .stButton>button {
        background: linear-gradient(90deg, #4CAF50, #2E7D32);
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5em 1.5em;
        border: none;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #66BB6A, #388E3C);
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Header ---
st.title("🚀 **AI-Powered Crypto Trading Signal Bot**")
st.caption("Upload crypto price data and analyze market sentiment to get actionable trading signals.")

# --- Layout ---
col1, col2 = st.columns(2)

with col1:
    csv_file = st.file_uploader("📤 Upload `price.csv`", type="csv")
with col2:
    sentiment_text = st.text_area("🧠 Enter crypto news/tweet", height=100, value="Bitcoin crashes due to regulation.")

# --- Predict Button ---
if st.button("🔍 Analyze Market Signal"):
    if csv_file is not None and sentiment_text.strip() != "":
        # Send data to backend
        files = {"file": csv_file}
        data = {"sentiment_text": sentiment_text}

        try:
            response = requests.post("http://127.0.0.1:8000/predict", files=files, data=data)
            if response.status_code == 200:
                result = response.json()

                st.success(f"**Signal:** {result['signal']}  \n"
                           f"**Confidence:** {result['confidence']*100:.2f}%  \n"
                           f"**Sentiment Score:** {result['sentiment']}")

                # --- Price Chart ---
                csv_file.seek(0)
                df = pd.read_csv(csv_file)
                st.subheader("📉 Closing Price Trend")
                chart = alt.Chart(df).mark_line(point=True).encode(
                    x='timestamp:T',
                    y='close:Q',
                    tooltip=['timestamp', 'close']
                ).properties(width=800, height=400).interactive()
                st.altair_chart(chart, use_container_width=True)
            else:
                st.error(f"❌ Error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"⚠️ Could not connect to backend: {e}")
    else:
        st.warning("⚠️ Please upload a CSV file and enter sentiment text.")
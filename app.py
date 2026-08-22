import streamlit as st
import preprocessor

st.sidebar.title("Whatsapp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)

    st.dataframe(df)

    #Fetching unique users
    user_list = df['user'].unique().tolist()

    st.sidebar.selectbox("Show analysis with respect to", user_list)
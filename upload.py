import streamlit as st


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    video_file = open('uploaded_file', 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)

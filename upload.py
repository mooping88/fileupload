import streamlit as st
import cv2 as cv
import tempfile

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)
    vf = cv.VideoCapture(tfile.name)

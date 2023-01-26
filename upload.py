import streamlit as st
import cv2 as cv

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    vf = cv.VideoCapture(uploaded_file)
    

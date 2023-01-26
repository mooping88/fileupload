import streamlit as st
import cv2 as cv

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    vf = cv.VideoCapture(uploaded_file)
    
    while vf.isOpened():
        ret, frame = vf.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        stframe.image(gray)
    

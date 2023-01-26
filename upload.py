import streamlit as st


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
   # st.video(uploaded_file, format="video/mp4", start_time=0)
    video_file = open(uploaded_file, 'rb') #enter the filename with filepath

    video_bytes = video_file.read() #reading the file

    st.video(video_bytes) #displaying the video

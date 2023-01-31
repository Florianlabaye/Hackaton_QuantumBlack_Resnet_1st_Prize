import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import base64

st.set_page_config(
    page_title="Foodix",
    page_icon="👋",  
)
col1, col2 = st.columns([1,2])



with st.container():


    st.markdown('<style> body {background-color: Blue;}</style>',unsafe_allow_html=True)

    with col1:
        st.image(Image.open("assets/logo_foodix.png"))

    with col2:
        st.markdown("## _Revolutions in food storage_")


    im = Image.open("assets/logo_foodix.png")

st.sidebar.image(im)
#st.sidebar.title("#Hackathon X - QuamtunBlack")


video_file = open('assets/farmer_video.mp4', 'rb')
video_bytes = video_file.read()    
st.video(video_bytes)



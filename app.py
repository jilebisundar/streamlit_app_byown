import streamlit as st

from PIL import Image

st.title("SUNDAR DATA APP")
btn_click = st.button("click me")

if btn_click == True :
    st.subheader("you clicked me i am crying :cry:")
    st.balloons()
    st.snow()
image = Image.open("D:\\STREAMLIT-PROJECTS\\project1\\image27_frqkzv.png")
st.image(image , caption = "STRAMLIT IMAGE")
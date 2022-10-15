import streamlit as st
import base64
from PIL import Image
st.set_page_config(
    page_title="SAKEC",
    page_icon="$",
)
st.title('Health Diet & Nutrition')
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

feature_image1 = Image.open(r'C:\Users\Narendra\PycharmProjects\copy-of-git\app\pages\sakec.png')
with st.container():
    image_col, text_col = st.columns((1, 4))
    with image_col:
        st.image(feature_image1)
    with text_col:
        st.markdown(""" <style> .font {
        font-size:28px ; font-family: 'Black'; color: #FFFFF;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font", center >Mahavir Education Trust<br>Shah & Anchor Kutchhi Engineering College.</p>',unsafe_allow_html=True)

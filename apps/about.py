import streamlit as st
import numpy as np
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
from streamlit_option_menu import option_menu


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_bmzarwuq.json")
lottie_coding1= load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_cs6ygtm3.json")


def app():
 image_1 = Image.open("images/srijan.jpeg")
 image_2 = Image.open("images/harsh.jpeg")
 image_3 = Image.open("images/nilesh.jpeg")
 image_4 = Image.open("images/hemant.jpeg")
 image_5 = Image.open("images/ugersain.jpg")
 with st.container():
    left_column, right_column = st.columns([3,2])
    with left_column:
        st.title('WHO WE ARE')
        st.write("We're a team of passionate engineers who believe that independent investors need a better way to analyze and research stocks. ")
        st.write("This stock prediction platform that doesn't just show you data, it helps you interpret the data. ")
        st.write(" Our mission is to help part-time investors like us make better, long-term investment decisions. ")
    with right_column:
        st_lottie(lottie_coding, height=300, key="codin")
    
    #st.write("")
 
 with st.container():
        
    st.title("Our Team :-")
    
    st.write("---")
   
    st.write("##")
    image1,Text1,image2,Text2,image3,Text3= st.columns((2,2,2,2,2,2))
    with image1:
        st.image(image_1)
    with Text1:
        st.subheader("Srijan Saxena")
        st.write("DIT University")
    with image2:
        st.image(image_2)
    with Text2:
        st.subheader("Harsh Singh")
        st.write("DIT University")
   
    with image3:
        st.image(image_3)
    with Text3:
        st.subheader("Nilesh Kumar")
        st.write("DIT University")
    st.write("##")
    Text,image4,Text4,image5,Text5,text= st.columns((2,2,2,2,2,2))
    with Text:
        st.write("")
    with image4:
        st.image(image_4)
    with Text4:
        st.subheader("Hemant")
        st.write("DIT University")
    with image5:
        st.image(image_5) 
    with Text5:
        st.subheader("Ugersain")
        st.write("DIT University")
    with text:
        st.write("")  
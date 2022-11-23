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

lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/private_files/lf30_F3v2Nj.json")
lottie_coding1= load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_cs6ygtm3.json")

def app():
  
    with st.container():
     left_column, right_column = st.columns([2,3])
    with right_column:
        
        st.title("Stock Market Prediction Web ")
        st.subheader("A Simple And Efficient Way To Predict Stock Price")
        st.write("Stock Price Prediction using machine learning helps you discover the future value of company stock and other financial assets traded on an exchange. The entire idea of predicting stock prices is to gain significant profits. Predicting how the stock market will perform is a hard task to do. There are other factors involved in the prediction, such as physical and psychological factors, rational and irrational behavior, and so on. All these factors combine to make share prices dynamic and volatile. This makes it very difficult to predict stock prices with high accuracy. ")
    with left_column:
        st_lottie(lottie_coding1, height=300, key="codin")
    st.write("-----")
    with st.container():
     left_column, right_column = st.columns([2,3])
    with left_column:
        st.header("What Our App Does:-")
        st.write("##")
        st.subheader("""
               Our App uses Machine Learning algorithm that can predict data accurately:
               - This application seeks to utilize Deep Learning models, Long-Short Term Memory (LSTM)
                 Neural Network algorithm, to predict stock prices. For data with timeframes recurrent
                 neural networks (RNNs) come in handy but recent researches have shown that LSTM,
                 networks are the most popular and useful variants of RNNs.
                 We used Keras to build a LSTM to predict stock prices using historical closing price and
                 trading volume and visualize both the predicted price values over time and the optimal
                 parameters for the model.

               """
        )
        st.write("##")
        st.subheader("""
            Main problems that were faced by many users:
            - As financial institutions begin to embrace artificial intelligence, machine learning is increasingly utilized to help make trading decisions. Although there is an abundance of stock data for machine learning models to train on, a high noise to signal ratio and the multitude of factors that affect stock prices are among the several reasons that predicting the market difficult. At the same time, these models don’t need to reach high levels of accuracy because even 60% accuracy can deliver solid returns.
            
           
            
            """
        )
        
    with right_column:
        st_lottie(lottie_coding, height=400, key="coding")
    st.write("-----")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
from keras.models import load_model
import streamlit as st
import webbrowser
from sklearn import datasets
from datetime import date
from plotly import graph_objs as go

start = "2012-01-01"
end = date.today().strftime("%Y-%m-%d")
# In[6]:

def app():
 start = "2015-01-01"
 end = date.today().strftime("%Y-%m-%d")

 st.title('Market Prediction Zone:-')
 
 user_input=st.text_input('Enter Stock Ticker:','AAPL')
# In[7]:
 
 data_load_state = st.text('Loading data...')
 data = load_data(user_input)
 data_load_state.text('Loading data... Done!!!')

 st.subheader('Raw Data Of Stock Till Date:')
 st.subheader(end)
 #data=data.reset_index()
 #data=data.drop(['Adj Close'], axis=1)
 st.write(data.tail())
 if st.button('To see live stock prices click here'):
  url = 'https://finance.yahoo.com/'
  webbrowser.open_new_tab(url)
 st.write("---")
 
 fig = go.Figure()
 fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
 fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
 fig.layout.update(title_text='Graph of opening stock value VS closing stock value:-', xaxis_rangeslider_visible=True)
 st.plotly_chart(fig)
# In[8]:
 

#visuals
 st.subheader('Closing Price vs Time Chart')
 fig=plt.figure(figsize=(16,6))
 plt.plot(data.Close)
 st.pyplot(fig)


# In[11]:



 st.subheader('Closing Price vs Time Chart with 100MA')
 ma100=data.Close.rolling(100).mean()
 fig=plt.figure(figsize=(16,6))
 plt.plot(ma100,'r')
 plt.plot(data.Close) 
 st.pyplot(fig)


# In[12]:


 st.subheader('Closing Price vs Time Chart with 200MA')
 ma100=data.Close.rolling(100).mean()
 ma200=data.Close.rolling(200).mean()
 fig=plt.figure(figsize=(16,6))
 plt.plot(ma100,'r')
 plt.plot(ma200,'g')
 plt.plot(data.Close,'b')
 st.write(data.Close.tail(1)) 
 st.pyplot(fig)

 data_training=pd.DataFrame(data['Close'][0:int(len(data)*0.70)]) #we take only 70% values of close column  
 data_testing=pd.DataFrame(data['Close'][int(len(data)*0.70): int(len(data))])#we take remaining 30% values of close column 

 print(data_training.shape)

 print(data_testing.shape) # addition of both values will be equal to df.shape


# In[14]:


 from sklearn.preprocessing import MinMaxScaler #to ocnvert datas into scaled data
 scaler=MinMaxScaler(feature_range=(0,1))# each value of closing price will be scaled between 0 and 1


# In[15]:


 data_training_array=scaler.fit_transform(data_training)#converts values to array


# In[17]:


# load our model
 model=load_model('keras_model.h5')

#testing part
 past_100_days=data_training.tail(100)
 final_df = past_100_days.append(data_testing, ignore_index=True)
 input_data=scaler.fit_transform(final_df)

 x_test=[] #100 days are going to be x train example of 10 days
 y_test=[] #101th day is going to be y train
#as closing price of last day will be dependent on values of previous days

 for i in range(100,input_data.shape[0]):
    x_test.append(input_data[i-100:i])
    y_test.append(input_data[i,0])

 x_test,y_test=np.array(x_test),np.array(y_test)
 y_predicted=model.predict(x_test)

 scaler=scaler.scale_

 scale_factor=1/scaler[0]
 y_predicted=y_predicted*scale_factor
 y_test=y_test*scale_factor


# In[18]:


 st.subheader('Graph of Our Prediction vs Original')
 fig2=plt.figure(figsize=(16,6))
 plt.plot(y_test,'b',label= 'Original Price')
 plt.plot(y_predicted,'r',label= 'Predicted Price')
 plt.xlabel('Time')
 plt.ylabel('Price')
 plt.legend()
 st.pyplot(fig2)
 st.write(y_predicted)
 

def load_data(ticker):
 df = data.DataReader(ticker, 'yahoo', start,end)
 df.reset_index(inplace=True)
 return df
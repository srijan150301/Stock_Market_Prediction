#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
from keras.models import load_model
import streamlit as st




# In[6]:

page_bg_img = '''
<style>
body {
background-image: url("https://www.pexels.com/photo/close-up-photo-of-monitor-159888/");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

start = '2011-01-01'
end = '2021-12-31'

st.header("Stock Market Prediction")

user_input=st.text_input('Enter Stock Ticker','AAPL')
def load_data(ticker):
    df = data.DataReader(user_input, 'yahoo', start,end)
    df.reset_index(inplace=True)
    return df

df_load_state=st.text("Loading Data...")
df=load_data(user_input)
df_load_state.text("Loading Data... Done")
st.balloons()
# In[7]:


st.subheader('Raw Data ')
st.write(df.describe())


# In[8]:


#visulas
st.subheader('Closing Price vs Time Chart')
fig=plt.figure(figsize=(12,6))
plt.plot(df.Close) 
st.pyplot(fig)


# In[11]:



st.subheader('Closing Price vs Time Chart with 100MA')
ma100=df.Close.rolling(100).mean()
fig=plt.figure(figsize=(12,6))
plt.plot(ma100)
plt.plot(df.Close) 
st.pyplot(fig)


# In[12]:


st.subheader('Closing Price vs Time Chart with 200MA')
ma100=df.Close.rolling(100).mean()
ma200=df.Close.rolling(200).mean()
fig=plt.figure(figsize=(12,6))
plt.plot(ma100,'r')
plt.plot(ma200,'g')
plt.plot(df.Close,'b') 
st.pyplot(fig)


# In[13]:


data_training=pd.DataFrame(df['Close'][0:int(len(df)*0.70)]) #we take only 70% values of close column  
data_testing=pd.DataFrame(df['Close'][int(len(df)*0.70): int(len(df))])#we take remaining 30% values of close column 

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

x_test=[]
y_test=[]

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


st.subheader('Prediction vs Original')
fig2=plt.figure(figsize=(12,6))
plt.plot(y_test,'b',label= 'Original Price')
plt.plot(y_predicted,'r',label= 'Predicted Price')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
st.pyplot(fig2)


# In[ ]:





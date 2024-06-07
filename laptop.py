import pandas as pd
import numpy as np
import streamlit as st
import pickle as pk

model = pk.load(open('laptopprediction.pkl','rb'))

data = pd.read_csv('laptopPrice.csv')
st.header('Laptop Price Precdictor ')

pg = st.selectbox('Processor Generation',[10,11,7,8,9,4,12])
r = st.selectbox('RAM(GB)',[ 4,  8, 16, 32])
s = st.selectbox('SSD(GB)' , [ 0,  512,  256,  128, 1024, 2048, 3072])
h = st.selectbox('HDD(GB)' , [1024,    0,  512, 2048])
o = st.selectbox('OS',data['os'].unique())
if o == "Windows":
    gen = 0
if o == "DOS":
    gen = 1
if o == "Mac":
    gen = 2
b = st.selectbox('OS BITS(GB)',[64,32])
g = st.selectbox('Graphic Card Size(GB)',[0, 2, 4, 6, 8])

if st.button ('Predict'):
    input =np.array([[pg,r,s,h,gen,b,g]])
    x = model.predict(input)
    a = int(x[0])
    y = format(a,",")

    st.success(str(y)+"  Rupees")
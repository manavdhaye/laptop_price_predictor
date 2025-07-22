import streamlit as st
import pickle
import numpy as np
import math
import pandas as pd
df=pickle.load(open("df.pkl","rb"))
pipe = pickle.load(open("pipe.pkl", "rb"))
st.title("Laptop Predicyion System")


company = st.selectbox(("select company"),df["Company"].unique())
typename = st.selectbox(("select type "),df["TypeName"].unique())
ram=st.selectbox(("select Ram (GB)"),[2,4,6,8,12,16,24,32,64])
weight = st.number_input("Wight of a laptop")
sreen_size = st.number_input("Sreen Size")
touchscrren = st.selectbox(("Touchsreen"),["yes","no"])
ips = st.selectbox(("IPS"),["yes","no"])
scrren_resolution= st.selectbox(("Sreen Resolution"),["1920x1080","1366x768","1600x900","3840x2160","3200x1800","2880x1800","2560x1600","2560x1440","2304x1440"])
cpu= st.selectbox(("CPU Brand"),df["CPU_brand"].unique())
gpu= st.selectbox(("GPU Brand"),df["Gpu_brand"].unique())
os= st.selectbox(("OS"),df["os"].unique())
SDD= st.selectbox(("SDD(GB)"),[0,8,128,256,512,1024])
HDD= st.selectbox(("HDD(GB)"),[0,128,256,512,1024,2048])

if touchscrren=="yes":
    touchscrren=1
else:
    touchscrren=0

if ips=="yes":
    ips=1
else:
    ips=0

x_res=int(scrren_resolution.split("x")[0])
y_res=int(scrren_resolution.split("x")[1])
ppi=(((x_res**2)+(y_res**2))**0.5)/sreen_size if sreen_size > 0 else 0

if st.button("predict prize"):
    query=np.array([company,typename,ram,weight,touchscrren,ips,ppi,cpu,gpu,os,HDD,SDD])
    query=query.reshape(1,12)
    st.title(math.floor(int(np.exp(pipe.predict(query)[0]))))

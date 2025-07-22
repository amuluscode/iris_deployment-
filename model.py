import streamlit as st
import numpy as np
from predict import predict
st.title('classifying the types of iris')
col1,col2=st.columns(2)
with col1:
    st.text('sepal_characteristics')
    sepal_l=st.selectbox('enter the sepal_length',np.arange(1,9,0.3))
    sepal_w=st.selectbox('enter the sepal_width',np.arange(1,9,0.3))
with col2:
    st.text('sepal_characteristics')
    petal_l=st.selectbox('enter the petal_length',np.arange(1,9,0.3))
    petal_w=st.selectbox('enter the petal_width',np.arange(1,9,0.3))
if st.button('predict type of iris'):
    result=predict(np.array([[sepal_l,sepal_w,petal_l,petal_w]]))
    predicted_class=result
    st.success(f'predicted class is:{predicted_class}')
import streamlit as st

st.title('Hello World')

x = st.text_input('Enter your name')
st.write('Hello my friend:', x)

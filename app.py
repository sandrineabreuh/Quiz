import streamlit as st

st.title("hello")

num1= st.number_input("digite o primeiro numero: ")
num2= st.number_input("digite o segundo numero: ")

if st.button("calcular"):
    resultado= num1 + num2
    st.text("resultado: ")
    st.title(resultado)

st.title("calculadora")

st. writer("----")
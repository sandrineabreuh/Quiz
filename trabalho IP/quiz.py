import streamlit as st

pontuaçao= 0

contador_de_perguntas= 0

st.title ('Bem-vindo(a) ao quiz')
nome= st.text_input (" Qual seu nome?: ")
if nome: 
    st.text(f'Ola, podemos começar?: ')

    st.text (f'Qual a comida japonesa mais famosa no Brasil?')
    op1= st.button('Sushi')
    op2= st.button('yakissoba')

    if op1 == True:
        st.text('Correto!')
        pontuaçao += 1
        contador_de_perguntas += 1
    elif op2 == True:
        st.text('incorreto')
        contador_de_perguntas += 1

    if contador_de_perguntas == 1:
        st.text(f'Seu placar foi: {pontuaçao}')
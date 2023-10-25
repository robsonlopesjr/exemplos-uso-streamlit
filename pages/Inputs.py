import streamlit as st

d = {}

with st.form('Formulário de conta'):
    a, b = st.columns(2)
    d['nome'] = a.text_input('Seu nome:')
    d['sobrenome'] = b.text_input('Seu sobrenome:')

    d['email'] = st.text_input('Seu e-mail:')
    d['nascimento'] = st.date_input('Data de nascimento:')

    d['comentario'] = st.text_area('Um comentário:')

    st.form_submit_button('Enviar')

if d:
    st.json(d)

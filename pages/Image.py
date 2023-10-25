import streamlit as st
from PIL import Image
from rembg import remove


def remove_bg(image, widget):
    bytes_data = Image.open(image)
    output = remove(bytes_data)
    widget.image(output)


st.title('Exemplo upload de arquivo')
image = st.file_uploader('Upe uma foto', type=['jpg', 'png', 'jpeg'])

col_a, col_b = st.columns(2)

if image is not None:
    col_a.title('Imagem original')
    col_a.image(image)
    st.button('Remover fundo', on_click=remove_bg, args=(image, col_b))

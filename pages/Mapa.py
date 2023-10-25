import streamlit as st
import pandas as pd

ind = {
    'Indaiatuba': {'lat': -23.09, 'lon': -47.217778},
    'Manaus': {'lat': -3.1, 'lon': -60.016667},
}

df = pd.DataFrame(ind).transpose()

st.title('Conexão Indaiatuba - Manaus')

st.map(df)

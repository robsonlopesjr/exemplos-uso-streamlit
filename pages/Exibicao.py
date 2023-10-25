import streamlit as st
import pandas as pd

st.title('Exibição')

ind = {
    'Indaiatuba': {'lat': -23.09, 'lon': -47.217778},
    'Manaus': {'lat': -3.1, 'lon': -60.016667},
}

df = pd.DataFrame(ind).transpose()

st.header('Table')
st.table(df)

st.header('DataFrame')
st.dataframe(df)

a, b = st.columns(2)

a.header('Json')
a.json(ind)

b.header('Metrica')
b.metric('Métrica qualquer', '115', '10')

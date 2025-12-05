import streamlit as st
import numpy as np

st.set_page_config(
  page_title = 'Uji Hipotesis',
  page_icon= '📊',
  layout = 'wide'
)

st.sidebar.title('Navigasi')
st.sidebar.header('Uji Hipotesis')
st.sidebar.subheader('Kelompok 4')
st.sidebar.markdown(
  'Anggota Kelompok:',
  '- Ghaisan Adlan Falah\n',
  '- Nama \n',
  '- Nama \n',
  '- Nama \n',
  '- Nama \n',
  '- Nama \n',
  '- Nama \n',
  '- Nama \n'
)

page = st.sidebar.selectbox('Pilih Halaman', ['Home', 'Uji Rata-rata 1 Sampel', 'Uji Proporsi', 'Uji Rata-rata 2 Sampel Independen',

import streamlit as st
import re

text = st.text_input('Masukkan Teks Di sini')
result_text = re.sub('nama', ':blue[nama]', text, re.IGNORECASE )

st.markdown(result_text)
st.button('Reset')
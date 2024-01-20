import streamlit as st
from web3_script import *

st.title('Web3 Contract Interaction')

st.header('Function: addcount')
if st.button('Execute addcount', key='addcount_button'):
    result = addcount()
    st.write(f'Result: {result}')

st.header('Function: userCount')
if st.button('Execute userCount', key='userCount_button'):
    result = userCount()
    st.write(f'Result: {result}')


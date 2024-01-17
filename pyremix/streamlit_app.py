import streamlit as st
from web3_script import *

st.title('Web3 Contract Interaction')

st.header('Function: addUser')
_username = st.text_input('Enter _username', key='addUser__username').encode()
_favoriteNumber = st.number_input('Enter _favoriteNumber', step=1, key='addUser__favoriteNumber')
if st.button('Execute addUser', key='addUser_button'):
    result = addUser(_username, _favoriteNumber)
    st.write(f'Result: {result}')

st.header('Function: getFavoriteNumber')
_username = st.text_input('Enter _username', key='getFavoriteNumber__username').encode()
if st.button('Execute getFavoriteNumber', key='getFavoriteNumber_button'):
    result = getFavoriteNumber(_username)
    st.write(f'Result: {result}')

st.header('Function: getUserNameAtIndex')
_index = st.number_input('Enter _index', step=1, key='getUserNameAtIndex__index')
if st.button('Execute getUserNameAtIndex', key='getUserNameAtIndex_button'):
    result = getUserNameAtIndex(_index)
    st.write(f'Result: {result}')

st.header('Function: favoriteNumbers')
arg0 = st.text_input('Enter arg0', key='favoriteNumbers_arg0').encode()
if st.button('Execute favoriteNumbers', key='favoriteNumbers_button'):
    result = favoriteNumbers(arg0)
    st.write(f'Result: {result}')

st.header('Function: userNames')
arg0 = st.number_input('Enter arg0', step=1, key='userNames_arg0')
if st.button('Execute userNames', key='userNames_button'):
    result = userNames(arg0)
    st.write(f'Result: {result}')

st.header('Function: userCount')
if st.button('Execute userCount', key='userCount_button'):
    result = userCount()
    st.write(f'Result: {result}')


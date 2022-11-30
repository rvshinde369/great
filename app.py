import streamlit as st
import pandas as pd

st.write('''
#Greatest number displaying app
This application is intended to display greatest number among three numbers.'''
)
st.header('User Input Numbers')
number1 = st.number_input("Enter first number:")
number2 = st.number_input("Enter second number:")
number3 = st.number_input("Enter third number:")
greatest = number1
if number2>greatest:
    greatest=number2
if number3>greatest:
    greatest=number3
st.write('Greatest number is:',greatest)
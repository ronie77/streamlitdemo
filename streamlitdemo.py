# app.py
import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title('Simple Streamlit App')

# Creating a simple DataFrame
st.write("Here's a simple DataFrame:")

df = pd.DataFrame({
    'Column 1': [1, 2, 3, 4],
    'Column 2': [10, 20, 30, 40]
})

# Display the DataFrame in the app
st.write(df)

# Add some interactive widgets
if st.checkbox('Show chart'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C']
    )
    st.line_chart(chart_data)

# Slider example
x = st.slider('Select a value', 0, 100, 50)
st.write(f'The selected value is: {x}')

# Selectbox example
option = st.selectbox(
    'Select your favorite number',
    [1, 2, 3, 4, 5]
)
st.write(f'Your favorite number is: {option}')

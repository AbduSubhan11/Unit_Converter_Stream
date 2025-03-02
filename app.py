import streamlit as st

st.title('Unit Converter')
st.write('Welcome to the unit converter app! Please enter the values you would like to convert in length.')

converting_value = st.text_input('Enter the value:')

dropdown1 = st.selectbox('Select the unit you would like to convert from:', ['meters', 'kilometers', 'inches', 'feet', 'yards', 'miles'])
dropdown2 = st.selectbox('Select the unit you would like to convert to:', ['meters', 'kilometers', 'inches', 'feet', 'yards', 'miles'])

conversion_factors = {
    "meters": 1,
    "kilometers": 1000,
    "inches": 0.0254,
    "feet": 0.3048,
    "yards": 0.9144,
    "miles": 1609.34
}

if converting_value:  
    try:
        value = float(converting_value)
        if dropdown1 in conversion_factors and dropdown2 in conversion_factors:
            result = value * (conversion_factors[dropdown1] / conversion_factors[dropdown2])
            st.write(f"The conversion is: {result:.2f} {dropdown2}")
        else:
            st.write("Invalid unit selection.")
    except:
        st.write("Please enter a valid number.")


import streamlit as st

st.title("Unit Converter")

# Conversion types
conversion_type = st.selectbox('Select conversion type', ['Length', 'Mass'])

# Units dictionary
units = {
    'Length': ['Meters', 'Kilometers', 'Centimeters', 'Inches', 'Feet'],
    'Mass': ['Grams', 'Kilograms', 'Pounds', 'Ounces'],
    
}

# From and To unit select
from_unit = st.selectbox("From Unit", units[conversion_type])
to_unit = st.selectbox("To Unit", units[conversion_type])

# Value input
value = st.number_input("Enter value", value=0.0)

# Length Conversion
def convert_length(value, from_unit, to_unit):
    to_meters = {
        'Meters': 1,
        'Kilometers': 1000,
        'Centimeters': 0.01,
        'Inches': 0.0254,
        'Feet': 0.3048
    }
    from_meters = {
        'Meters': 1,
        'Kilometers': 0.001,
        'Centimeters': 100,
        'Inches': 39.3701,
        'Feet': 3.28084
    }
    value_in_meters = value * to_meters[from_unit]
    result = value_in_meters * from_meters[to_unit]
    return result

# Mass Conversion
def convert_mass(value, from_unit, to_unit):
    to_grams = {
        'Grams': 1,
        'Kilograms': 1000,
        'Pounds': 453.592,
        'Ounces': 28.3495
    }
    from_grams = {
        'Grams': 1,
        'Kilograms': 0.001,
        'Pounds': 1 / 453.592,
        'Ounces': 1 / 28.3495
    }
    value_in_grams = value * to_grams[from_unit]
    result = value_in_grams * from_grams[to_unit]
    return result

# Convert on button click
if st.button("Convert"):
    if conversion_type == 'Length':
        result = convert_length(value, from_unit, to_unit)
    elif conversion_type == 'Mass':
        result = convert_mass(value, from_unit, to_unit)
   

    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

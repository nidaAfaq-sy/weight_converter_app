import streamlit as st   # Using Streamlit for UI

# Function to perform conversation
def convert_weight(value, from_unit, to_unit):
    conversion_factors = {
        'kg': {'g': 1000, 'lb': 2.20462, 'oz': 35.274},
        'g' : {'kg': 0.001, 'lb': 0.00220462, 'oz': 0.035274},
        'lb': {'kg': 0.453592, 'g': 453.592, 'oz': 16},
        'oz': {'kg': 0.0283495, 'g': 28.3495, 'lb': 0.0625},
    }
    return value * conversion_factors[from_unit][to_unit] # Applying conversion formula

# Setting up the Streamlit UI
st.write("Weight Convertor") # Setting the title

st.write("This tool helps you convert between different weight units.") # Writing description

# Taking input from the user
value = st.number_input ("Enter weight", min_value=0.0, format="%f") # Number input field

# Selecting first unit
from_unit = st.selectbox("Select the initial unit :", ['kg', 'g', 'lb', 'oz'])

# Filtering available options for the second unit
available_units = [unit for unit in ['kg', 'g', 'lb', 'oz'] if unit != from_unit]

# Selecting second unit
to_unit = st.selectbox("Select the unit to convert to :", available_units)

# Conversion button functionally
if st.button("Convert"):
    if value  > 0:
        result = convert_weight(value,  from_unit, to_unit) # Calling conversion function
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}") # Displaying result
    else:
        st.error("Please enter a valid value (greater than 0).")    # Error message for invalid input

# Reset button to reload the page
if st.button("Reset"):
   st.rerun()   #  Reloading the page 
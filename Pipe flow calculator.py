# Praveen
import math
import streamlit as st

G = 9.81

st.set_page_config(page_title="Pipe Flow Calculator", page_icon="💧")

st.title("💧 PIPE FLOW CALCULATOR")
st.write("Calculate Reynolds Number, Friction Factor, Head Loss and Pressure Drop.")

st.sidebar.header("Select Calculation")

choice = st.sidebar.selectbox(
    "Choose an option",
    [
        "Reynolds Number",
        "Darcy Friction Factor",
        "Head Loss",
        "Pressure Drop",
        "Calculate All"
    ]
)

# Calculation functions

def calculate_reynolds_number(density, velocity, diameter, viscosity):
    return (density * velocity * diameter) / viscosity


def calculate_friction_factor(reynolds, roughness, diameter):
    if reynolds <= 0:
        raise ValueError("Reynolds number must be positive")

    if reynolds <= 2000:
        return 64.0 / reynolds
    else:
        relative_roughness = roughness / diameter
        term = (relative_roughness / 3.7) + (5.74

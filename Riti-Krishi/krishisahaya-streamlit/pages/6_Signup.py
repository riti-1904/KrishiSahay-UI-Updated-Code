import streamlit as st
from streamlit.components.v1 import html
from utils.auth import register_user

# Load CSS
def load_css():
    with open("static/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Signup Form
st.markdown("""
<div class="form-container">
    <h2>Farmer Registration</h2>
</div>
""", unsafe_allow_html=True)

with st.form("signup_form"):
    # Personal Info
    name = st.text_input("Full Name*", placeholder="Enter your full name")
    email = st.text_input("Email*", placeholder="Enter your email address")
    password = st.text_input("Password*", type="password", placeholder="Create a password")
    st.caption("At least 8 characters with numbers")
    
    # Agricultural Info
    st.markdown("---")
    st.markdown("### Agricultural Details")
    user_type = st.selectbox(
        "You are*",
        ["Farmer", "Agriculture Expert", "Other"],
        index=0
    )
    
    col1, col2 = st.columns(2)
    with col1:
        soil_type = st.selectbox(
            "Primary Soil Type*",
            ["Clay", "Sandy", "Loamy", "Black (Regur)", "Red", "Laterite"],
            index=0
        )
    with col2:
        land_area = st.number_input("Land Area (acres)*", min_value=0.1, step=0.1)
    
    irrigation_type = st.selectbox(
        "Primary Irrigation Method",
        ["Rainfed", "Well/Tube well", "Canal", "Drip Irrigation", "Sprinkler"],
        index=0
    )
    
    # Location
    location = st.text_input("Farm Location*", value="Fetching...", disabled=True)
    st.caption("Allow location access for accurate recommendations")
    
    if st.form_submit_button("Register Now"):
        if register_user(name, email, password, {
            "user_type": user_type,
            "soil_type": soil_type,
            "land_area": land_area,
            "irrigation_type": irrigation_type,
            "location": location
        }):
            st.success("Registration successful! Please login.")
            st.switch_page("pages/5_Login.py")

st.markdown("""
<p style="text-align:center">Already have an account? <a href="/Login" target="_self">Login here</a></p>
""", unsafe_allow_html=True)

# JavaScript for geolocation
html("""
<script>
navigator.geolocation.getCurrentPosition(
    position => {
        const locInput = window.parent.document.getElementById("location");
        if (locInput) {
            locInput.value = `${position.coords.latitude}, ${position.coords.longitude}`;
        }
    },
    error => console.error(error),
    { enableHighAccuracy: true }
);
</script>
""")
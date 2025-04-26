import streamlit as st
from streamlit.components.v1 import html
from utils.auth import authenticate_user

# Load CSS
def load_css():
    with open("static/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Login Form
st.markdown("""
<div class="form-container">
    <h2>Login</h2>
</div>
""", unsafe_allow_html=True)

with st.form("login_form"):
    email = st.text_input("Email", placeholder="Enter your email address")
    password = st.text_input("Password", type="password", placeholder="Enter your password")
    
    if st.form_submit_button("Login"):
        if authenticate_user(email, password):
            st.session_state.logged_in = True
            st.success("Login successful!")
            st.switch_page("main.py")
        else:
            st.error("Invalid credentials")

st.markdown("""
<p style="text-align:center">Don't have an account? <a href="/Signup" target="_self">Sign up</a></p>
""", unsafe_allow_html=True)
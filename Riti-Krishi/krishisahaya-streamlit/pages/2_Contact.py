import streamlit as st
import os

# Load CSS
def load_css():
    current_dir = os.path.dirname(__file__)  # Get current file directory
    css_path = os.path.join(current_dir, '..', 'static', 'styles.css')
    with open(css_path, encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Contact Form
st.markdown("""
<h1 style="text-align:center">Contact Us</h1>
<p style="text-align:center">We'd love to hear from you!</p>
""", unsafe_allow_html=True)

with st.form("contact_form"):
    name = st.text_input("Your Name", placeholder="Enter your full name")
    email = st.text_input("Your Email", placeholder="Enter your email address")
    subject = st.text_input("Subject", placeholder="Enter the subject")
    message = st.text_area("Your Message", height=150, placeholder="Write your message here")

    if st.form_submit_button("Send Message"):
        if name and email and message:
            # Save to database or send email (implementation needed)
            st.success("Message sent successfully!")
        else:
            st.error("Please fill all required fields")



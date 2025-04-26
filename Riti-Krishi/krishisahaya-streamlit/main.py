import streamlit as st
from streamlit.components.v1 import html

# Initialize session state for authentication
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Load CSS
def load_css():
    with open("static/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Custom Header with Navigation
def show_header():
    st.markdown("""
    <header>
        <div class="logo">Krishisahaya</div>
        <nav>
            <ul>
                <li><a href="/" target="_self">Home</a></li>
                <li><a href="/About" target="_self">About</a></li>
                <li><a href="/Features" target="_self">Features</a></li>
                <li><a href="/Contact" target="_self">Contact</a></li>
                <li><a href="/FAQ" target="_self">FAQ</a></li>
                <li><a href="/Login" target="_self">Login</a></li>
            </ul>
        </nav>
    </header>
    """, unsafe_allow_html=True)

# Main Page Content
def main_content():
    # Banner Section
    st.markdown("""
    <section class="banner">
        <h1>Empowering Farmers with Smart Solutions</h1>
        <p>Krishisahaya - ML Model for Sustainable Agricultural Development</p>
    </section>
    """, unsafe_allow_html=True)

    # Auth Buttons (only show when logged out)
    if not st.session_state.logged_in:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Login", key="login_btn"):
                st.switch_page("pages/5_Login.py")
        with col2:
            if st.button("Sign Up", key="signup_btn"):
                st.switch_page("pages/6_Signup.py")
    else:
        st.success(f"Welcome back! Explore the features below.")

    # Footer
    st.markdown("""
    <footer>
        <p>Contact us: support@krishisahaya.com | Follow us on:</p>
        <div class="social-icons">
            <a href="#">Facebook</a>
            <a href="#">Twitter</a>
            <a href="#">Instagram</a>
        </div>
    </footer>
    """, unsafe_allow_html=True)

# App Layout
def main():
    show_header()

    if st.session_state.logged_in:
        # Show logout button if logged in
        if st.sidebar.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()

    main_content()

if __name__ == "__main__":
    main()




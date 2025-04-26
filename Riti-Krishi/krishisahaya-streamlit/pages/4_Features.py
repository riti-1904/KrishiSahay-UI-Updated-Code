import streamlit as st

# Load CSS
def load_css():
    with open("static/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Hero Section
st.markdown("""
<section class="features-hero">
    <h1>Our Features</h1>
    <p>Explore the smart tools and innovative solutions we provide for modern agriculture.</p>
</section>
""", unsafe_allow_html=True)

# Features Grid
features = [
    ("Weather Updates", "weather.png", "Accurate and real-time weather forecasts"),
    ("Crop Recommendations", "crop.png", "AI-driven suggestions for the best crops"),
    ("Market Trends", "market.png", "Live updates on crop prices and trends"),
    ("Community Chat", "chat.png", "Connect with fellow farmers")
]

cols = st.columns(2)
for idx, (title, img, desc) in enumerate(features):
    with cols[idx % 2]:
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        st.image(f"static/images/{img}", width=80)
        st.markdown(f"""
            <h3>{title}</h3>
            <p>{desc}</p>
            <button class="feature-btn">Learn More</button>
        </div>
        """, unsafe_allow_html=True)

# CTA Section
st.markdown("""
<div class="cta">
    <h2>Ready to transform your farming?</h2>
    <p>Join Krishisahaya today and experience the benefits of modern agriculture.</p>
</div>
""", unsafe_allow_html=True)

if st.button("Get Started", key="cta_btn"):
    st.switch_page("pages/5_Login.py")


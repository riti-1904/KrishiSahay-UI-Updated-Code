import streamlit as st

# Load CSS
def load_css():
    with open("static/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# FAQ Accordion Component
def faq_accordion():
    faq_html = """
    <div class="faq">
        <h1>Frequently Asked Questions</h1>
        <div class="accordion">
            <div class="accordion-item">
                <button class="accordion-header">What is Krishisahaya?</button>
                <div class="accordion-body">
                    <p>Krishisahaya is an innovative platform that uses machine learning and AI to provide farmers with climate forecasts, crop recommendations, and market price predictions.</p>
                </div>
            </div>
            <div class="accordion-item">
                <button class="accordion-header">How does the crop recommendation system work?</button>
                <div class="accordion-body">
                    <p>Our system analyzes local climate data, soil conditions, and weather forecasts to suggest the most suitable crops for a given region.</p>
                </div>
            </div>
            <div class="accordion-item">
                <button class="accordion-header">Is Krishisahaya available in all regions?</button>
                <div class="accordion-body">
                    <p>Currently available in select regions with ongoing expansion.</p>
                </div>
            </div>
            <div class="accordion-item">
                <button class="accordion-header">How accurate are the weather forecasts?</button>
                <div class="accordion-body">
                    <p>We use advanced models and real-time data from trusted sources.</p>
                </div>
            </div>
            <div class="accordion-item">
                <button class="accordion-header">Can I access Krishisahaya on mobile?</button>
                <div class="accordion-body">
                    <p>Yes! Our platform is fully mobile-friendly.</p>
                </div>
            </div>
        </div>
    </div>
    """
    st.components.v1.html(faq_html, height=600, scrolling=False)

faq_accordion()





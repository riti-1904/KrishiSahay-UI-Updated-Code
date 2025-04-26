import streamlit as st
from streamlit.components.v1 import html

# Load CSS
def load_css():
    with open("static/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Hero Section
st.markdown("""
<section class="about-hero">
    <h1>About Us</h1>
    <p>Your trusted partner in building a sustainable future for farmers.</p>
</section>
""", unsafe_allow_html=True)

# Mission Section
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("""
    <div class="mission">
        <h2>Our Mission</h2>
        <p>Our mission is to revolutionize agriculture by seamlessly integrating traditional practices with modern technological advancements...</p>
        <ul>
            <li>Equip farmers with precise climate forecasting</li>
            <li>Provide AI-driven crop recommendations</li>
            <li>Foster transparency in market prices</li>
            <li>Build a collaborative platform</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.image("static/images/image1.png", width=300)

# What We Offer
st.markdown("""<h2>What We Offer</h2>""", unsafe_allow_html=True)
cols = st.columns(4)
offers = [
    ("Climate Insights", "Get precise weather updates"),
    ("Crop Recommendations", "Best crops for your soil"),
    ("Market Trends", "Real-time market prices"),
    ("Community Support", "Connect with other farmers")
]
for idx, (title, desc) in enumerate(offers):
    with cols[idx]:
        st.markdown(f"""
        <div class="card">
            <h3>{title}</h3>
            <p>{desc}</p>
        </div>
        """, unsafe_allow_html=True)

# Team Section
st.markdown("""<h2>Meet Our Team</h2>""", unsafe_allow_html=True)
team_cols = st.columns(4)

# Team members with their respective images
team = [
    ("Prateek Giddaplavar", "AI Specialist", "static/images/p.png"),
    ("Ritika Pasari", "Data Scientist", "static/images/r.png"),
    ("Sakshi Nimbalkar", "Backend Engineer", "static/images/s.png"),
    ("Nilanjan Paul", "ML Expert", "static/images/n.png")
]

# Loop through the team list and display the images and details
for idx, (name, role, img_path) in enumerate(team):
    with team_cols[idx]:
        # Display image above the name and role
        st.image(img_path, width=150)
        st.markdown(f"""
        <div style="text-align:center">
            <h3>{name}</h3>
            <p>{role}</p>
        </div>
        """, unsafe_allow_html=True)

# # Meet Our Team
# st.markdown("""<h2>Meet Our Team</h2>""", unsafe_allow_html=True)
# team_cols = st.columns(4)
# team = [
#     ("Prateek Giddaplavar", "AI Specialist", "p.png"),
#     ("Ritika Pasari", "Data Scientist", "r.png"),
#     ("Sakshi Nimbalkar", "Backend Engineer", "s.png"),
#     ("Nilanjan Paul", "ML Expert", "n.png")
# ]
# for idx, (name, role, img) in enumerate(team):
#     with team_cols[idx]:
#         st.image(f"static/images/{img}", width=150)
#         st.markdown(f"""
#         <div style="text-align:center">
#             <h3>{name}</h3>
#             <p>{role}</p>
#         </div>
#         """, unsafe_allow_html=True)













# import streamlit as st
# from streamlit.components.v1 import html

# # Load CSS
# def load_css():
#     with open("static/styles.css") as f:
#         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# load_css()

# # Hero Section
# st.markdown("""
# <section class="about-hero">
#     <h1>About Us</h1>
#     <p>Your trusted partner in building a sustainable future for farmers.</p>
# </section>
# """, unsafe_allow_html=True)

# # Mission Section
# col1, col2 = st.columns([2, 1])
# with col1:
#     st.markdown("""
#     <div class="mission">
#         <h2>Our Mission</h2>
#         <p>Our mission is to revolutionize agriculture by seamlessly integrating traditional practices with modern technological advancements...</p>
#         <ul>
#             <li>Equip farmers with precise climate forecasting</li>
#             <li>Provide AI-driven crop recommendations</li>
#             <li>Foster transparency in market prices</li>
#             <li>Build a collaborative platform</li>
#         </ul>
#     </div>
#     """, unsafe_allow_html=True)
# with col2:
#     st.image("static/images/image1.png", width=300)

# # What We Offer
# st.markdown("""<h2>What We Offer</h2>""", unsafe_allow_html=True)
# cols = st.columns(4)
# offers = [
#     ("Climate Insights", "Get precise weather updates"),
#     ("Crop Recommendations", "Best crops for your soil"),
#     ("Market Trends", "Real-time market prices"),
#     ("Community Support", "Connect with other farmers")
# ]
# for idx, (title, desc) in enumerate(offers):
#     with cols[idx]:
#         st.markdown(f"""
#         <div class="card">
#             <h3>{title}</h3>
#             <p>{desc}</p>
#         </div>
#         """, unsafe_allow_html=True)

# # Team Section
# st.markdown("""<h2>Meet Our Team</h2>""", unsafe_allow_html=True)
# team_cols = st.columns(4)
# team = [
#     ("Prateek Giddaplavar", "AI Specialist", "team1.jpg"),
#     ("Ritika Pasari", "Data Scientist", "team2.jpg"),
#     ("Sakshi Nimbalkar", "Backend Engineer", "team3.jpg"),
#     ("Nilanjan Paul", "ML Expert", "team3.jpg")
# ]
# for idx, (name, role, img) in enumerate(team):
#     with team_cols[idx]:
#         st.image(f"static/images/{img}", width=150)
#         st.markdown(f"""
#         <div style="text-align:center">
#             <h3>{name}</h3>
#             <p>{role}</p>
#         </div>
#         """, unsafe_allow_html=True)
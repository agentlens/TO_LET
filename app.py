import streamlit as st

# Set page configuration for mobile viewing
st.set_page_config(page_title="Property Details", page_icon="🏡", layout="centered")

# Custom CSS to style it like a clean physical card
st.markdown("""
    <style>
    .property-card {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .video-btn {
        display: block;
        width: 100%;
        text-align: center;
        background-color: #FF0000;
        color: white !important;
        padding: 12px;
        border-radius: 8px;
        font-weight: bold;
        text-decoration: none;
        margin: 15px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Render the Card UI
st.markdown("""
<div class="property-card">
    <h2>🏡 Premium 2 BHK Apartment</h2>
    <hr>
    <p><strong>🔹 Type:</strong> 2 BHK Residential</p>
    <p><strong>🔹 Bathrooms:</strong> 2 Toilets</p>
    <p><strong>🔹 Status:</strong> Available for Site Visit</p>
    
    <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" target="_blank" class="video-btn">
        📺 Watch Video Tour
    </a>
    
    <hr>
    <h4>📞 Contact Information</h4>
    <p><strong>Agent:</strong> Property Desk<br>
    <strong>Phone:</strong> +91 XXXXX XXXXX<br>
    <strong>Email:</strong> info@example.com</p>
</div>
""", unsafe_allow_html=True)
import streamlit as st

# 1. Page Config
st.set_page_config(page_title="Property Details", page_icon="🏡", layout="centered")

# 2. Build the entire application using clean markdown injecting blocks
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    .card-container {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        font-family: system-ui, -apple-system, sans-serif;
        max-width: 400px;
        margin: 10px auto;
        border: 1px solid #eaeaea;
    }
    .card-header { color: #1a1a1a; margin: 0; font-size: 14px; font-weight: 700; }
    .card-divider { border: 0; height: 1px; background: #e0e0e0; margin: 15px 0; }
    .feature-item { font-size: 16px; color: #333333; margin-bottom: 12px; }
    .video-btn {
        display: block; width: 100%; text-align: center; background-color: #FF0000;
        color: #ffffff !important; padding: 14px; border-radius: 8px; font-weight: bold;
        font-size: 16px; text-decoration: none; margin: 25px 0; box-shadow: 0 4px 10px rgba(255, 0, 0, 0.2);
    }
    .contact-box { background-color: #f9f9f9; padding: 15px; border-radius: 8px; border-left: 4px solid #007AFF; }
</style>

<div class="card-container">
    <h3 class="card-header">🏡 PROPERTY DETAILS</h3>
    <div style="color: #666666; font-size: 14px;">Available for Immediate To-Let</div>
    <hr class="card-divider">
    <div class="feature-item">🔹 <strong>Type:</strong> 2 BHK & Dining</div>
    <div class="feature-item">🔹 <strong>Floor:</strong> Ground</div>
    <div class="feature-item">🔹 <strong>Bathrooms:</strong> 2</div>
    <div class="feature-item">🔹 <strong>Rent:</strong> Rs.28,000 (Including water)</div>
    <div class="feature-item">🔹 <strong>Advance:</strong> Rs.1 Lakh</div>
    <div class="feature-item">🔹 <strong>Criteria:</strong> Only for Family</div>
    <div class="feature-item">🚫 <strong>Policy:</strong> NO PETS</div>
    <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" target="_blank" class="video-btn">📺 Watch Video Tour</a>
    <div class="contact-box">
        <div style="font-weight: bold; color: #1a1a1a; margin-bottom: 6px;">📞 CONTACT DETAILS</div>
        <strong>Phone:</strong> <a href="tel:+918105340081" style="color: #007AFF; text-decoration: none; font-weight: bold;">+91 8105340081</a>
    </div>
</div>
""", unsafe_allow_html=True)
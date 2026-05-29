import streamlit as st

# 1. Page Config
st.set_page_config(page_title="Property Details", page_icon="🏡", layout="centered")

# 2. Build the entire application using clean markdown injecting blocks
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    
    /* Main container styling */
    .card-container {
        background-color: #ffffff !important; /* Force white background */
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
        font-family: system-ui, -apple-system, sans-serif;
        max-width: 360px; /* Marginally narrower for better mobile fit */
        margin: 10px auto;
        border: 1px solid #eaeaea;
    }
    
    /* Header layout - Font size reduced to 18px and forced black */
    .card-header { 
        color: #000000 !important; 
        margin: 0; 
        font-size: 18px; 
        font-weight: 700; 
    }
    
    .card-divider { border: 0; height: 1px; background: #e0e0e0; margin: 12px 0; }
    
    /* Feature list layout - Font size reduced to 14px and forced dark gray */
    .feature-item { 
        font-size: 14px !important; 
        color: #333333 !important; 
        margin-bottom: 10px; 
        line-height: 1.4;
    }
    
    /* Strong tags inside items forced dark gray as well */
    .feature-item strong {
        color: #222222 !important;
    }
    
    /* High-visibility Action Button for YouTube link */
    .video-btn {
        display: block; 
        width: 100%; 
        text-align: center; 
        background-color: #FF0000;
        color: #ffffff !important; 
        padding: 12px; 
        border-radius: 8px; 
        font-weight: bold;
        font-size: 14px; 
        text-decoration: none; 
        margin: 20px 0; 
        box-shadow: 0 4px 10px rgba(255, 0, 0, 0.2);
    }
    
    /* Contact detail footer box */
    .contact-box { 
        background-color: #f9f9f9 !important; 
        padding: 12px; 
        border-radius: 8px; 
        border-left: 4px solid #007AFF;
        font-size: 14px !important;
        color: #444444 !important;
    }
    
    .contact-box strong {
        color: #222222 !important;
    }
</style>

<div class="card-container">
    <h2 class="card-header">🏡 PROPERTY DETAILS</h2>
    <div style="color: #666666 !important; font-size: 12px;">Available for Immediate To-Let</div>
    
    <hr class="card-divider">
    
    <div class="feature-list">
        <div class="feature-item">🔹 <strong>Type:</strong> 2 BHK</div>
        <div class="feature-item">🔹 <strong>Floor:</strong> Ground</div>
        <div class="feature-item">🔹 <strong>Bathrooms:</strong> 2</div>
        <div class="feature-item">🔹 <strong>Rent:</strong> Rs.28,000 (Including water)</div>
        <div class="feature-item">🔹 <strong>Advance:</strong> Rs.1 Lakh</div>
        <div class="feature-item">🔹 <strong>Criteria:</strong> Only for Family</div>
        <div class="feature-item">🚫 <strong>Policy:</strong> NO PETS</div>
    </div>
    
    <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" target="_blank" class="video-btn">📺 Watch Video Tour</a>
    
    <div class="contact-box">
        <div style="font-weight: bold; color: #1a1a1a !important; margin-bottom: 4px; font-size: 14px;">📞 CONTACT DETAILS</div>
        <strong>Phone:</strong> <a href="tel:+918105340081" style="color: #007AFF !important; text-decoration: none; font-weight: bold;">+91 8105340081</a>
    </div>
</div>
""", unsafe_allow_html=True)
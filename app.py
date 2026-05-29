import streamlit as st

# 1. Setup mobile-friendly viewport configurations
st.set_page_config(
    page_title="Property Details Brochure",
    page_icon="🏡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. Complete structural HTML and CSS layout for the Digital Card
property_card_html = """
<style>
    /* Hide default Streamlit padding and headers for a clean standalone look */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main container styling to mimic a physical card */
    .card-container {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        max-width: 450px;
        margin: 10px auto;
        border: 1px solid #eaeaea;
    }
    
    /* Header layout */
    .card-header {
        color: #1a1a1a;
        margin-top: 0;
        margin-bottom: 5px;
        font-size: 24px;
        font-weight: 700;
    }
    
    .card-divider {
        border: 0;
        height: 1px;
        background: #e0e0e0;
        margin: 15px 0;
    }
    
    /* Feature items configuration */
    .feature-list {
        margin: 20px 0;
    }
    
    .feature-item {
        font-size: 16px;
        color: #333333;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
    }
    
    /* High-visibility Action Button for YouTube link */
    .video-btn {
        display: block;
        width: 100%;
        box-sizing: border-box;
        text-align: center;
        background-color: #FF0000;
        color: #ffffff !important;
        padding: 14px;
        border-radius: 8px;
        font-weight: bold;
        font-size: 16px;
        text-decoration: none;
        margin: 25px 0;
        box-shadow: 0 4px 10px rgba(255, 0, 0, 0.2);
        transition: transform 0.1s ease, background-color 0.2s ease;
    }
    
    .video-btn:hover {
        background-color: #cc0000;
        text-decoration: none;
    }
    
    .video-btn:active {
        transform: scale(0.98);
    }
    
    /* Contact detail footer box */
    .contact-box {
        background-color: #f9f9f9;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #007AFF;
        font-size: 15px;
        color: #444444;
        line-height: 1.5;
    }
    
    .contact-title {
        font-weight: bold;
        color: #1a1a1a;
        margin-bottom: 6px;
        font-size: 16px;
    }
</style>

<div class="card-container">
    <div class="card-header">🏡 PROPERTY DETAILS</div>
    <div style="color: #666666; font-size: 14px;">Available for Immediate To-Let</div>
    
    <hr class="card-divider">
    
    <div class="feature-list">
        <div class="feature-item">🔹 &nbsp; <strong>Type:</strong> &nbsp; 2 BHK</div>
        <div class="feature-item">🔹 &nbsp; <strong>Floor:</strong> &nbsp; Ground</div>
        <div class="feature-item">🔹 &nbsp; <strong>Bathrooms:</strong> &nbsp; 2</div>
        <div class="feature-item">🔹 &nbsp; <strong>Rent:</strong> &nbsp; Rs.28,000 (Including water)</div>
        <div class="feature-item">🔹 &nbsp; <strong>Advance:</strong> &nbsp; Rs.1 Lakh</div>
        <div class="feature-item">🔹 &nbsp; <strong>Criteria:</strong> &nbsp; Only for Family</div>
        <div class="feature-item">🚫 &nbsp; <strong>Policy:</strong> &nbsp; NO PETS</div>
    </div>
    
    <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" target="_blank" class="video-btn">
        📺 Watch Video Tour
    </a>
    
    <div class="contact-box">
        <div class="contact-title">📞 CONTACT DETAILS</div>
        <strong>Phone:</strong> &nbsp; <a href="tel:+918105340081" style="color: #007AFF; text-decoration: none; font-weight: bold;">+91 8105340081</a><br>
        <span style="font-size: 12px; color: #777;">Tap the number above to call directly.</span>
    </div>
</div>
"""

# 3. Force Streamlit to render the custom HTML card structure securely
st.markdown(property_card_html, unsafe_allow_html=True)
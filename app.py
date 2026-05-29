import streamlit as st
import streamlit.components.v1 as components

# Set up mobile-friendly page settings
st.set_page_config(
    page_title="Property Details Brochure",
    page_icon="🏡",
    layout="centered"
)

# HTML & CSS Card Structure
html_code = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background-color: #f4f6f9;
            margin: 0;
            padding: 10px;
            display: flex;
            justify-content: center;
        }
        .card-container {
            background-color: #ffffff;
            padding: 24px;
            border-radius: 16px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            max-width: 400px;
            width: 100%;
            box-sizing: border-box;
            border: 1px solid #eaeaea;
        }
        .card-header {
            color: #1a1a1a;
            margin: 0 0 5px 0;
            font-size: 22px;
            font-weight: 700;
        }
        .card-divider {
            border: 0;
            height: 1px;
            background: #e0e0e0;
            margin: 15px 0;
        }
        .feature-list {
            margin: 20px 0;
        }
        .feature-item {
            font-size: 16px;
            color: #333333;
            margin-bottom: 12px;
            line-height: 1.4;
        }
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
        }
        .contact-box {
            background-color: #f9f9f9;
            padding: 15px;
            border-radius: 8px;
            border-left: 4px solid #007AFF;
            font-size: 15px;
            color: #444444;
        }
        .contact-title {
            font-weight: bold;
            color: #1a1a1a;
            margin-bottom: 6px;
        }
    </style>
</head>
<body>

<div class="card-container">
    <h2 class="card-header">🏡 PROPERTY DETAILS</h2>
    <div style="color: #666666; font-size: 14px;">Available for Immediate To-Let</div>
    
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
    
    <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" target="_blank" class="video-btn">
        📺 Watch Video Tour
    </a>
    
    <div class="contact-box">
        <div class="contact-title">📞 CONTACT DETAILS</div>
        <strong>Phone:</strong> <a href="tel:+918105340081" style="color: #007AFF; text-decoration: none; font-weight: bold;">+91 8105340081</a><br>
        <span style="font-size: 12px; color: #777;">Tap the number to call directly.</span>
    </div>
</div>

</body>
</html>
"""

# 3. Render the component using native iframe engine (height adjusted for mobile cards)
components.html(html_code, height=600, scrolling=True)
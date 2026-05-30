import streamlit as st

# 1. Page Config
st.set_page_config(page_title="Property Details", page_icon="🏡", layout="centered")

# 2. Store the entire HTML as a clean, single-line concatenation block to prevent Streamlit parsing errors
html_string = (
    "<style>"
    "#MainMenu, footer, header {visibility: hidden;}"
    ".card-container {background-color: #ffffff !important; padding: 24px; border-radius: 16px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06); font-family: system-ui, -apple-system, sans-serif; max-width: 360px; margin: 10px auto; border: 1px solid #e2e8f0;}"
    "h3.card-header {color: #000000 !important; margin: 0 0 4px 0 !important; font-size: 18px !important; font-weight: 700 !important;}"
    ".card-divider {border: 0; height: 1px; background: #e2e8f0; margin: 12px 0;}"
    ".feature-item {font-size: 14px !important; color: #334155 !important; margin-bottom: 10px; line-height: 1.5;}"
    ".feature-item strong {color: #0f172a !important;}"
    ".video-btn {display: block; width: 100%; box-sizing: border-box; text-align: center; background-color: #dc2626; color: #ffffff !important; padding: 12px; border-radius: 8px; font-weight: bold; font-size: 14px; text-decoration: none; margin: 20px 0; box-shadow: 0 4px 10px rgba(220, 38, 38, 0.2);}"
    ".contact-box {background-color: #f8fafc !important; padding: 14px; border-radius: 10px; border-left: 4px solid #2563eb; font-size: 14px !important; color: #334155 !important;}"
    "</style>"
    "<div class='card-container'>"
    "<h3 class='card-header'>🏡 PROPERTY DETAILS</h3>"
    "<div style='color: #64748b !important; font-size: 12px; font-weight: 500;'>Available for Immediate To-Let</div>"
    "<div style='color: #64748b !important; font-size: 12px; font-weight: 500;'>4th Main, AECS Layout,B-Block, Singasandra</div>"
    "<hr class='card-divider'>"
    "<div class='feature-list'>"
    "<div class='feature-item'>🔹 <strong>Type:</strong> 2 BHK & Dining</div>"
    "<div class='feature-item'>🔹 <strong>Floor:</strong> Ground</div>"
    "<div class='feature-item'>🔹 <strong>Bathrooms:</strong> 2</div>"
    "<div class='feature-item'>🔹 <strong>Rent:</strong> Rs.28,000 (Including water)</div>"
    "<div class='feature-item'>🔹 <strong>Advance:</strong> Rs.1 Lakh</div>"
    "<div class='feature-item'>🔹 <strong>Criteria:</strong> Only for Family</div>"
    "<div class='feature-item'>🚫 <strong>Policy:</strong> NO PETS</div>"
    "</div>"
    "<a href='https://youtube.com/shorts/4ygNBP2UEkY?feature=share' target='_blank' class='video-btn'>📺 Watch Video Tour</a>"
    "<div class='contact-box'>"
    "<div style='font-weight: bold; color: #0f172a !important; margin-bottom: 4px;'>📞 CONTACT DETAILS</div>"
    "<strong>Phone:</strong> <a href='tel:+918105340081' style='color: #2563eb !important; text-decoration: none; font-weight: bold;'>+91 8105340081</a>"
    "</div>"
    "</div>"
)

# 3. Securely render the string block
st.write(html_string, unsafe_allow_html=True)
import streamlit as st
import os
from PIL import Image
from datetime import datetime

# Create a directory to store photos
PHOTO_DIR = "photos"
os.makedirs(PHOTO_DIR, exist_ok=True)

# Page config
st.set_page_config(page_title="📸 My Photo Gallery", layout="wide")
st.title("📷 Google Photos Mini - Built with Streamlit")

# Photo upload
st.subheader("Upload Your Photos")
uploaded_files = st.file_uploader("Choose images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        # Save uploaded image
        file_path = os.path.join(PHOTO_DIR, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"Uploaded: {uploaded_file.name}")

# Show gallery
st.subheader("📸 Photo Gallery")
image_files = [f for f in os.listdir(PHOTO_DIR) if f.lower().endswith(('png', 'jpg', 'jpeg'))]

if image_files:
    cols = st.columns(4)
    for i, img_name in enumerate(sorted(image_files, reverse=True)):
        img_path = os.path.join(PHOTO_DIR, img_name)
        with cols[i % 4]:
            st.image(img_path, caption=img_name, use_column_width=True)
else:
    st.info("No photos uploaded yet!")

# Option to clear all
st.markdown("---")
if st.button("🗑️ Clear All Photos"):
    for f in image_files:
        os.remove(os.path.join(PHOTO_DIR, f))
    st.success("All photos deleted.")


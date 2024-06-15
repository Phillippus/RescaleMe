import streamlit as st
from PIL import Image

def resize_image_to_tiff(input_image, width_px, height_px, dpi):
    with Image.open(input_image) as img:
        # Resize the image to the specified dimensions
        img = img.resize((width_px, height_px), Image.LANCZOS)
        # Save the image as TIFF with high quality
        output_path = 'resized_image.tiff'
        img.save(output_path, dpi=(dpi, dpi), format='TIFF', compression='none')
        return output_path

# Streamlit UI
st.title("Image Resizer")

uploaded_file = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
    
    width_px = st.number_input("Enter the width in pixels:", value=2598)
    height_px = st.number_input("Enter the height in pixels:", value=2127)
    dpi = st.number_input("Enter the DPI:", value=300)
    
    if st.button("Resize Image"):
        output_path = resize_image_to_tiff(uploaded_file, width_px, height_px, dpi)
        st.success(f"Image has been resized and saved as {output_path}")
        with open(output_path, "rb") as file:
            btn = st.download_button(
                label="Download resized image",
                data=file,
                file_name="resized_image.tiff",
                mime="image/tiff"
            )
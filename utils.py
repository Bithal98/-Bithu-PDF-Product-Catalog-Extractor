from pdf2image import convert_from_bytes
from io import BytesIO

def get_pdf_images(uploaded_file):
    pdf_images = convert_from_bytes(
        uploaded_file.read(),
        poppler_path=r"C:\poppler\poppler-24.08.0\Library\bin"  # ✅ Make sure this path is correct
    )
    return pdf_images

def image_to_bytes(image):
    img_bytes = BytesIO()
    image.save(img_bytes, format='PNG')
    return img_bytes.getvalue()

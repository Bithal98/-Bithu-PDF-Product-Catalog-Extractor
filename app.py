import streamlit as st
from dotenv import load_dotenv
from utils import get_pdf_images
from extract import extract_product_data_from_pdf
from db import init_db, save_product_data

st.set_page_config(page_title="📦 Bithu Catalog Extractor")
st.title("📦 Bithu PDF Product Catalog Extractor")

load_dotenv()
init_db()

uploaded_file = st.file_uploader("📄 Upload product catalog PDF", type=["pdf"])

if uploaded_file:
    st.info("📄 PDF uploaded. Converting to images...")
    try:
        pdf_images = get_pdf_images(uploaded_file)
        st.success(f"✅ {len(pdf_images)} pages converted to images.")
    except Exception as e:
        st.error(f"❌ Error converting PDF to images: {e}")
        st.stop()

    with st.spinner("🧠 Extracting data using Gemini..."):
        results = extract_product_data_from_pdf(pdf_images)

    if results:
        st.success("✅ Data extracted and saved to database!")
        save_product_data(results)
        st.json(results)
    else:
        st.warning("⚠️ No structured data could be extracted from the PDF.")
        
import streamlit as st
import os

DB_PATH = "data/catalog.db"

# ...existing code...

if os.path.exists(DB_PATH):
    with open(DB_PATH, "rb") as db_file:
        st.download_button(
            label="⬇️ Download Database",
            data=db_file,
            file_name="catalog.db",
            mime="application/octet-stream"
        )
# ...existing code...
# -Bithu-PDF-Product-Catalog-Extractor
A powerful AI-based Streamlit application that extracts structured product data—like category, name, size, and specifications—from tile and ceramic product catalogs in PDF or image formats.  Utilizes Google Gemini 2.5 Pro to intelligently analyze brochure pages and outputs clean JSON and SQLite-stored data, enabling fast product indexing.

# 📦 Bithu PDF Product Catalog Extractor

An intelligent Streamlit web application to **extract structured product data from tile brochures or catalogs** (PDF or image format).  
Powered by **Google Gemini 2.5 Pro**, it identifies and parses product details like category, size, name, description, and specifications, storing them in **SQLite** and exporting as **JSON**.

---

## 🚀 Features

- 📄 Upload PDF catalogs or product images  
- 🤖 AI-powered data extraction using Gemini 2.5 Pro  
- 🧠 Parses visual and textual information from brochures  
- 🗃 Saves structured product info (category, subcategory, specs, etc.)  
- 💾 Data stored in **SQLite** and available for **download as JSON**  
- 🖼 Detects and marks image presence for each product  
- 🌐 Simple, interactive UI built with **Streamlit**

---

## 📌 Sample Output

```json
[
  {
    "category": "GVT",
    "subcategory": "Native Series",
    "product_name": "Native Crema",
    "size": "600x1200mm",
    "description": "Base tile with a stone-like texture in sandy, creamy tones...",
    "specifications": "Finish: DIGI MATT. Water Absorption: ≤0.5%...",
    "image_present": true
  }
]


📂 Folder Structure
📁 Bithu-PDF-Product-Catalog-Extractor/
├── app.py                  # Main Streamlit app
├── db.py                   # SQLite DB logic
├── extract.py              # Gemini API logic
├── utils.py                # PDF/image utilities
├── data/
│   └── catalog.db          # SQLite DB file (auto-generated)
├── requirements.txt
└── README.md

⚙️ Setup Instructions
1.Clone the repo:
git clone https://github.com/your-username/Bithu-PDF-Product-Catalog-Extractor.git
cd Bithu-PDF-Product-Catalog-Extractor

2.Install dependencies:
pip install -r requirements.txt
3.Download & set Poppler (for Windows users):
Download from: https://github.com/oschwartz10612/poppler-windows/releases/

Extract and copy the path to poppler/bin

Update utils.py with poppler_path="..."

4.Set your Google Gemini API key:
Create a .env file:
GOOGLE_API_KEY=your_gemini_api_key

5.Run the app:
streamlit run app.py

📤 Exported Data
SQLite Database: stored in data/catalog.db

JSON File: downloadable via the Streamlit UI

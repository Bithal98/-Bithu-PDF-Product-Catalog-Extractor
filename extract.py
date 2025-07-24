import json  # Use this instead of eval
import os
import google.generativeai as genai
from dotenv import load_dotenv
from utils import image_to_bytes

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-pro")

def extract_product_data_from_pdf(images):
    image_parts = [
        {
            "mime_type": "image/png",
            "data": image_to_bytes(image)
        }
        for image in images
    ]

    prompt = """
You are an expert in understanding tile product catalogs from brochures.
For each product in the image, extract:
- Category
- Subcategory
- Product Name
- Size
- Description
- Specifications (if any)
- Image presence (true/false)

Respond with ONLY valid JSON as a list of dictionaries. DO NOT return explanation or intro text. Example:
[
  {
    "category": "Wall Tiles",
    "subcategory": "Glossy",
    "product_name": "Marble Elegance",
    "size": "300x600mm",
    "description": "High gloss finish",
    "specifications": "Durable, waterproof",
    "image_present": true
  }
]
"""

    try:
        response = model.generate_content([prompt] + image_parts)
        text = response.text

        # ✅ Ensure we only extract JSON
        json_start = text.find("[")
        json_end = text.rfind("]") + 1
        if json_start != -1 and json_end != -1:
            json_data = json.loads(text[json_start:json_end])
            return json_data
        else:
            print("Gemini returned non-JSON text:", text)
            return []
    except Exception as e:
        print("Gemini error:", e)
        return []

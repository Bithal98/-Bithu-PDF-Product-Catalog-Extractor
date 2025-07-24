import sqlite3
import os

DB_PATH = "data/catalog.db"

def init_db():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT,
            subcategory TEXT,
            product_name TEXT,
            size TEXT,
            description TEXT,
            specifications TEXT,
            image_present BOOLEAN
        )
    """)
    conn.commit()
    conn.close()

def save_product_data(data):
    if not data:
        print("⚠️ No data to save.")
        return

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        for item in data:
            cursor.execute("""
                INSERT INTO products (
                    category, subcategory, product_name, size,
                    description, specifications, image_present
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                item.get("category", ""),
                item.get("subcategory", ""),
                item.get("product_name", ""),
                item.get("size", ""),
                item.get("description", ""),
                item.get("specifications", ""),
                bool(item.get("image_present", False))  # Ensure boolean
            ))
        conn.commit()
        print(f"✅ Saved {len(data)} products to the database.")
    except Exception as e:
        print(f"❌ Error saving to DB: {e}")
    finally:
        conn.close()

from fastapi import FastAPI, Query, HTTPException, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
import sqlite3
import os
from typing import List, Optional
from pydantic import BaseModel
import uvicorn

# Create FastAPI app
app = FastAPI(title="Succulent Collection API")

# Set up templates
templates = Jinja2Templates(directory="templates")

# Database configuration
DATABASE = 'succulents.db'

# Pydantic models for API responses
class CareTag(BaseModel):
    tag: str

class Succulent(BaseModel):
    id: int
    name: str
    image: str
    description: str
    care: List[str]

# Database helper functions
def get_db_connection():
    """Create a database connection"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize the database with the schema"""
    if not os.path.exists(DATABASE):
        conn = get_db_connection()
        with open('schema.sql', 'r') as f:
            conn.executescript(f.read())
        
        # Add sample data
        populate_sample_data(conn)
        
        conn.close()

def populate_sample_data(conn):
    """Add sample succulents and care tags to the database"""
    cursor = conn.cursor()
    
    # Check if data already exists
    cursor.execute("SELECT COUNT(*) FROM succulents")
    if cursor.fetchone()[0] > 0:
        return
    
    # Sample data
    sample_data = [
        (
            "Echeveria Elegans", 
            "/api/placeholder/400/320", 
            "Also known as Mexican Snowball, this rosette-forming succulent has pale blue-green leaves with pink-tinged edges."
        ),
        (
            "Haworthia Fasciata", 
            "/api/placeholder/400/320", 
            "Commonly called Zebra Plant, this small succulent has distinctive white ridges on its dark green leaves."
        ),
        (
            "Sedum Morganianum", 
            "/api/placeholder/400/320", 
            "Known as Burro's Tail or Donkey's Tail, this succulent has trailing stems with plump, tear-shaped leaves."
        ),
        (
            "Crassula Ovata", 
            "/api/placeholder/400/320", 
            "The Jade Plant features thick, woody stems and oval-shaped leaves that store water, making it drought-resistant."
        ),
        (
            "Aloe Vera", 
            "/api/placeholder/400/320", 
            "A medicinal plant with thick, fleshy leaves containing a gel-like substance used for healing burns and skin conditions."
        ),
        (
            "Kalanchoe Blossfeldiana", 
            "/api/placeholder/400/320", 
            "A flowering succulent with scalloped-edged leaves and clusters of small, brightly colored flowers."
        )
    ]
    
    cursor.executemany(
        "INSERT INTO succulents (name, image_url, description) VALUES (?, ?, ?)",
        sample_data
    )
    
    # Sample care tags
    care_data = [
        (1, "Low water"),
        (1, "Full sun"),
        (1, "Well-draining soil"),
        (2, "Partial shade"),
        (2, "Low water"),
        (2, "Indoor friendly"),
        (3, "Bright indirect light"),
        (3, "Minimal water"),
        (3, "Hanging baskets"),
        (4, "Bright light"),
        (4, "Low water"),
        (4, "Good for beginners"),
        (5, "Bright indirect light"),
        (5, "Moderate water"),
        (5, "Medicinal"),
        (6, "Bright light"),
        (6, "Low water"),
        (6, "Flowering")
    ]
    
    cursor.executemany(
        "INSERT INTO care_tags (succulent_id, tag) VALUES (?, ?)",
        care_data
    )
    
    conn.commit()

# Initialize the database on startup
init_db()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# API Routes
@app.get("/api/succulents", response_model=List[Succulent])
async def get_succulents(search: Optional[str] = Query(None, description="Search term for filtering succulents")):
    """
    Get all succulents or search by name, description, or care tag
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        if search:
            search_term = f"%{search.lower()}%"
            # Search for matching succulents with their care tags
            query = """
            SELECT DISTINCT s.id, s.name, s.image_url, s.description
            FROM succulents s
            LEFT JOIN care_tags c ON s.id = c.succulent_id
            WHERE LOWER(s.name) LIKE ? 
            OR LOWER(s.description) LIKE ?
            OR LOWER(c.tag) LIKE ?
            """
            cursor.execute(query, (search_term, search_term, search_term))
        else:
            cursor.execute("SELECT id, name, image_url, description FROM succulents")
        
        succulents_data = []
        for row in cursor.fetchall():
            # For each succulent, get its care tags
            cursor.execute("SELECT tag FROM care_tags WHERE succulent_id = ?", (row['id'],))
            care_tags = [tag['tag'] for tag in cursor.fetchall()]
            
            succulents_data.append({
                'id': row['id'],
                'name': row['name'],
                'image': row['image_url'],
                'description': row['description'],
                'care': care_tags
            })
        
        return succulents_data
    
    finally:
        conn.close()

@app.get("/", response_class=HTMLResponse)
async def get_home_page(request: Request):
    """Serve the home page with the succulent gallery"""
    return templates.TemplateResponse("index.html", {"request": request})

# For development server
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

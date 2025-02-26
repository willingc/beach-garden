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

# Database configuration - Using the test database
DATABASE = 'succulents_test.db'

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

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# API Routes
@app.get("/api/succulents", response_model=List[Succulent])
async def get_succulents(search: Optional[str] = Query(None, description="Search term for filtering succulents")):
    """
    Get all succulents or search by name, description, or care tag
    """
    if not os.path.exists(DATABASE):
        raise HTTPException(status_code=500, detail=f"Database '{DATABASE}' not found. Run create_test_db.py first.")
    
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

# Status endpoint to check database connection
@app.get("/api/status")
async def get_status():
    """Check if the database is available and return basic statistics"""
    if not os.path.exists(DATABASE):
        return {
            "status": "error",
            "message": f"Database '{DATABASE}' not found. Run create_test_db.py first."
        }
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Get counts
        cursor.execute("SELECT COUNT(*) FROM succulents")
        succulent_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM care_tags")
        tag_count = cursor.fetchone()[0]
        
        conn.close()
        
        return {
            "status": "ok",
            "database": DATABASE,
            "succulent_count": succulent_count,
            "care_tag_count": tag_count
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

# For development server
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

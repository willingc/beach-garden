I'll create a sample SQLite database for testing your succulent collection project.

```python
import sqlite3
import os

# Database file name
DB_FILE = 'succulents_test.db'

def create_test_database():
    """Create a test database with sample succulent data"""
    # Remove existing database if it exists
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
        print(f"Removed existing database: {DB_FILE}")
    
    # Connect to the database
    conn = sqlite3.connect(DB_FILE)
    conn.execute("PRAGMA foreign_keys = ON")
    cursor = conn.cursor()
    
    # Create tables
    print("Creating tables...")
    cursor.executescript('''
        CREATE TABLE succulents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            image_url TEXT NOT NULL,
            description TEXT NOT NULL
        );

        CREATE TABLE care_tags (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            succulent_id INTEGER NOT NULL,
            tag TEXT NOT NULL,
            FOREIGN KEY (succulent_id) REFERENCES succulents (id)
        );
    ''')
    
    # Insert sample succulents
    print("Inserting sample succulents...")
    succulents = [
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
        ),
        (
            "Sempervivum Tectorum",
            "/api/placeholder/400/320",
            "Known as Hens and Chicks, this succulent forms rosettes that produce offsets around the mother plant."
        ),
        (
            "Aeonium Arboreum",
            "/api/placeholder/400/320",
            "The Tree Aeonium has spoon-shaped leaves arranged in rosettes at the ends of branching stems."
        ),
        (
            "Euphorbia Tirucalli",
            "/api/placeholder/400/320",
            "Commonly called Pencil Cactus or Firesticks, this succulent has pencil-thin, cylindrical stems."
        ),
        (
            "Gasteria Bicolor",
            "/api/placeholder/400/320",
            "Known for its thick, tongue-shaped leaves with white spots, making it an attractive houseplant."
        ),
        (
            "Lithops",
            "/api/placeholder/400/320",
            "Often called Living Stones, these small succulents have evolved to resemble pebbles as a form of camouflage."
        ),
        (
            "Senecio Rowleyanus",
            "/api/placeholder/400/320",
            "String of Pearls features trailing stems with small, spherical leaves resembling beads or pearls."
        ),
        (
            "Ceropegia Woodii",
            "/api/placeholder/400/320",
            "String of Hearts has heart-shaped leaves on thin, trailing stems, making it perfect for hanging baskets."
        ),
        (
            "Portulacaria Afra",
            "/api/placeholder/400/320",
            "Elephant Bush has small, round leaves on reddish-brown stems and is often used in bonsai."
        ),
        (
            "Cotyledon Orbiculata",
            "/api/placeholder/400/320",
            "Pig's Ear has thick, oval leaves with a powdery coating that gives them a silvery-blue appearance."
        )
    ]
    
    cursor.executemany(
        "INSERT INTO succulents (name, image_url, description) VALUES (?, ?, ?)",
        succulents
    )
    
    # Insert care tags
    print("Inserting care tags...")
    care_tags = [
        # Echeveria Elegans
        (1, "Low water"),
        (1, "Full sun"),
        (1, "Well-draining soil"),
        (1, "Frost sensitive"),
        
        # Haworthia Fasciata
        (2, "Partial shade"),
        (2, "Low water"),
        (2, "Indoor friendly"),
        (2, "Indirect light"),
        
        # Sedum Morganianum
        (3, "Bright indirect light"),
        (3, "Minimal water"),
        (3, "Hanging baskets"),
        (3, "Fragile stems"),
        
        # Crassula Ovata
        (4, "Bright light"),
        (4, "Low water"),
        (4, "Good for beginners"),
        (4, "Bonsai potential"),
        
        # Aloe Vera
        (5, "Bright indirect light"),
        (5, "Moderate water"),
        (5, "Medicinal"),
        (5, "Propagates easily"),
        
        # Kalanchoe Blossfeldiana
        (6, "Bright light"),
        (6, "Low water"),
        (6, "Flowering"),
        (6, "Frost sensitive"),
        
        # Sempervivum Tectorum
        (7, "Full sun"),
        (7, "Low water"),
        (7, "Cold hardy"),
        (7, "Ground cover"),
        
        # Aeonium Arboreum
        (8, "Partial sun"),
        (8, "Moderate water"),
        (8, "Summer dormant"),
        (8, "Branching"),
        
        # Euphorbia Tirucalli
        (9, "Full sun"),
        (9, "Minimal water"),
        (9, "Toxic sap"),
        (9, "Fast growing"),
        
        # Gasteria Bicolor
        (10, "Filtered light"),
        (10, "Low water"),
        (10, "Indoor friendly"),
        (10, "Slow growing"),
        
        # Lithops
        (11, "Bright light"),
        (11, "Very little water"),
        (11, "Gritty soil"),
        (11, "Unique appearance"),
        
        # Senecio Rowleyanus
        (12, "Bright indirect light"),
        (12, "Sparse watering"),
        (12, "Hanging plant"),
        (12, "Trailing stems"),
        
        # Ceropegia Woodii
        (13, "Medium light"),
        (13, "Allow to dry out"),
        (13, "Trailing"),
        (13, "Decorative"),
        
        # Portulacaria Afra
        (14, "Full to partial sun"),
        (14, "Low water"),
        (14, "Bonsai suitable"),
        (14, "Fast growing"),
        
        # Cotyledon Orbiculata
        (15, "Full sun"),
        (15, "Low water"),
        (15, "Drought tolerant"),
        (15, "Powdery leaves")
    ]
    
    cursor.executemany(
        "INSERT INTO care_tags (succulent_id, tag) VALUES (?, ?)",
        care_tags
    )
    
    # Commit changes and close connection
    conn.commit()
    conn.close()
    
    print(f"Test database '{DB_FILE}' created successfully with 15 succulents and their care tags.")
    print("You can now use this database for testing the FastAPI application.")

if __name__ == "__main__":
    create_test_database()

```

```python
import sqlite3
import os
import json

# Database file name
DB_FILE = 'succulents_test.db'

def check_database():
    """Check the contents of the test database and display them"""
    if not os.path.exists(DB_FILE):
        print(f"Error: Database file '{DB_FILE}' not found.")
        print("Please run create_test_db.py first to generate the test database.")
        return
    
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    # Get count of succulents
    cursor.execute("SELECT COUNT(*) FROM succulents")
    succulent_count = cursor.fetchone()[0]
    
    # Get count of care tags
    cursor.execute("SELECT COUNT(*) FROM care_tags")
    tag_count = cursor.fetchone()[0]
    
    print(f"Database '{DB_FILE}' contains {succulent_count} succulents and {tag_count} care tags.")
    
    # Get all succulents with their care tags
    cursor.execute("""
        SELECT s.id, s.name, s.image_url, s.description
        FROM succulents s
        ORDER BY s.name
    """)
    
    succulents = []
    for row in cursor.fetchall():
        # Get care tags for this succulent
        cursor.execute(
            "SELECT tag FROM care_tags WHERE succulent_id = ? ORDER BY tag",
            (row['id'],)
        )
        care_tags = [tag['tag'] for tag in cursor.fetchall()]
        
        succulents.append({
            'id': row['id'],
            'name': row['name'],
            'image': row['image_url'],
            'description': row['description'],
            'care': care_tags
        })
    
    # Print the first succulent as a sample
    print("\nSample succulent data:")
    print(json.dumps(succulents[0], indent=2))
    
    # Print all succulents names
    print("\nAll succulents in the database:")
    for i, succulent in enumerate(succulents, 1):
        print(f"{i}. {succulent['name']} ({len(succulent['care'])} care tags)")
    
    conn.close()

if __name__ == "__main__":
    check_database()

```

```python
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

```

I've created a complete set of tools for testing your succulent collection project with a sample SQLite database. Here's what each component does:

### 1. Create Test Database Script (`create_test_db.py`)

This script generates a comprehensive test database with 15 different succulents and their associated care tags:

- Creates a new SQLite database file named `succulents_test.db`
- Defines the schema with the `succulents` and `care_tags` tables
- Populates the database with a diverse collection of succulents, including:
  - Common varieties like Aloe Vera and Jade Plant
  - Unusual varieties like Living Stones and String of Pearls
  - Each succulent has 4 associated care tags

### 2. Database Verification Script (`check_db.py`) 

This utility script helps you verify the contents of the test database:

- Counts the number of succulents and care tags in the database
- Displays a sample succulent with all its data
- Lists all succulents in the database with their care tag counts

### 3. Updated FastAPI Application (`main.py`)

I've updated the FastAPI application to use the test database:

- Changed the database path to point to `succulents_test.db`
- Added error handling for when the database doesn't exist
- Included a new `/api/status` endpoint to verify database connectivity and get basic statistics

### How to Use These Files

1. **Set Up the Test Database**:
   ```
   python create_test_db.py
   ```
   This will create a new `succulents_test.db` file with 15 succulents and their care tags.

2. **Verify the Database Contents** (optional):
   ```
   python check_db.py
   ```
   This will display information about the database, including a list of all succulents.

3. **Run the FastAPI Application**:
   ```
   python main.py
   ```
   This will start the server using the test database.

4. **Access the Application**:
   - Web interface: http://localhost:8000/
   - API documentation: http://localhost:8000/docs
   - Status endpoint: http://localhost:8000/api/status

### Database Contents

The test database includes a wide variety of succulents:

1. Echeveria Elegans (Mexican Snowball)
2. Haworthia Fasciata (Zebra Plant)
3. Sedum Morganianum (Burro's Tail)
4. Crassula Ovata (Jade Plant)
5. Aloe Vera
6. Kalanchoe Blossfeldiana
7. Sempervivum Tectorum (Hens and Chicks)
8. Aeonium Arboreum (Tree Aeonium)
9. Euphorbia Tirucalli (Pencil Cactus)
10. Gasteria Bicolor
11. Lithops (Living Stones)
12. Senecio Rowleyanus (String of Pearls)
13. Ceropegia Woodii (String of Hearts)
14. Portulacaria Afra (Elephant Bush)
15. Cotyledon Orbiculata (Pig's Ear)

Each succulent has 4 unique care tags that provide useful information about their growing requirements.

Would you like me to make any adjustments to the test database or add any additional functionality to the project?

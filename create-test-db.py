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

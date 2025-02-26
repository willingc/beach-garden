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

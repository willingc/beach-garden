DROP TABLE IF EXISTS succulents;
DROP TABLE IF EXISTS care_tags;

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


products_query = """
CREATE TABLE IF NOT EXISTS products (
    id           SERIAL PRIMARY KEY,
    name         VARCHAR(128) NOT NULL,
    description  TEXT,
    price        INT,
    created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""
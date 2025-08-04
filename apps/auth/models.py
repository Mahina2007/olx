users_query = """
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY, 
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(128),
    password VARCHAR(128) NOT NULL,
    is_active BOOLEAN DEFAULT FALSE,
    is_login BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
"""
codes_query = """
CREATE TABLE IF NOT EXISTS codes (
    id SERIAL PRIMARY KEY, 
    code INTEGER,
    email VARCHAR(128)
    );
"""
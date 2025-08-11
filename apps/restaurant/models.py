kitchens_query = """
              CREATE TABLE IF NOT EXISTS kitchens
              (
                  id          SERIAL PRIMARY KEY,
                  name  VARCHAR(128) NOT NULL,
                  owner_id     INT NOT NULL REFERENCES users(id),
                  created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
              ) \
              """
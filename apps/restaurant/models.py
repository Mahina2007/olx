products_query = """
              CREATE TABLE IF NOT EXISTS products
              (
                  id          SERIAL PRIMARY KEY,
                  product_name  VARCHAR(128) NOT NULL,
                  price         VARCHAR(100) NOT NULL,
                  is_active   BOOLEAN   DEFAULT FALSE,
                  created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
              ) \
              """
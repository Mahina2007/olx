orders_query = """
              CREATE TABLE IF NOT EXISTS orders
              (
                  id          SERIAL PRIMARY KEY,
                  product       VARCHAR(128) NOT NULL,
                  is_active   BOOLEAN   DEFAULT FALSE,
                  created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
              ) \
              """

comments_query = """
                 CREATE TABLE IF NOT EXISTS comments
                 (
                     id         SERIAL PRIMARY KEY,
                     user_id    INTEGER REFERENCES restaurant (id),
                     post_id       INTEGER REFERENCES orders (id),
                     comment    TEXT NOT NULL,
                     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                 ) \
                 """

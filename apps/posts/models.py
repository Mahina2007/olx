posts_query = """
              CREATE TABLE IF NOT EXISTS posts
              (
                  id          SERIAL PRIMARY KEY,
                  title       VARCHAR(128) NOT NULL,
                  description TEXT         NOT NULL,
                  price       INTEGER      NOT NULL,
                  is_active   BOOLEAN   DEFAULT FALSE,
                  created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                  updated_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
              );
              """

comments_query = """
                 CREATE TABLE IF NOT EXISTS comments
                 (
                     id         SERIAL PRIMARY KEY,
                     user_id    INTEGER REFERENCES users (id),
                     post_id       INTEGER REFERENCES posts (id),
                     comment    TEXT NOT NULL,
                     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                 )
                 """
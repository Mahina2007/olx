restaurants_query = """
              CREATE TABLE IF NOT EXISTS restaurants
              (
                  id          SERIAL PRIMARY KEY,
                  name  VARCHAR(128) NOT NULL,
                  owner_id     INT NOT NULL REFERENCES users(id),
                  created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
              ) \
              """
couriers_query = """
              CREATE TABLE IF NOT EXISTS couriers
              (
                  id          SERIAL PRIMARY KEY,
                  name  VARCHAR(128) NOT NULL,
                  owner_id     INT NOT NULL REFERENCES users(id),
                  created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
              ) \
              """

users_query = """
              CREATE TYPE role_status as ENUM('courier', 'canteen', 'user');
              CREATE TABLE IF NOT EXISTS users
              (
                  id           SERIAL PRIMARY KEY,
                  full_name    VARCHAR(128) NOT NULL,
                  phone_number VARCHAR(13)  NOT NULL,
                  password     VARCHAR(128) NOT NULL,
                  role         role_status,
                  is_active    BOOLEAN   DEFAULT FALSE,
                  is_login     BOOLEAN   DEFAULT FALSE,
                  created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
              ) \
              """

verification_codes_query = """
                           CREATE TABLE IF NOT EXISTS codes
                           (
                               id           SERIAL PRIMARY KEY,
                               code         CHAR(4)     NOT NULL,
                               phone_number VARCHAR(13) NOT NULL,
                               created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                           ) \
                           """

foods_query = """
CREATE TABLE IF NOT EXISTS food_items (
    id           SERIAL PRIMARY KEY,
    kitchen_id   INT NOT NULL REFERENCES kitchens(id) ON DELETE CASCADE,
    name         VARCHAR(128) NOT NULL,
    description  TEXT,
    price        NUMERIC(10, 2) NOT NULL CHECK (price >= 0),
    created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

orders_query = """CREATE TYPE order_status AS ENUM ('pending', 'accepted', 'in_transit', 'delivered', 'cancelled');

CREATE TABLE IF NOT EXISTS orders (
    id            SERIAL PRIMARY KEY,
    customer_id   INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    kitchen_id    INT NOT NULL REFERENCES kitchens(id) ON DELETE CASCADE,
    courier_id    INT REFERENCES users(id) ON DELETE SET NULL,
    status          order_status NOT NULL DEFAULT 'pending',
    created_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);"""

ordering_query = """CREATE TABLE IF NOT EXISTS order_items (
    id          SERIAL PRIMARY KEY,
    order_id    INT NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
    food_id     INT NOT NULL REFERENCES food_items(id) ON DELETE CASCADE,
    quantity    INT NOT NULL CHECK (quantity > 0)
);"""
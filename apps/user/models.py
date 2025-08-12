
orders_query = """
CREATE TABLE IF NOT EXISTS orders (
    id             SERIAL PRIMARY KEY,
    status         VARCHAR(100) DEFAULT 'pending',
    created_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users(id),
    CONSTRAINT fk_restaurant_id FOREIGN KEY (restaurant_id) REFERENCES restaurants(id),
    CONSTRAINT fk_courier_id FOREIGN KEY (courier_id) REFERENCES users(id)
);

"""

order_products_query = """
CREATE TABLE IF NOT EXISTS order_products (
    id          SERIAL PRIMARY KEY,
    order_id    INT NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
    food_id     INT NOT NULL REFERENCES products(id) ON DELETE CASCADE,
    quantity    INT NOT NULL CHECK (quantity > 0)
);
"""
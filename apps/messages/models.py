messages_query = """
CREATE TABLE IF NOT EXISTS messages (
    id SERIAL PRIMARY KEY,
    from_user INTEGER REFERENCES users(id) ,
    to_user INTEGER REFERENCES users(id),
    message text not null,
    is_read boolean default false.
    created_at timestamp default current_timestamp,
    updated_at timestamp default current_timestamp
    );
"""
from core.database import execute_query


class MessageQueries:
    @staticmethod
    def update_messages_is_read(from_user, to_user) -> list | None:
        query = """UPDATE messages
                   SET is_read = TRUE
                   WHERE (from_user = %s AND to_user = %s)
                      OR (from_user = %s AND to_user = %s)"""
        params = (from_user, to_user, to_user, from_user,)
        execute_query(query=query, params=params)

    @staticmethod
    def get_all_user() -> list:
        query = "SELECT * FROM restaurant WHERE is_active = True"
        users = execute_query(query=query, fetch="all")
        return users if users else None

    @staticmethod
    def get_user_messages(from_user, to_user, is_read) -> list | None:
        query = """SELECT *
                   FROM messages
                   WHERE from_user = %s
                     AND to_user = %s
                     AND is_read = %s
                """
        params = (from_user, to_user, is_read,)
        users = execute_query(query=query, params=params, fetch="all")
        return users if users else []

    @staticmethod
    def get_all_user_messages(from_user, to_user) -> list | None:
        query = """SELECT *
                   FROM messages
                   WHERE (from_user = %s AND to_user = %s)
                      OR (from_user = %s AND to_user = %s)
                   ORDER BY created_at
                """
        params = (from_user, to_user, to_user, from_user,)
        all_messages = execute_query(query=query, params=params, fetch="all")
        return all_messages if all_messages else []

    @staticmethod
    def add_message(from_user, to_user, message) -> list | None:
        query = """INSERT INTO messages (from_user, to_user, message)
                   VALUES (%s, %s, %s)
                   RETURNING messages.id
                """
        params = (from_user, to_user, message,)
        message_id = execute_query(query=query, params=params, fetch="one")
        return message_id
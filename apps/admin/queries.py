from core.database import execute_query

admin_menu = """
1. Add a restaurant
2. Add a courier
3. Exit
"""
class AdminQueries:
    @staticmethod
    def add_restaurant(name, owner_id):
        """
        Insert a new kitchen into the database and return its ID.

        :param params: Tuple containing (name, owner_id)
        :return: int (new kitchen ID) or None if failed
        """
        try:
            query = """
                INSERT INTO restaurants(name, owner_id)
                VALUES (%s, %s);
            """
            params = (name, owner_id)
            execute_query(query=query, params=params)
        except Exception as e:
            print(f"Error inserting kitchen: {e}")
            return None

    @staticmethod
    def add_courier(name, owner_id):
        try:
            query = """
                INSERT INTO couriers(name, owner_id)
                VALUES( %s, %s);
        """
            params = (name, owner_id)
            execute_query(query=query, params=params)
        except Exception as e:
            print(f"Error: {e}")
            return None

    @staticmethod
    def courier_owner_exists(owner_id):
        try:
            query = "SELECT 1 FROM couriers WHERE owner_id = %s"
            params = (owner_id,)
            result = execute_query(query=query, params=params, fetch="one")
            return result is not None  # True if found, False if not
        except Exception as e:
            print(f"Error checking owner: {e}")
            return None


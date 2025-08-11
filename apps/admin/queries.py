from core.database import execute_query

admin_menu = """
1. Add a restaurant
2. Add a courier
3. Exit
"""
class AdminQueries():
    def add_kitchen(self, params: tuple):
        """
        Insert a new kitchen into the database and return its ID.

        :param params: Tuple containing (name, owner_id)
        :return: int (new kitchen ID) or None if failed
        """
        try:
            query = """
                INSERT INTO kitchens(name, owner_id)
                VALUES (%s, %s);
            """
            result = execute_query(query=query, params=params)
            if result:
                return result[0]
            return None
        except Exception as e:
            print(f"Error inserting kitchen: {e}")
            return None

    def add_courier(self, params: tuple):
        try:
            query = """
                INSERT INTO couriers(name, owner_id)
                VALUES( %s, %s)
                RETURNING id;
        """
            result = execute_query(query=query, params=params)
            if result:
                return result[0]
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None

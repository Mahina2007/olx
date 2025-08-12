from core.database import execute_query

restaurant_menu = """
1. Add product
2. Delete product
3. Accept order
4. Change status
5. Cancel order
6. Exit
"""
class RestaurantQueries:
    @staticmethod
    def add_products(name, description, price):
        try:
            query = """
                INSERT INTO products(name, description, price)
                VALUES (%s, %s, %s);
            """
            params = (name, description, price,)
            execute_query(query=query, params=params)
        except Exception as e:
            print(f"Error inserting kitchen: {e}")
            return None


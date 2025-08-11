from core.database import execute_query

admin_menu = """
1. Add a restaurant
2. Add a courier
3. Exit
"""
class AdminQueries():
    def add_restaurant(self):
        username = input("Enter restaurant username: ")
        password = input("Enter restaurant password: ")

        params = (username, password, 'restaurant')
        try:
            query = """
                        INSERT INTO users (username, password, role)
                        VALUES (%s, %s, %s)
                    """
            execute_query(query=query, params=params)
            print("Restaurant account created successfully!")
            return True
        except Exception as e:
            print(f"Error: {e}")
            return None

    def add_courier(self):
        pass

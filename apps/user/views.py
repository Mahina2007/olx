from apps.auth.queries import AuthQueries
from apps.restaurant.views import RestaurantViews
from core.database import execute_query

user_menu = """
1. Add an order
2. Delete an order
3. View history
4. Exit
"""

class UserViews(RestaurantViews, AuthQueries):
    def add_order(self):
        user = self.get_active_user()
        if not user:
            print("No active user logged in. Please log in first.")
            return

        user_id = user['id']
        try:
            # Step 1: Show available products
            self.show_products()

            # Step 2: Get product (food) ID and quantity
            food_id = int(input("Enter product (food) ID: ").strip())
            quantity = int(input("Enter quantity: ").strip())

            if quantity <= 0:
                print("Quantity must be greater than 0.")
                return

            product_query = "SELECT restaurant_id FROM products WHERE id = %s"
            product = execute_query(query=product_query, params=(food_id,), fetch="one")

            if not product:
                print("Invalid product selected.")
                return

            restaurant_id = product["restaurant_id"]
            courier_id = None  # No courier assigned yet
            status = 'pending'

            # Step 3: Create a new order for the current user
            # Assuming self.current_user_id exists (logged-in user)
            order_query = "INSERT INTO orders (user_id, restaurant_id, courier_id, status) VALUES (%s, %s, %s, %s) RETURNING id"
            params = (user_id, restaurant_id, courier_id, status)
            order_result = execute_query(query=order_query, params=params, fetch="one")

            if not order_result:
                print("Failed to create order.")
                return

            order_id = order_result["id"]
            # Step 4: Add product to order_products
            order_product_query = """
                INSERT INTO order_products (order_id, food_id, quantity)
                VALUES (%s, %s, %s)
            """
            execute_query(query=order_product_query, params=(order_id, food_id, quantity), fetch=None)

            print(f"✅ Order {order_id} created with {quantity}x product ID {food_id}.")

        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except Exception as e:
            print(f"Error adding order: {e}")




    def delete_order(self):
        pass

    def view_history(self):
        pass
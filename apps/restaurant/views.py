from apps.restaurant.queries import RestaurantQueries
from core.database import execute_query

class RestaurantViews(RestaurantQueries):
    def accept_order(self):
        order_id = input("Enter order ID to accept: ").strip()

        try:
            order_id = int(order_id)
        except ValueError:
            print("Order ID must be a number.")
            return

        # Check if order exists and is pending
        query_check = "SELECT status FROM orders WHERE id = %s"
        result = execute_query(query=query_check, params=(order_id,), fetch="one")

        if not result:
            print(f"No order found with ID {order_id}.")
            return

        if result["status"].lower() != "pending":
            print(f"Order {order_id} cannot be accepted because it is currently '{result['status']}'.")
            return

        # Update order status
        query_update = "UPDATE orders SET status = 'accepted' WHERE id = %s"
        execute_query(query=query_update, params=(order_id,), fetch=None)

        print(f"Order {order_id} has been accepted.")

    def cancel_order(self):
        pass

    def add_product(self):
        name = input("enter your product: ")
        description = input("enter your description: ")
        price = int(input("enter price: "))

        self.add_products(name, description, price)
        print(f"Food '{name}' is added")

    def show_products(self):
        try:
            query = "SELECT id, name, description, price FROM products"
            products = execute_query(query=query, fetch="all")  # fetch="all" should return a list of dicts or tuples

            if not products:
                print("No products found.")
                return

            print("=== Product List ===")
            for p_id, name, description, price in products:
                print(f"ID: {p_id} | Name: {name} | Description: {description} | Price: {price} so'm")

        except Exception as e:
            print(f"Error fetching products: {e}")

    def delete_product(self):
        self.show_products()
        id = int(input("enter id: "))
        try:
            query = """DELETE FROM products where id = %s """
            params = (id,)
            execute_query(query=query, params=params)
            print("Product is deleted")
        except Exception as e:
            print(e)
            return None
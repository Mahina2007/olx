from apps.orders.queries import OrdersQueries
from core.database import execute_query


user_menu = """
1. Add an order
2. Delete an order
3. Chat with courier
4. Exit
"""
class UserMenu(OrdersQueries):
    def add_order(self):
        order = input("enter your order: ")
        params = (order,)
        if self.add_orders(params):
            print("order added successfully!")
            return True
        else:
            print("try again")
            return None

    def delete_order(self):
        id = int(input("enter your order's id: "))

        if not self.order_exists(id):
            print("order doesn't exist")
            return None

        if self.delete_orders(id):
            print("your order is deleted")
            return True
        else:
            print("try again")
            return None
















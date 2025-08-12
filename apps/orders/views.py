from apps.orders.queries import OrdersQueries
from apps.user.views import UserViews
from core.database import execute_query

class UserMenu(OrdersQueries, UserViews):
    def add_order(self):
        self.show_products()

        order = input("enter your order id: ")
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
















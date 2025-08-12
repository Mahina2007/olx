from apps.admin.queries import AdminQueries
from core.database import execute_query


class AdminView(AdminQueries):
    def add_restaurants(self):
        name = input("Enter restaurant name: ").strip()
        owner_id = input("Enter owner user ID: ").strip()
        try:
            owner_id = int(owner_id)
        except ValueError:
            print("Owner ID must be a number.")
            return
        self.add_restaurant(name, owner_id)
        print(f"Restaurant '{name}' added for owner ID {owner_id}.")

    def add_couriers(self):
        name = input("Enter courier name: ").strip()
        owner_id = input("Enter owner user ID: ").strip()
        try:
            owner_id = int(owner_id)
        except ValueError:
            print("Owner ID must be a number.")
            return

        if self.courier_owner_exists(owner_id):
            print(f"Owner ID {owner_id} already has a courier assigned.")
            return False

        self.add_courier(name, owner_id)
        print(f"Courier '{name}' added for owner ID {owner_id}.")





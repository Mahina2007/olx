from apps.admin.models import kitchens_query, couriers_query
from core.database import execute_query

main_menu = """
1. Register
2. Login
3. Exit
"""




def get_user_option(menu: str, max_option: int) -> str:
    while True:
        print(menu)
        option = input("Enter your option: ")
        if not (1 <= int(option) <= max_option):
            print("Invalid option number!")
        else:
            return option


def execute_tables():
    from apps.auth.models import users_query, verification_codes_query
    from apps.orders.models import orders_query

    execute_query(query=users_query)
    execute_query(query=verification_codes_query)
    execute_query(query=orders_query)
    execute_query(query=kitchens_query)
    execute_query(query=couriers_query)

from apps.admin.models import restaurants_query, couriers_query
from apps.restaurant.models import products_query
from core.database import execute_query

main_menu = """
1. Register
2. Login
3. Exit
"""




def get_user_option(menu: str, max_option: int) -> str:
    while True:
        print(menu)
        option = input("Enter your option: ").strip().lower()
        
        if option == "exit":
            return "exit"
        
        if option.isdigit() and 1 <= int(option) <= max_option:
            return option
        
        print("Invalid option! Please enter a number or 'exit'.")


def execute_tables():
    from apps.auth.models import users_query, verification_codes_query
    from apps.user.models import orders_query
    from apps.user.models import order_products_query

    execute_query(query=users_query)
    execute_query(query=verification_codes_query)
    execute_query(query=orders_query)
    execute_query(query=restaurants_query)
    execute_query(query=couriers_query)
    execute_query(query=products_query)
    execute_query(query=order_products_query)


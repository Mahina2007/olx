from apps.auth.models import codes_query
from core.database import execute_query

main_menu = """
1. Show products
2. Register
3. Login
4. Exit
"""



def get_user_option(menu: str, max_option: int):
    print(menu)
    option = input("Enter your option: ")
    if not (1 <= int(option) <= max_option):
        print("Invalid option number!")
        get_user_option(menu, max_option)
    return option

def execute_tables():
    from apps.auth.models import users_query, codes_query
    from apps.messages.models import messages_query
    from apps.posts.models import posts_query, comments_query

    execute_query(query=users_query)
    execute_query(query=codes_query)
    # execute_query(query=messages_query)
    # execute_query(query=posts_query)
    # execute_query(query=comments_query)
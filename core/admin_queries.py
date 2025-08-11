from core.database import execute_query

def view_users():
    try:
        query = "SELECT COUNT(*) AS users_number FROM restaurant"
        result = execute_query(query=query, fetch="one")
        print(f"Total restaurant: {result['users_number']}")
        return result['users_number']
    except Exception as e:
        print(e)
        return None

def view_active_users():
    try:
        query = "SELECT count(*) as active_users FROM restaurant WHERE is_active = true "
        result = execute_query(query=query, fetch="one")
        print(f"Active restaurant: {result['active_users']}")
        return result['active_users']
    except Exception as e:
        print(e)
        return False




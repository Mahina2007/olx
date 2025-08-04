from core.database import execute_query


def get_active_user() -> dict | None:
    """
    get current is_login user from database
    if not exists return None
    :return:
    """
    query = "SELECT * FROM users WHERE is_login = %s"
    params = (True,)

    user = execute_query(query=query, params=params, fetch="one")
    return user if user else None
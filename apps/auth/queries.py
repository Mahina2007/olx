from core.database import execute_query

class AuthQueries:
    @staticmethod
    def get_user_by_phone_number(phone_number) -> dict | None:
        query = "SELECT * FROM users WHERE phone_number = %s"
        params = (phone_number,)

        user = execute_query(query=query, params=params, fetch="one")
        return user if user else None

    @staticmethod
    def update_user_is_login(phone_number) -> dict | bool:
        query = "UPDATE users SET is_login = %s WHERE phone_number = %s"
        params = (True, phone_number,)
        execute_query(query=query, params=params)
        return True

    @staticmethod
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


    @staticmethod
    def add_user(params: tuple) -> None | bool:
        try:
            query = """INSERT INTO users (full_name, phone_number, password, role)
                    VALUES (%s, %s, %s, %s)
                    """
            execute_query(query=query, params=params)
            return True
        except Exception as e:
            print(e)
            return None


    @staticmethod
    def get_verification_code(phone_number, code) -> dict | None:
        try:
            query = "SELECT * FROM codes WHERE phone_number = %s AND code = %s"
            params = (phone_number, code,)

            verification_code = execute_query(query=query, params=params, fetch="one")
            return verification_code if verification_code else None
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def add_code(phone_number, code) -> None | bool:
        try:
            query = """INSERT INTO codes (phone_number, code)
                       VALUES (%s, %s)
                    """
            params = (phone_number, code,)
            execute_query(query=query, params=params)
            return True
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def update_user_status(status, phone_number) -> None | bool:
        try:
            query = "UPDATE users SET is_active = %s WHERE phone_number = %s"
            params = (status, phone_number,)
            execute_query(query=query, params=params)
            return True
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def logout_all_users() -> None | bool:
        try:
            query = "UPDATE users SET is_login = False"
            execute_query(query=query)
            return True
        except Exception as e:
            print(e)
            return None




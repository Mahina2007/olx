from core.database import execute_query

class OrdersQueries:
    def add_orders(self, params: tuple) -> None | bool:
        try:
            query = """INSERT INTO orders (product)
                       VALUES (%s)
                    """

            execute_query(query=query, params=params)
            return True
        except Exception as e:
            print(e)
            return None

    def delete_orders(self, order_id: int):
        try:
            query = """DELETE FROM orders where id = %s """
            params = (order_id,)
            execute_query(query=query, params=params)
            return True
        except Exception as e:
            print(e)
            return None

    def order_exists(self, id: int) -> bool:
        try:
            query = "SELECT id FROM orders WHERE id = %s"
            params = (id,)
            result = execute_query(query=query, params=params, fetch="one")
            return result is not None
        except Exception as e:
            print(e)
            return False

    def update_posts(self,params: tuple) -> bool:
        try:
            query = "UPDATE orders SET title = %s, description = %s, price = %s WHERE id = %s"
            execute_query(query=query, params=params)
            return True
        except Exception as e:
            print(e)
            return False





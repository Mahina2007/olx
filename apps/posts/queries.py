from core.database import execute_query

class PostsQueries:
    def add_posts(self, params: tuple) -> None | bool:
        try:
            query = """INSERT INTO posts (title, description, price)
                       VALUES (%s, %s, %s)
                    """

            execute_query(query=query, params=params)
            return True
        except Exception as e:
            print(e)
            return None

    def delete_posts(self, post_id: int):
        try:
            query = """DELETE FROM posts where id = %s """
            params = (post_id,)
            execute_query(query=query, params=params)
            return True
        except Exception as e:
            print(e)
            return None

    def post_exists(self, id: int) -> bool:
        try:
            query = "SELECT id FROM posts WHERE id = %s"
            params = (id,)
            result = execute_query(query=query, params=params, fetch="one")
            return result is not None
        except Exception as e:
            print(e)
            return False

    def update_posts(self,params: tuple) -> bool:
        try:
            query = "UPDATE posts SET title = %s, description = %s, price = %s WHERE id = %s"
            execute_query(query=query, params=params)
            return True
        except Exception as e:
            print(e)
            return False





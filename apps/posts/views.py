from operator import is_not

from apps.posts.queries import PostsQueries
from core.database import execute_query


user_menu = """
1. Add a post
2. Delete a post
3. Update a post
4. Exit
"""
class UserMenu(PostsQueries):
    def add_post(self):
        title = input("enter your title: ")
        description = input("enter description: ")
        price = int(input("enter price: "))

        params = (title, description, price,)
        if self.add_posts(params):
            print("post added successfully!")
            return True
        else:
            print("try again")
            return None

    def delete_post(self):
        id = int(input("enter your post's id: "))

        if not self.post_exists(id):
            print("post doesn't exist")
            return None

        if self.delete_posts(id):
            print("your post is deleted")
            return True
        else:
            print("try again")
            return None

    def update_post(self):
        id = int(input("enter your post's id: "))

        if not self.post_exists(id):
            print("post doesn't exist")
            return None

        title = input("enter new title: ")
        description = input("enter new description: ")
        try:
            price = int(input("enter new price: "))
        except ValueError as e:
            print(e)

        params = (title, description, price, id)
        if self.update_posts(params):
            print("post is successfully updated")
        else:
            print("something went wrong")















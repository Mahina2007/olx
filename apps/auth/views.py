import psycopg2
from psycopg2.extras import DictCursor
from core.database import *
from datetime import datetime
from apps.auth.utils import *

admin_email = "a"
admin_password = "a"

class RegisterView:
    def send_code(self):
        pass

    def check_code(self):
        user_code = input("Code: ")

        try:
            conn = get_db_conn()
            cursor = conn.cursor(cursor_factory=DictCursor)

            cursor.execute("SELECT email FROM codes WHERE code = %s;", (user_code,))
            result = cursor.fetchone()

            if result is None:
                print("Invalid code")
                cursor.close()
                conn.close()
                return self.check_code()

            email = result["email"]
            cursor.execute("UPDATE users SET is_active = TRUE WHERE email = %s RETURNING id;", (email,))
            updated = cursor.fetchone()

            conn.commit()
            cursor.close()
            conn.close()

            if updated:
                print("User activated successfully")
                return True
            else:
                print("User with this email not found")
                return False

        except psycopg2.OperationalError as e:
            print(e)
            print("Something went wrong")
            return None

    def register(self):
        full_name = input("Enter your full name: ")
        email = input("Enter your email: ")
        password1 = input("Enter your password: ")
        password2 = input("Confirm your password: ")

        while password1 != password2:
            print("Doesnt not match")
            password1 = input("Enter your password: ")
            password2 = input("Confirm your password: ")

        try:
            conn = get_db_conn()
            cursor = conn.cursor(cursor_factory=DictCursor)
            query = "INSERT INTO users (full_name, email, password, is_active, is_login, created_at) VALUES (%s, %s, %s, %s, %s, %s )"
            params = (full_name, email, password2, False, False, datetime.now())
            cursor.execute(query, params)

            random_code = get_random_code(email=email)
            cursor.execute(
                "INSERT INTO codes (code, email) VALUES (%s, %s);",
                (random_code, email))
            conn.commit()
            print("you are logged in successfully!")
            cursor.close()
            conn.close()

            send_mail(receiver_email=email, body=str(random_code))
            return self.check_code()

        except psycopg2.OperationalError as e:
            print(e)
            print("Something went wrong")
            return None


class LoginView:
    def login(self):
        email = input("your email: ")
        password = input("Enter your password: ")
        if email == admin_email and password == admin_password:
            return "admin"
        try:
            conn = get_db_conn()
            cursor = conn.cursor(cursor_factory=DictCursor)
            query = "SELECT id from users where email = %s and password = %s;"
            params = (email, password)
            cursor.execute(query, params)
            users = cursor.fetchone()
            if users:
                cursor.execute("update users set is_login = true where email = %s;", (email,))
                print("you are log in!")
                conn.commit()
                cursor.close()
                conn.close()
                return "users"
            else:
                print("Invalid username or password")
                cursor.close()
                conn.close()
                return False

        except psycopg2.Error as e:
            print("Database error:", e)
            return False


class Logout:
    def logout(self):
        pass
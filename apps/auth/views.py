import random

from twilio.rest import Client

from apps.admin.queries import admin_menu
from apps.auth.queries import AuthQueries
from apps.auth.utils import  main_menu
from apps.user.views import user_menu
from core.config import AUTH_TOKEN, ACCOUNT_SID


class RegisterView( AuthQueries):
    def verify_code(self):
        phone_number = input("Enter your phone number: ")
        code = input("Enter your verification code: ")

        verification_code = self.get_verification_code(phone_number, code)
        if not verification_code:
            print("Invalid code")
            return self.verify_code()
        else:
          
            self.update_user_status(True, phone_number)
            print("You can login now")
            return True

    def generate_code(self, phone_number):
        while True:
            random_code = str(random.randint(1000, 9999))
            verification_code = self.get_verification_code(phone_number, random_code)
            if not verification_code:
                self.add_code(phone_number, random_code)
                return random_code

    def send_code(self, phone_number):
        twilio_number = '+13202447896'
        to_number = '+821053730692'
        try:
            client = Client(ACCOUNT_SID, AUTH_TOKEN)
            code = self.generate_code(phone_number)

            client.messages.create(
                body=f"Hello! This is your Olx_n68 account verification code: {code}",
                from_=twilio_number,
                to=to_number
            )

            print("Please check your messages and enter code: ")
            return self.verify_code()
        except Exception as e:
            print(f"Something went wrong!!: {e}")
            return None

    def register(self):
        full_name = input("Enter your full name: ")
        phone_number = input("Enter your phone number: ")
        password1 = input("Enter your password: ")
        password2 = input("Confirm your password: ")


        while not self.check_phone_number(phone_number):
            phone_number = input("Enter your phone number: ")

        while not self.check_password(password1, password2):
            password1 = input("Enter your password: ")
            password2 = input("Confirm your password: ")
        role_map = {
            "1": 'Admin',
            "2": 'User',
            "3": 'Courier',
            "4": 'Canteen',
            "5": 'Back'
        }
        role_choice = input("""
                Choose your role:
                1. Admin
                2. User
                3. Courier
                4. Canteen
                5. Back
                """).strip()

        if role_choice == "5":
            return main_menu()
        elif role_choice not in role_map:
            print("Invalid role choice.")
            return self.register()

        role = role_map[role_choice]

        params = (full_name, phone_number, password1, role)
        if self.add_user(params):
            return self.send_code(phone_number)
        else:
            print("Something get wrong, please try again later")
            return None

    def check_phone_number(self, phone_number):
        if phone_number.startswith('+') and phone_number[1:].isdigit() and 10 <= len(phone_number[1:]) <= 15:
            return True
        return False

    def check_password(self, password1, password2):
        if password1 != password2:
            return False
        return True


class LoginView(AuthQueries):
    def __init__(self):
        self.admin_phone_number = "a"
        self.admin_password = "a"

    def login(self):
        phone_number = input("Enter your phone number: ")
        password = input("Enter your password: ")
        user = self.get_user_by_phone_number(phone_number)
        if phone_number == self.admin_phone_number and password == self.admin_password:
            print("Welcome, Admin!")
            return "admin"

        user = self.get_user_by_phone_number(phone_number)
        if not user:
            print("No account found with that phone number.")
            return None

        if user and user['password'] == password:
            self.update_user_is_login(phone_number=phone_number)
            print(f"Welcome, {user['full_name']}")
            return "user"
        print("Incorrect password")


class LogoutView(AuthQueries):
    def logout_all(self):
        self.logout_all_users()

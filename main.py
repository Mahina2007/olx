from apps.auth.queries import get_active_user
from core.utils import *
from apps.auth.views import *
from apps.auth.models import *


class Menu:
    @staticmethod
    def main_menu():
        r = RegisterView()
        l = LoginView()
        option = get_user_option(menu=main_menu, max_option=4)

        if option == '1':
            pass
        elif option == '2':
            r.register()
        elif option == '3':
            l.login()
        elif option == '4':
            print("Goodbye!")
            return
        else:
            print("Invalid option. Please try again.")

    def user_menu(self):
        pass

    def admin_menu(self):
        pass


if __name__ == '__main__':
    execute_tables()
    Menu.main_menu()
import logging

from apps.admin.queries import AdminQueries, admin_menu
from apps.auth.views import RegisterView, LogoutView, LoginView
from core.admin_queries import view_users, view_active_users
from core.utils import *
from apps.orders.views import *

logging.basicConfig(level=logging.INFO, filename='logs.log')
logger = logging.getLogger(__name__)


class Menu:
    def main_menu(self):
        option = get_user_option(menu=main_menu, max_option=3)
        if option == "1":
            result = RegisterView().register()
            self.main_menu()
            if not result:
                print("Something get wrong, try again later")
        elif option == "2":
            user = LoginView().login()
            if user == "user":
                pass
            elif user == "admin":
                return self.admin_menu()
            else:
                print("Invalid phone number or password")
                return self.main_menu()
        else:
            print("Goodbye!")
            return None


    # def user_menu(self):
    #     option = get_user_option(menu=user_menu, max_option=4)
    #     if option == "1":
    #         UserMenu().add_order()
    #         return Menu().user_menu()
    #     elif option == "2":
    #         UserMenu().delete_order()
    #         return Menu().user_menu()
    #     elif option == "3":
    #         if MessageView().show_all_users():
    #             MessageView().send_message()
    #         return self.user_menu()
    #     elif option == "4":
    #         LogoutView().logout_all()
    #         return self.main_menu()

    def admin_menu(self):
        option = get_user_option(menu=admin_menu, max_option=3)
        if option == "1":
            AdminQueries.add_kitchen()
            self.admin_menu()
        elif option == "2":
            AdminQueries.add_courier()
            self.admin_menu()
        elif option == "3":
            LogoutView().logout_all()
            return self.main_menu()

if __name__ == '__main__':
    execute_tables()
    LogoutView.logout_all_users()
    Menu().main_menu()

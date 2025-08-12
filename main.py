import logging

from apps.admin.queries import AdminQueries, admin_menu
from apps.admin.views import AdminView
from apps.auth.views import RegisterView, LogoutView, LoginView
from apps.auth.utils import *
from apps.orders.views import UserMenu
from apps.restaurant.queries import restaurant_menu
from apps.restaurant.views import RestaurantViews
from apps.user.views import user_menu, UserViews

logging.basicConfig(level=logging.INFO, filename='logs.log')
logger = logging.getLogger(__name__)


class Menu:
    def main_menu(self):
        while True:
            option = get_user_option(menu=main_menu, max_option=3)
            if option == "exit" or option == "3":
                print("Goodbye!")
                break
            if option == "1":
                result = RegisterView().register()
                if not result:
                    print("Something went wrong, try again later")
                continue

            if option == "2":
                user = LoginView().login()
                if user == "user":
                    self.user_menu()
                elif user == "admin":
                    self.admin_menu()
                else:
                    print("Invalid phone number or password")



    def user_menu(self):
        option = get_user_option(menu=user_menu, max_option=4)
        if option == "1":
            UserViews().add_order()
            return Menu().user_menu()
        elif option == "2":
            UserMenu().delete_order()
            return Menu().user_menu()
        elif option == "3":
            pass
            return self.user_menu()
        elif option == "4":
            LogoutView().logout_all()
            return self.main_menu()

    def admin_menu(self):
        option = get_user_option(menu=admin_menu, max_option=6)
        if option == "1":
            AdminView().add_restaurants()
            return self.admin_menu()
        elif option == "2":
            AdminView().add_couriers()
            self.admin_menu()
        elif option == "3":
            LogoutView().logout_all()
            return self.main_menu()
        return self.admin_menu()

    def restaurants_menu(self):
        option = get_user_option(menu=restaurant_menu, max_option=3)
        if option == "1":
            RestaurantViews().add_product()
            return self.restaurants_menu()
        elif option == "2":
            RestaurantViews().delete_product()
            return self.restaurants_menu()
        elif option == "3":
            LogoutView().logout_all()
            return self.main_menu()
        return self.admin_menu()


if __name__ == '__main__':
    execute_tables()
    LogoutView.logout_all_users()
    Menu().main_menu()
    # Menu().user_menu()
    # # Menu().restaurants_menu()
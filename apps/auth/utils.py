class AuthValidation:
    def __init__(self):
        self.errors = []

    def check_phone_number(self, phone_number):
        if phone_number.startswith('+') and phone_number[1:].isdigit() and 10 <= len(phone_number[1:]) <= 15:
            return True
        return False

    def check_password(self, password1, password2):
        if password1 != password2:
            return False
        return True

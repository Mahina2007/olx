from apps.auth.queries import AuthQueries
from apps.messages.queries import MessageQueries


class MessageView(MessageQueries, AuthQueries):
    def __init__(self):
        self.current_user = self.get_active_user()
        self.user_id = None

    def show_all_users(self):
        users = self.get_all_user()
        if not users:
            print("There is no user to chat with")
            return None
        for user in users:
            user_messages_count = len(self.get_user_messages(
                from_user=user['id'], to_user=self.current_user['id'],
                is_read=False
            ))
            print(f"ID: {user['id']} | {user['full_name']} ({user_messages_count})")
        return True

    def user_chat_history(self, user_id):
        all_messages = self.get_all_user_messages(
            from_user=user_id, to_user=self.current_user['id']
        )
        if not all_messages:
            print("There is no messages yet")
        else:
            for message in all_messages:
                terminal_width = 80  # Adjust based on your terminal size
                if message['from_user'] == self.current_user['id']:
                    # Right-align the message
                    print(f"{message['message']:>{terminal_width}}")
                else:
                    # Left-align the message
                    print(f"{message['message']}")

    def send_message(self):
        if self.user_id is None:
            user_id = input("Enter user ID: ")
            self.user_id = user_id
            self.update_messages_is_read(
                from_user=self.current_user['id'],
                to_user=self.user_id
            )

        self.user_chat_history(self.user_id)

        message = input("Enter message or None to leave: ").strip()

        if message == "":
            return True
        else:
            if self.add_message(
                    from_user=self.current_user['id'],
                    to_user=self.user_id,
                    message=message
            ):
                return self.send_message()
            else:
                print("Something went wrong, try again later")
                return True
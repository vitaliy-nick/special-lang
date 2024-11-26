from tabulate import tabulate
from Classes.api_repository import APIRepository
from Classes.data_factory import DataFactory
from Classes.history_manager import HistoryManager
from Classes.deleter import Deleter
from Classes.adder import Adder
from Lab7.Classes.file_manager import DataSaver


class ConsoleApp:
    def __init__(self):
        self.api_repository = APIRepository()
        self.local_users = []
        self.local_posts = []
        self.history_manager = HistoryManager()
        self.deleter = Deleter(self.local_users, self.local_posts, self.history_manager)
        self.adder = Adder(self.api_repository, self.local_users, self.local_posts, self.history_manager)

    def show_users(self):
        users_data = self.api_repository.get_users()
        users = [DataFactory.create_user(user) for user in users_data]
        users.extend(self.local_users)
        table = [[user.user_id, user.name, user.email] for user in users]
        print(tabulate(table, headers=["ID", "Name", "Email"], tablefmt="grid"))
        self.history_manager.log("Show users", "All users.")

    def show_posts(self):
        posts_data = self.api_repository.get_posts()
        posts = [DataFactory.create_post(post) for post in posts_data]
        posts.extend(self.local_posts)
        table = [[post.post_id, post.title, post.body, post.user_id] for post in posts]
        print(tabulate(table, headers=["ID", "Title", "Text", "User ID"], tablefmt="grid"))
        self.history_manager.log("Show posts", "All posts.")

    def add_user(self):
        name = input("Enter name for new user: ")
        email = input("Enter Email for new user: ")
        self.adder.add_user(name, email)

    def add_post(self):
        title = input("Enter title: ")
        body = input("Enter text: ")
        user_id = int(input("Enter user ID: "))
        self.adder.add_post(title, body, user_id)

    def delete_user(self):
        user_id = int(input("Enter user ID for deletion: "))
        self.deleter.delete_user(user_id)

    def delete_post(self):
        post_id = int(input("Enter post ID for deletion: "))
        self.deleter.delete_post(post_id)

    def save_users(self):
        users_data = self.api_repository.get_users()
        users = [DataFactory.create_user(user) for user in users_data]
        users.extend(self.local_users)
        data = [user.__dict__ for user in users]
        DataSaver.select_save_format(data, "users")

    def save_posts(self):
        posts_data = self.api_repository.get_posts()
        posts = [DataFactory.create_post(post) for post in posts_data]
        posts.extend(self.local_posts)
        data = [post.__dict__ for post in posts]
        DataSaver.select_save_format(data, "posts")

    def show_history(self):
        self.history_manager.show_history()
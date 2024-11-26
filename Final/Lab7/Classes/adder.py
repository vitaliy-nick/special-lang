from Classes.data_factory import DataFactory

class Adder:
    def __init__(self, api_repository, local_users, local_posts, history_manager):
        self.api_repository = api_repository
        self.local_users = local_users
        self.local_posts = local_posts
        self.history_manager = history_manager

    def add_user(self, name, email):
        user_data = self.api_repository.add_user(name, email)
        new_user = DataFactory.create_user(user_data)
        self.local_users.append(new_user)
        self.history_manager.log("Add user", f"User {name} ({email}) added.")
        print("New user added:", user_data)

    def add_post(self, title, body, user_id):
        post_data = self.api_repository.add_post(title, body, user_id)
        new_post = DataFactory.create_post(post_data)
        self.local_posts.append(new_post)
        self.history_manager.log("Add post", f"Post {title} added.")
        print("New post added:", post_data)

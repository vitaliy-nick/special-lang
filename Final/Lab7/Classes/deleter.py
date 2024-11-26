class Deleter:
    def __init__(self, local_users, local_posts, history_manager):
        self.local_users = local_users
        self.local_posts = local_posts
        self.history_manager = history_manager

    def delete_user(self, user_id):
        for user in self.local_users:
            if user.user_id == user_id:
                self.local_users.remove(user)
                self.history_manager.log("Delete user", f"User with ID {user_id} was deleted.")
                print(f"User with ID {user_id} was deleted.")
                return
        print(f"Error: User with ID {user_id} is not found.")

    def delete_post(self, post_id):
        for post in self.local_posts:
            if post.post_id == post_id:
                self.local_posts.remove(post)
                self.history_manager.log("Delete post", f"Post with ID {post_id} was deleted.")
                print(f"Post with ID {post_id} was deleted.")
                return
        print(f"Error: Post with ID {post_id} is not found.")

import os
import sys

lab7_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(lab7_root)

from Classes.console_app import ConsoleApp

def main():
    app = ConsoleApp()

    while True:
        print("\nMain menu:")
        print("1. Show users.")
        print("2. Show posts.")
        print("3. Add new user.")
        print("4. Add new post.")
        print("5. Delete user.")
        print("6. Delete post.")
        print("7. Save users.")
        print("8. Save posts.")
        print("9. Show history.")
        print("0. Exit.")
        choice = input("Select option: ")

        match choice:
            case "1":
                app.show_users()
            case "2":
                app.show_posts()
            case "3":
                app.add_user()
            case "4":
                app.add_post()
            case "5":
                app.delete_user()
            case "6":
                app.delete_post()
            case "7":
                app.save_users()
            case "8":
                app.save_posts()
            case "9":
                app.show_history()
            case "0":
                print("Exit!")
                break
            case _:
                print("Error: Incorrect option! Please, try again!")

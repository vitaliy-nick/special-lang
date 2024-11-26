from Lab9.facade import RunnerFacade


def main():
    facade = RunnerFacade()
    while True:
        facade.show_menu()
        try:
            choice = int(input("Select program: "))
            if choice == 0:
                print("Exit from final program!")
                break
            facade.run_lab(choice)
        except ValueError:
            print("Error: Incorrect option! Please, try again!")

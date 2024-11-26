from classes import Calculator

def main():
    try:
        calc = Calculator()
    except TypeError as e:
        print(e)
        exit(1)

    while True:
        print("\nCalculator")
        print("1. Perform calculations.")
        print("2. Show history.")
        print("3. Get result from memory.")
        print("4. Clean memory.")
        print("5. Change the number of symbols after the decimal point.")
        print("6. Exit.")

        choice = input("Select option: ")

        match choice:
            case '1':
                try:
                    calc.calculate()
                except ZeroDivisionError as e:
                    print(e)
                except ValueError as e:
                    print(e)
            case '2':
                calc.history.show_history()
            case '3':
                print(f"Saved value: {calc.memory.get_memory()}")
            case '4':
                calc.memory.clear_memory()
                print("Saved value cleared.")
            case '5':
                try:
                    calc.settings.set_decimal_places()
                except ValueError as e:
                    print(e)
                except TypeError as e:
                    print(e)
            case '6':
                print("Exit from calculator.")
                break
            case _:
                print("Wrong choice! Please try again!")

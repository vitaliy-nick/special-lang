from Lab1.runner import main as lab1
from Lab2.interface import main as lab2
from Lab3.UI.user_interface import main as lab3
from Lab4.UI.user_interface import main as lab4
from Lab5.UI.user_interface import user_interface as lab5
from Lab6.run_tests_with_coverage import main as lab6
from Lab7.UI.user_interface import main as lab7
from Lab8.UI.user_interface import main as lab8


class RunnerFacade:
    def __init__(self):
        self.labs = {
            1: self.run_lab1,
            2: self.run_lab2,
            3: self.run_lab3,
            4: self.run_lab4,
            5: self.run_lab5,
            6: self.run_lab6,
            7: self.run_lab7,
            8: self.run_lab8,
        }

    def show_menu(self):
        print("\nAll programs:")
        for lab_number in sorted(self.labs.keys()):
            print(f"{lab_number}: Program {lab_number}.")
        print("0: Exit.")

    def run_lab(self, choice):
        if choice in self.labs:
            print(f"Starting program {choice}...")
            self.labs[choice]()
        elif choice == 0:
            print("Exit!")
        else:
            print("Error: Incorrect option! Please, try again!")

    def run_lab1(self):
        lab1()

    def run_lab2(self):
        lab2()

    def run_lab3(self):
        lab3()

    def run_lab4(self):
        lab4()

    def run_lab5(self):
        lab5()

    def run_lab6(self):
        lab6()

    def run_lab7(self):
        lab7()

    def run_lab8(self):
        lab8()

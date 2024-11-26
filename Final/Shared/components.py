import math
from abc import ABC, abstractmethod

memory = 0
history = []
decimal_places = 2


class Memory:
    def __init__(self):
        self.__memory = memory

    def set_memory(self, value):
        self.__memory = value

    def get_memory(self):
        return self.__memory

    def clear_memory(self):
        self.__memory = 0


class History:
    def __init__(self):
        self.__history = history

    def add_to_history(self, expression, result):
        self.__history.append(f"{expression} = {result}")

    def show_history(self):
        if self.__history:
            print("History of calculations:")
            for entry in self.__history:
                print(entry)
        else:
            print("History is empty.")


class Settings:
    def __init__(self):
        self.__decimal_places = decimal_places

    def set_decimal_places(self):
        places = input("Enter the number of symbols after the decimal point: ")
        if places.isalpha():
            raise places("Please, enter a positive integer!")
        elif int(places) >= 0:
            self.__decimal_places = int(places)
            print(f"Number of symbols after decimal point - {self.__decimal_places}.")
        else:
            raise ValueError("Please, try again. Number of symbols must not be negated!")

    def get_decimal_places(self):
        return self.__decimal_places


class BaseCalculator(ABC):
    def __init__(self):
        self.memory = Memory()
        self.history = History()
        self.settings = Settings()

    def get_input(self):
        try:
            num1_input = input("Enter first number or 'm' for use value from memory: ")
            num1 = self.memory.get_memory() if num1_input.lower() == 'm' else float(num1_input)
            operator = self.get_operator()

            num2 = None
            if operator != '√':
                while True:
                    try:
                        num2_input = input("Enter second number or 'm' for use value from memory: ")
                        num2 = self.memory.get_memory() if num2_input.lower() == 'm' else float(num2_input)
                        break
                    except ValueError:
                        print("Incorrect input! Please, try again!")
            return num1, operator, num2
        except ValueError:
            print("Incorrect input! Please, try again!")
            return self.get_input()

    def check_operator(self, operator):
        return operator in ['+', '-', '*', '/', '^', '√', '%']

    def get_operator(self):
        while True:
            operator = input("Choose one of the operators (+, -, *, /, ^, √, %): ")
            if self.check_operator(operator):
                return operator
            else:
                print("Incorrect operator! Please, try again!")

    @abstractmethod
    def perform_operators(self, num1, operator, num2):
        pass

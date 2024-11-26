import math
from abc import ABC, abstractmethod
from variables import memory, history, decimal_point

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

class Set:
    def __init__(self):
        self.__decimal_point = decimal_point

    def set_decimal_point(self):
        point = input("Enter the number of symbols after the decimal point: ")
        if point.isalpha():
            raise TypeError("Please, enter a positive integer!")
        elif int(point) >= 0:
            self.__decimal_point = int(point)
            print(f"Number of symbols after decimal point - {self.__decimal_point}.")
        else:
            raise ValueError("Please, try again. Number of symbols must not be negated!")

    def get_decimal_point(self):
        return self.__decimal_point

class BaseCalculator(ABC):
    def __init__(self):
        self.memory = Memory()
        self.history = History()
        self.set = Set()

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

class Calculator(BaseCalculator):
    def perform_operators(self, num1, operator, num2):
        decimal_point = self.set.get_decimal_point()

        match operator:
            case '+':
                return round(num1 + num2, decimal_point)
            case '-':
                return round(num1 - num2, decimal_point)
            case '*':
                return round(num1 * num2, decimal_point)
            case '/':
                if num2 == 0:
                    raise ZeroDivisionError("You cant't divide by zero!")
                return round(num1 / num2, decimal_point)
            case '^':
                return round(math.pow(num1, num2), decimal_point)
            case '√':
                if num1 < 0:
                    raise ValueError("You can't get a square root from a negative number!")
                return round(math.sqrt(num1), decimal_point)
            case '%':
                if num2 == 0:
                    raise ZeroDivisionError("You can't get a percentage from zero!")
                return round(num1 % num2, decimal_point)
            case _:
                raise ValueError("Incorrect operator! Please, try again!")

    def calculate(self):
        while True:
            num1, operator, num2 = self.get_input()
            result = self.perform_operators(num1, operator, num2)
            if result is not None:
                print(f"Result of calculations: {result}")
                self.history.add_to_history(f"{num1} {operator} {num2 if num2 is not None else ''}", result)

                if input("Do you want to save result? (y/n)").lower() == 'y':
                    self.memory.set_memory(result)
                    print(f"Result {result} was saved.")

            if input("Do you want to do new calculation? (y/n)").lower() == 'n':
                break
import json
import csv
import os

class DataSaver:
    @staticmethod
    def save_to_json(data, filename):
        os.makedirs("/Users/admin/Desktop/ДЗ/3 семестр/Спеціалізовані мови програмування/Final/Lab7/Data", exist_ok=True)
        filepath = os.path.join("/Users/admin/Desktop/ДЗ/3 семестр/Спеціалізовані мови програмування/Final/Lab7/Data", filename)
        with open(filepath, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Data was saved in {filepath}")

    @staticmethod
    def save_to_csv(data, filename):
        os.makedirs("/Users/admin/Desktop/ДЗ/3 семестр/Спеціалізовані мови програмування/Final/Lab7/Data", exist_ok=True)
        filepath = os.path.join("/Users/admin/Desktop/ДЗ/3 семестр/Спеціалізовані мови програмування/Final/Lab7/Data", filename)
        if data:
            keys = data[0].keys()
            with open(filepath, "w", newline='') as file:
                writer = csv.DictWriter(file, fieldnames=keys)
                writer.writeheader()
                writer.writerows(data)
        print(f"Data was saved in {filepath}")

    @staticmethod
    def save_to_txt(data, filename):
        os.makedirs("/Users/admin/Desktop/ДЗ/3 семестр/Спеціалізовані мови програмування/Final/Lab7/Data", exist_ok=True)
        filepath = os.path.join("/Users/admin/Desktop/ДЗ/3 семестр/Спеціалізовані мови програмування/Final/Lab7/Data", filename)
        with open(filepath, "w") as file:
            for entry in data:
                file.write(f"{entry}\n")
        print(f"Data was saved in {filepath}")

    @staticmethod
    def select_save_format(data, data_type):
        print("\nSelect format to save:")
        print("1. JSON")
        print("2. CSV")
        print("3. TXT")
        choice = input("Select option: ")

        filename = input("Enter file name, without extencion: ")

        if choice == "1":
            filename += ".json"
            DataSaver.save_to_json(data, filename)
        elif choice == "2":
            filename += ".csv"
            DataSaver.save_to_csv(data, filename)
        elif choice == "3":
            filename += ".txt"
            DataSaver.save_to_txt(data, filename)
        else:
            print("Error; Incorrect option! Please, try again!")
            DataSaver.select_save_format(data, data_type)

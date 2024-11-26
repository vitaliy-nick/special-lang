from abc import ABC, abstractmethod
import pandas as pd
import matplotlib.pyplot as plt
import os


class DataVisualizer(ABC):
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def visualize(self):
        try:
            self.load_data()
            self.process_data()
            self.plot()
            self.export()
        except KeyError as e:
            print(f"Error: Required column missing from file - {e}!")
        except FileNotFoundError:
            print("Error: File not found!")
        except pd.errors.EmptyDataError:
            print("Error: File is empty or wrong format!")

    def load_data(self):
        self.data = pd.read_csv(self.file_path)
        print("Data loaded successfully!")

    @abstractmethod
    def process_data(self):
        pass

    @abstractmethod
    def plot(self):
        pass

    def export(self):
        save_option = input("Do you want to save chart? (y/n): ").strip().lower()
        if save_option == 'y':
            file_format = input("Select file format to save, png or svg: ").strip().lower()
            if file_format not in ['png', 'svg']:
                print("Invalid format. The chart will be saved in PNG format by default.")
                file_format = 'png'

            file_name = input("Enter file name without extension: ").strip()
            if not file_name:
                print("Name is empty, so file was saved as 'chart'")
                file_name = "chart"

            folder_path = 'Lab8/data'
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            file_name_with_extension = os.path.join(folder_path, f"{file_name}.{file_format}")
            try:
                plt.tight_layout()
                plt.savefig(file_name_with_extension)
                print(f"Chart was saved in '{file_name_with_extension}'.")
            except Exception as e:
                print(f"Error saving file {e}")
        else:
            print("Error: Chart was not saved!")
        plt.show()

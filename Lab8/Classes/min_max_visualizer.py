import pandas as pd

from Classes.data_visualizer import DataVisualizer


class MinMaxVisualizer(DataVisualizer):
    def visualize(self):
        try:
            self.load_data()
            self.process_data()
        except FileNotFoundError:
            print("Error: File not found!")
        except pd.errors.EmptyDataError:
            print("Error: File is empty or wrong format!")

    def process_data(self):
        print("\nMin and max values for each column:")

        for column in self.data.columns:
            column_min = self.data[column].min()
            column_max = self.data[column].max()
            print(f"{column}: Min = {column_min}, Max = {column_max}")

    def plot(self):
        pass

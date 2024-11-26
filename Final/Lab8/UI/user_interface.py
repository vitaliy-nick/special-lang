import os
import sys

lab8_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(lab8_root)

from Classes.bar_chart_visualizer import BarChartVisualizer
from Classes.line_chart_visualizer import LineChartVisualizer
from Classes.scatter_plot_visualizer import ScatterPlotVisualizer
from Classes.min_max_visualizer import MinMaxVisualizer
from Classes.combined_chart_visualizer import CombinedChartVisualizer

def main():
    while True:
        print("\nMain menu:")
        print("1. Bar Chart.")
        print("2. Line Chart.")
        print("3. Scatter Chart.")
        print("4. Show max and min values.")
        print("5. Show all charts.")
        print("6. Exit.")

        choice = input("Select option: ")

        if choice == '6':
            print("Exit from programm!")
            break

        file_path = input("Enter path to CSV-file: ")

        if choice == '1':
            visualizer = BarChartVisualizer(file_path)
        elif choice == '2':
            visualizer = LineChartVisualizer(file_path)
        elif choice == '3':
            visualizer = ScatterPlotVisualizer(file_path)
        elif choice == '4':
            visualizer = MinMaxVisualizer(file_path)
        elif choice == '5':
            visualizer = CombinedChartVisualizer(file_path)
        else:
            print("Error: Incorrect option. Please, try again!")
            continue

        visualizer.visualize()


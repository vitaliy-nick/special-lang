from Classes.data_visualizer import DataVisualizer
import matplotlib.pyplot as plt

class ScatterPlotVisualizer(DataVisualizer):
    def process_data(self):
        print("Data processed for scatter chart.")

    def plot(self):
        plt.scatter(self.data['X'], self.data['Y'], color='red', alpha=0.5)
        plt.title("Scatter Chart") # Діаграма розсіювання
        plt.xlabel("X")
        plt.ylabel("Y")
        print("Scatter chart is build.")

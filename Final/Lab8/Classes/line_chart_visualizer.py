from Classes.data_visualizer import DataVisualizer
import matplotlib.pyplot as plt

class LineChartVisualizer(DataVisualizer):
    def process_data(self):
        self.data.sort_values('Year', inplace=True)
        print("Data processed for line chart.")

    def plot(self):
        plt.plot(self.data['Year'], self.data['Change'], marker='o', linestyle='-', color='green')
        plt.title("Line Chart") # лінійна діаграма
        plt.xlabel("Year")
        plt.ylabel("Change")
        plt.xticks(rotation=45)
        print("Line chart is build.")

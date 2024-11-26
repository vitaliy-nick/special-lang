from matplotlib import pyplot as plt
from Classes.data_visualizer import DataVisualizer

class BarChartVisualizer(DataVisualizer):
    def process_data(self):
        self.data = self.data.groupby('Year')['Price'].sum()
        print("Data processed for bar chart.") # стовпчикова діаграма

    def plot(self):
        self.data.plot(kind='bar', color='skyblue')
        plt.title("Bar Chart")
        plt.xlabel("Year")
        plt.ylabel("Price Bitcoin")
        print("Bar chart is build.")

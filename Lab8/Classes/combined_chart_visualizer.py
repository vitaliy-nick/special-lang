from Classes.data_visualizer import DataVisualizer
import matplotlib.pyplot as plt

class CombinedChartVisualizer(DataVisualizer):
    def process_data(self):
        self.bar_data = self.data.groupby('Price')['Change'].sum()
        self.line_data = self.data.sort_values('Year')
        self.scatter_data = self.data[['X', 'Y']]

    def plot(self):
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))

        # Стовпчикова діаграма
        self.bar_data.plot(kind='bar', color='skyblue', ax=axes[0])
        axes[0].set_title("Bar Chart")
        axes[0].set_xlabel("Year")
        axes[0].set_ylabel("Price Bitcoin")

        # Лінійна діаграма
        axes[1].plot(self.line_data['Year'], self.line_data['Change'], marker='o', linestyle='-', color='green')
        axes[1].set_title("Line Chart")
        axes[1].set_xlabel("Year")
        axes[1].set_ylabel("Change")
        axes[1].tick_params(axis='x', rotation=45)

        # Діаграма розсіювання
        axes[2].scatter(self.scatter_data['X'], self.scatter_data['Y'], color='red', alpha=0.5)
        axes[2].set_title("Scatter Chart")
        axes[2].set_xlabel("X")
        axes[2].set_ylabel("Y")

        plt.tight_layout()

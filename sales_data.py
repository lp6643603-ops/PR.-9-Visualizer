import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class SalesDataAnalyzer:
    def __init__(self, file_path=None):
        self.data = None
        self.last_fig = None
        if file_path:
            self.load_data(file_path)

    def __del__(self):
        
        pass

    def load_data(self, file_path):
        try:
            self.data = pd.read_csv(file_path)
            print("Dataset loaded successfully!")
        except Exception as e:
            print(f"Error loading file: {e}")

    def explore_data(self, option):
        if self.data is None:
            print("Please load a dataset first!")
            return
        
        if option == 1:
            print(self.data.head(5))
        elif option == 2:
            print(self.data.tail(5))
        elif option == 3:
            print(self.data.columns.tolist())
        elif option == 4:
            print(self.data.dtypes)
        elif option == 5:
            print(self.data.info())

    def handle_missing_data(self, option, fill_value=None):
        if self.data is None:
            print("Please load a dataset first!")
            return

        missing = self.data[self.data.isnull().any(axis=1)]
        
        if option == 1:
            if missing.empty:
                print("No missing values found in the dataset!")
            else:
                print(missing)
        elif option == 2:
            numeric_cols = self.data.select_dtypes(include=[np.number]).columns
            self.data[numeric_cols] = self.data[numeric_cols].fillna(self.data[numeric_cols].mean())
            print("Missing values filled with column mean.")
        elif option == 3:
            self.data.dropna(inplace=True)
            print("Rows with missing values dropped.")
        elif option == 4:
            if fill_value is not None:
                self.data.fillna(fill_value, inplace=True)
                print(f"Missing values replaced with {fill_value}.")

    def generate_descriptive_stats(self):
        if self.data is None:
            print("Please load a dataset first!")
            return
        print(self.data.describe())
        print("\nStandard Deviation:")
        print(self.data.std(numeric_only=True))
        print("\nVariance:")
        print(self.data.var(numeric_only=True))

    def visualize_data(self, plot_type, x_col=None, y_col=None):
        if self.data is None:
            print("Please load a dataset first!")
            return

        fig, ax = plt.subplots(figsize=(8, 5))
        
        if plot_type == 1: 
            sns.barplot(data=self.data, x=x_col, y=y_col, ax=ax)
        elif plot_type == 2: 
            sns.lineplot(data=self.data, x=x_col, y=y_col, ax=ax)
        elif plot_type == 3: 
            print(f"Generating scatter plot...")
            sns.scatterplot(data=self.data, x=x_col, y=y_col, ax=ax)
        elif plot_type == 4: 
            self.data[x_col].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
        elif plot_type == 5:
            sns.histplot(self.data[x_col], ax=ax)
        elif plot_type == 6: 
            ax.stackplot(range(len(self.data)), self.data[x_col], self.data[y_col])

        plt.title(f"{x_col} vs {y_col}" if y_col else f"Distribution of {x_col}")
        self.last_fig = fig
        plt.show()
        print(f"{plot_type} displayed successfully!")

    def save_visualization(self, filename):
        if self.last_fig:
            self.last_fig.savefig(filename)
            print(f"Visualization saved as {filename} successfully!")
        else:
            print("No generated plot available to save.")


def main():
    analyzer = SalesDataAnalyzer()
    
    while True:
        print("\nData Analysis & Visualization Program")
        print("Please select an option:")
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Perform DataFrame Operations")
        print("4. Handle Missing Data")
        print("5. Generate Descriptive Statistics")
        print("6. Data Visualization")
        print("7. Save Visualization")
        print("8. Exit")
     

        choice = input("Enter your choice: ")

        if choice == '1':
            print("\n== Load Dataset ==")
            path = input("Enter the path of the dataset (CSV file): ")
            analyzer.load_data(path)

        elif choice == '2':
            print("\nExplore Data")
            print("1. Display the first 5 rows")
            print("2. Display the last 5 rows")
            print("3. Display column names")
            print("4. Display data types")
            print("5. Display basic info")
            sub_choice = int(input("Enter your choice: "))
            analyzer.explore_data(sub_choice)

        elif choice == '4':
            print("\n Handle Missing Data ")
            print("1. Display rows with missing values")
            print("2. Fill missing values with mean")
            print("3. Drop rows with missing values")
            print("4. Replace missing values with a specific value")
            sub_choice = int(input("Enter your choice: "))
            analyzer.handle_missing_data(sub_choice)

        elif choice == '5':
            print("\n Descriptive Statistics ")
            analyzer.generate_descriptive_stats()

        elif choice == '6':
            print("\n Data Visualization ")
            print("1. Bar Plot\n2. Line Plot\n3. Scatter Plot\n4. Pie Chart\n5. Histogram\n6. Stack Plot")
            plot_type = int(input("Enter your choice: "))
            x_col = input("Enter x-axis column name: ")
            y_col = input("Enter y-axis column name: ") if plot_type in [1, 2, 3, 6] else None
            analyzer.visualize_data(plot_type, x_col, y_col)

        elif choice == '7':
            print("\n Save Visualization ")
            filename = input("Enter file name to save the plot (e.g., scatter_plot.png): ")
            analyzer.save_visualization(filename)

        elif choice == '8':
            print("\nExiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()
Sales Data Analyzer

A Python-based Sales Data Analysis and Visualization program that loads CSV datasets and provides options to explore data, handle missing values, generate descriptive statistics, create visualizations, and save generated plots.

Features

Load a dataset from a CSV file

Explore dataset:

Display first 5 rows

Display last 5 rows

Display column names

Display data types

Display basic dataset information

Handle missing data:

Display rows containing missing values

Fill numeric missing values with the column mean

Drop rows containing missing values

Replace missing values with a specific value

Generate descriptive statistics:

Count, mean, standard deviation, minimum, maximum, and other statistics

Standard deviation

Variance

Create different visualizations:

Bar Plot

Line Plot

Scatter Plot

Pie Chart

Histogram

Stack Plot

Save the last generated visualization to a file

Interactive menu-driven interface

Technologies Used

Python

Pandas – data loading and DataFrame operations

NumPy – numerical operations

Matplotlib – plotting and visualization

Seaborn – statistical data visualization

Project Structure

Sales-Data-Analyzer/
│
├── sales_data.py
└── README.md

Installation

Make sure Python is installed on your system.

Install the required libraries using:

pip install pandas numpy matplotlib seaborn

How to Run

Run the Python file from the terminal:

python sales_data.py

The program will display the following main menu:

Data Analysis & Visualization Program
Please select an option:

1. Load Dataset
2. Explore Data
3. Perform DataFrame Operations
4. Handle Missing Data
5. Generate Descriptive Statistics
6. Data Visualization
7. Save Visualization
8. Exit

How to Use

1. Load Dataset

Select option 1 and enter the path of your CSV file.

Example:

Enter the path of the dataset (CSV file): sales.csv

The program loads the CSV file using Pandas.

2. Explore Data

Select option 2.

Available operations:

1. Display the first 5 rows
2. Display the last 5 rows
3. Display column names
4. Display data types
5. Display basic info

3. Handle Missing Data

Select option 4.

Available operations:

1. Display rows with missing values
2. Fill missing values with mean
3. Drop rows with missing values
4. Replace missing values with a specific value

The mean option fills missing values only in numeric columns.

4. Generate Descriptive Statistics

Select option 5.

The program displays descriptive statistics using Pandas, followed by standard deviation and variance.

5. Data Visualization

Select option 6.

The program supports:

1. Bar Plot
2. Line Plot
3. Scatter Plot
4. Pie Chart
5. Histogram
6. Stack Plot

For plots that require two columns, enter the x-axis and y-axis column names.

Example:

Enter x-axis column name: sales_rep
Enter y-axis column name: sales_amount

6. Save Visualization

After creating a plot, select option 7 and enter a filename.

Example:

Enter file name to save the plot (e.g., scatter_plot.png): sales_plot.png

The last generated figure will be saved with the specified filename.

7. Exit

Select option 8 to close the program.

Main Class

The project uses a class named SalesDataAnalyzer.

Important methods include:

load_data() – loads a CSV dataset

explore_data() – explores basic dataset information

handle_missing_data() – handles missing values

generate_descriptive_stats() – generates statistical information

visualize_data() – creates charts

save_visualization() – saves the last generated chart

The class structure and these operations are implemented directly in sales_data.py. fileciteturn0file0L6-L10 fileciteturn0file0L18-L22

Missing Data Handling

The program identifies rows containing missing values and provides multiple ways to handle them. Numeric columns can be filled with their mean, or rows containing missing values can be removed. fileciteturn0file0L40-L62

Visualization

The program creates a Matplotlib figure and supports six visualization types through Seaborn/Matplotlib, including bar, line, scatter, pie, histogram, and stack plots. fileciteturn0file0L74-L97

Requirements

Python 3.x

Pandas

NumPy

Matplotlib

Seaborn

Notes

The dataset must be in CSV format.

A dataset should be loaded before performing exploration, missing-data handling, statistics, or visualization.

The save option saves the most recently generated visualization.

The program is designed as an interactive command-line application.

Author

Laxman Prajapati

License

This project is created for educational and data-analysis purpose

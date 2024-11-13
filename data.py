import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file
data = pd.read_csv('data/co-emissions-per-capita new.csv')  # Replace with your actual file path if needed

# Show the first few rows
print(data.head())

# Basic statistics
print(data.describe())

# Check for missing values
print(data.isnull().sum())

# Data types of columns
print(data.dtypes)

# Correlation between numerical columns
correlation = data.corr()
print(correlation)

# Group data by a categorical column
grouped_data = data.groupby('Entity')['Annual COâ‚‚ emissions (per capita)'].mean()  # Replace with your actual column names
print(grouped_data)

# Plot a histogram for a numerical column
plt.figure(figsize=(10, 6))
plt.hist(data['Annual COâ‚‚ emissions (per capita)'], bins=20, color='blue', edgecolor='black')  # Replace with your actual column name
plt.title('Histogram of CO2 Emissions Per Capita')
plt.xlabel('CO2 Emissions Per Capita')
plt.ylabel('Frequency')
plt.show()

# Plot a boxplot to visualize the distribution
sns.boxplot(x=data['Entity'], y=data['Annual COâ‚‚ emissions (per capita)'])  # Replace with your actual column names
plt.title('CO2 Emissions Per Capita by Entity')
plt.show()

# Plot a heatmap for correlation
plt.figure(figsize=(10, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()

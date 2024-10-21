import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'vehicle_emission_dataset.csv'
data = pd.read_csv(r"C:\Users\suhas\Desktop\mini project\Master Thesis\Data\Main_Air_vehicle_emission_dataset.csv\vehicle_emission_dataset.csv")

# Check for duplicates
duplicates = data.duplicated().sum()
print(f"Number of duplicate entries: {duplicates}")

# Drop duplicates if any
data = data.drop_duplicates()

# Set visual styles
sns.set(style="whitegrid")

# Plot distribution of CO2 emissions by vehicle type
plt.figure(figsize=(12, 6))
sns.boxplot(x='Vehicle Type', y='CO2 Emissions', data=data)
plt.title('Distribution of CO2 Emissions by Vehicle Type')
plt.xticks(rotation=45)
plt.ylabel('CO2 Emissions (g/km)')
plt.show()

# Filter for electric and non-electric vehicles
ev_data = data[data['Fuel Type'] == 'Electric']
non_ev_data = data[data['Fuel Type'] != 'Electric']

# Plot comparison of CO2 emissions
plt.figure(figsize=(10, 6))
sns.kdeplot(ev_data['CO2 Emissions'], label='Electric Vehicles', fill=True)
sns.kdeplot(non_ev_data['CO2 Emissions'], label='Non-Electric Vehicles', fill=True)
plt.title('Comparison of CO2 Emissions: Electric vs Non-Electric Vehicles')
plt.xlabel('CO2 Emissions (g/km)')
plt.ylabel('Density')
plt.legend()
plt.show()

# Select only numeric columns for correlation analysis
numeric_columns = data.select_dtypes(include=['float64', 'int64'])

# Calculate correlation matrix
correlation_matrix = numeric_columns.corr()

# Plot heatmap of correlations
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', square=True)
plt.title('Correlation Matrix of Vehicle Emissions Data')
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

# Aggregate emissions data by Vehicle Type
emissions_by_vehicle = data.groupby('Vehicle Type')[['CO2 Emissions', 'NOx Emissions',
                                                      'PM2.5 Emissions', 'VOC Emissions',
                                                      'SO2 Emissions']].sum().reset_index()

# Set the figure size
plt.figure(figsize=(14, 8))

# Set the number of pollutants
num_pollutants = emissions_by_vehicle.shape[1] - 1  # Exclude the 'Vehicle Type' column

# Create a bar plot for each pollutant
for i, pollutant in enumerate(emissions_by_vehicle.columns[1:]):
    plt.subplot(2, 3, i+1)  # 2 rows, 3 columns
    sns.barplot(x='Vehicle Type', y=pollutant, data=emissions_by_vehicle, palette='viridis')
    plt.title(f'Total {pollutant} by Vehicle Type')
    plt.ylabel(f'{pollutant} (g/km)')
    plt.xticks(rotation=45)

    # Adding exact numbers on top of the bars
    for index, value in enumerate(emissions_by_vehicle[pollutant]):
        plt.text(index, value, f'{value:.2f}', ha='center', va='bottom')

plt.tight_layout()  # Adjust subplots to fit into the figure area.
plt.show()

# Summary statistics for emissions
summary_statistics = data[['CO2 Emissions', 'NOx Emissions', 'PM2.5 Emissions', 'VOC Emissions', 'SO2 Emissions']].describe()
print(summary_statistics)
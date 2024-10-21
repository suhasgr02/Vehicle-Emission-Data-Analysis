# Vehicle Emission Data Analysis

This repository contains Python scripts for analyzing a vehicle emissions dataset, focusing on various pollutants such as CO2, NOx, PM2.5, VOC, and SO2 emissions across different vehicle types, with a comparison between electric and non-electric vehicles. The analysis includes visualizations to explore emissions distribution and correlation analysis.

## Files
- **vehicle_emission_dataset.csv**: The dataset used for the analysis.
- **analysis_script.py**: Python script performing the data analysis and generating visualizations.

## Prerequisites
Ensure you have the following Python libraries installed:

```bash
pip install pandas matplotlib seaborn
```

## Analysis Steps

### 1. Load the Dataset
The dataset is loaded from a CSV file using `pandas`:

```python
data = pd.read_csv('vehicle_emission_dataset.csv')
```

### 2. Remove Duplicates
We check for duplicate rows in the dataset and remove them:

```python
duplicates = data.duplicated().sum()
data = data.drop_duplicates()
```

### 3. Visualize CO2 Emissions by Vehicle Type
We create a boxplot to show the distribution of CO2 emissions for different vehicle types:

```python
sns.boxplot(x='Vehicle Type', y='CO2 Emissions', data=data)
plt.title('Distribution of CO2 Emissions by Vehicle Type')
plt.show()
```

### 4. Compare Emissions: Electric vs Non-Electric Vehicles
We compare CO2 emissions between electric and non-electric vehicles using KDE plots:

```python
sns.kdeplot(ev_data['CO2 Emissions'], label='Electric Vehicles', fill=True)
sns.kdeplot(non_ev_data['CO2 Emissions'], label='Non-Electric Vehicles', fill=True)
plt.title('Comparison of CO2 Emissions: Electric vs Non-Electric Vehicles')
plt.show()
```

### 5. Correlation Analysis
We calculate and visualize the correlation between different emission types:

```python
correlation_matrix = numeric_columns.corr()
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', square=True)
plt.title('Correlation Matrix of Vehicle Emissions Data')
plt.show()
```

### 6. Aggregate Emissions by Vehicle Type
We calculate the total emissions for each pollutant by vehicle type and display them in a series of bar plots:

```python
emissions_by_vehicle = data.groupby('Vehicle Type')[['CO2 Emissions', 'NOx Emissions', 'PM2.5 Emissions', 'VOC Emissions', 'SO2 Emissions']].sum()
sns.barplot(x='Vehicle Type', y='CO2 Emissions', data=emissions_by_vehicle)
```

### 7. Summary Statistics
We generate summary statistics for the emissions data:

```python
summary_statistics = data[['CO2 Emissions', 'NOx Emissions', 'PM2.5 Emissions', 'VOC Emissions', 'SO2 Emissions']].describe()
print(summary_statistics)
```

## Results

This analysis helps in understanding the emission patterns from different vehicle types, providing insights into the impact of electric vehicles on air quality. Detailed visualizations and statistical summaries are generated to support the findings.

## Contributing

Feel free to contribute by:
- Improving the data analysis
- Adding more visualizations
- Extending the dataset for a broader scope

## License
This project is open-source under the MIT License.

# README for Vehicle Emission Data Analysis

## Overview
This repository contains Python code for analyzing a dataset on vehicle emissions. The analysis focuses on comparing CO2 emissions between different vehicle types, particularly between electric and non-electric vehicles. Additionally, the dataset's correlation matrix is explored, and the emissions of various pollutants such as NOx, PM2.5, VOC, and SO2 are visualized by vehicle type.

## Dataset
The dataset used for the analysis is named `vehicle_emission_dataset.csv`, and it contains data on various vehicle types, fuel types, and their corresponding emissions, including:
- CO2 Emissions (g/km)
- NOx Emissions (g/km)
- PM2.5 Emissions (g/km)
- VOC Emissions (g/km)
- SO2 Emissions (g/km)

## Files
- `vehicle_emission_analysis.py`: Contains the main analysis script, which:
  - Loads the dataset
  - Removes duplicates
  - Visualizes CO2 emissions by vehicle type
  - Compares CO2 emissions between electric and non-electric vehicles
  - Analyzes correlations between emissions
  - Visualizes pollutant emissions by vehicle type
  - Summarizes the statistical properties of the emission data

## Requirements
To run the code, you will need the following Python libraries:
- `pandas`
- `matplotlib`
- `seaborn`

You can install these using:
```bash
pip install pandas matplotlib seaborn
```

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/suhasgr02/vehicle-emission-analysis.git
   ```
2. Place the `vehicle_emission_dataset.csv` file in the appropriate directory.
3. Run the Python script:
   ```bash
   python vehicle_emission_analysis.py
   ```

## Key Steps in Analysis
1. **Loading and Cleaning the Data**: The dataset is loaded using `pandas`, and duplicates are identified and removed.
2. **CO2 Emissions by Vehicle Type**: The distribution of CO2 emissions for various vehicle types is visualized using a boxplot.
3. **Electric vs. Non-Electric Vehicles**: CO2 emissions of electric and non-electric vehicles are compared using KDE plots.
4. **Correlation Analysis**: A heatmap visualizing the correlation between various emission types (CO2, NOx, PM2.5, VOC, SO2) is generated.
5. **Pollutant Emissions by Vehicle Type**: Bar plots show the total emissions for each pollutant (NOx, PM2.5, VOC, SO2) by vehicle type.
6. **Summary Statistics**: Summary statistics (mean, median, standard deviation, etc.) for the emissions are calculated and printed.

## Interpretation of Results
1. **Duplicate Removal**: Any duplicate entries in the dataset are dropped, ensuring the accuracy of the analysis.
   
2. **CO2 Emissions by Vehicle Type**: The boxplot reveals how CO2 emissions differ across vehicle types. This highlights which vehicles tend to emit more CO2 and whether there are any outliers in the data.

3. **Electric vs. Non-Electric Vehicle Emissions**: The comparison using KDE plots shows a stark difference in CO2 emissions between electric and non-electric vehicles. As expected, electric vehicles have near-zero CO2 emissions, while non-electric vehicles exhibit a wide range of CO2 outputs.

4. **Correlation Matrix**: The heatmap shows how different emissions are correlated with each other. For example, a strong correlation between NOx and CO2 emissions may suggest that vehicles emitting more CO2 also tend to release more NOx.

5. **Pollutant Emissions by Vehicle Type**: The bar plots show the total emissions for various pollutants by vehicle type. This visualization allows us to see which vehicle types are the largest contributors to pollution in terms of each specific pollutant.

6. **Summary Statistics**: Descriptive statistics help in understanding the central tendencies and variability in the emissions data, providing insights into the overall pollution levels.

## Conclusion
This analysis provides a detailed comparison of emissions across vehicle types, with a particular focus on the impact of electric vehicles in reducing CO2 emissions. The correlation analysis and pollutant visualizations offer further insight into the relationships between different emissions and how they vary by vehicle type.

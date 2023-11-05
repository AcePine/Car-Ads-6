## Download the Data

Before proceeding, you need to download the car advertisement dataset (vehicles_us.csv) or use your own dataset in a CSV format. Place the dataset in the root directory of the project.

## Exploratory Data Analysis

A Jupyter notebook named `EDA.ipynb` has been created for exploratory data analysis. This notebook performs several tasks:

- Median approach for filling missing values by model and model year for columns like 'model_year' and 'cylinders'.
- Mode approach for filling missing values by 'model' for non-numeric columns like 'paint_color'.
- Analysis of the dataset for data quality, missing values, and duplicates.

## Web Application Dashboard

The core of this project is the web application dashboard. The `app.py` file in the project's root directory is responsible for creating this dashboard. It utilizes Streamlit and Plotly Express for data visualization.

### Features of the Web Application

1. A checkbox to show or hide new cars.
2. A price analysis section with a dropdown to select different attributes for analyzing their impact on vehicle prices.
3. A scatter plot that displays the distribution of prices by odometer miles, categorized by vehicle condition.
4. A histogram showing the distribution of prices by vehicle condition.

### Outlier Control

The application provides checkboxes to show or hide outliers in both the scatter plot and the histograms, giving users control over the data visualization.

## Project Deployment

The application has been configured for deployment on Render. The necessary files, `requirements.txt`, and `.streamlit/config.toml` have been created for this purpose. You can easily deploy the application by following the instructions in the project description.

# Link to website:
https://car-ads-project-6.onrender.com/

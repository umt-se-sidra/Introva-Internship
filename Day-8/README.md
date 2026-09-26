# Day 8: Getting & Understanding Data — Collection Through EDA

## Overview

On Day 8 of my Introva internship, I practiced collecting data from different sources and performing Exploratory Data Analysis (EDA) on a real-world dataset. I used World Bank population data for 2022 and collected it using two methods: downloading a CSV file and fetching data through a live API.

After collecting the data, I cleaned and organized it, explored its structure, analyzed population distributions, created visualizations, and generated an automated EDA report.

## Objectives

* Understand different ways of collecting data.
* Work with CSV files and JSON data from an API.
* Compare data collected through different methods.
* Understand a dataset using basic pandas functions.
* Perform univariate, bivariate, and multivariate-style analysis.
* Generate an automated EDA report using ydata-profiling.
* Identify meaningful findings from the data.

## Dataset

**Source:** World Bank

**Indicator:** Population, total (SP.POP.TOTL)

**Year:** 2022

The dataset contains country-level population information. I used the country name, country code, population, and region for my analysis.

## Data Collection

### 1. CSV Data Collection

I downloaded the World Bank population dataset in ZIP format using Python's `requests` library. I extracted the required CSV files and loaded them into pandas DataFrames.

I selected the population values for 2022 and combined the country metadata to include regional information. I also removed aggregate entries and rows with missing population values.

### 2. API Data Collection

I used the World Bank API to retrieve population data in JSON format. I sent a request for the year 2022, converted the returned records into a pandas DataFrame, and added regional information.

### 3. CSV and API Comparison

I compared the data collected through both methods using country codes. I checked the number of matching countries and compared their population values to identify any differences.

This practical exercise helped me understand how the same information can be obtained through a downloadable dataset and a live API.

## Data Cleaning and Understanding

I performed the following steps:

* Selected the required columns.
* Added region information using country metadata.
* Removed regional and income-group aggregate entries.
* Handled missing population values.
* Converted population values to numeric format.
* Reset the DataFrame index.
* Checked the dataset's shape, column names, data types, missing values, and duplicate rows.
* Reviewed the first and last rows and the statistical summary.

## Exploratory Data Analysis

### Univariate Analysis

I explored individual variables to understand their distributions.

* Used a histogram to examine the distribution of country populations.
* Used a box plot to identify population outliers.
* Calculated the mean, median, minimum, maximum, and standard deviation of population.
* Visualized the number of countries in each region.

### Bivariate and Group-Based Analysis

I explored population differences across countries and regions.

* Compared population values across regions using a box plot.
* Identified the ten most populated countries.
* Compared the populations of Pakistan, India, China, the United States, and Brazil.
* Calculated and visualized the average country population for each region.

I also generated a correlation heatmap for the numeric population variable. Since the dataset contains population data for a single year, this heatmap does not show a relationship between population and time.

## Automated EDA Report

I used `ydata-profiling` to generate an HTML report containing a statistical overview of the dataset, variable information, distributions, and other useful data-quality details.

The report was saved as `population_eda_report.html`.

## Key Findings

1. The most populated country in the dataset was identified using the maximum population value for 2022.
2. The least populated country among the included countries was identified using the minimum population value.
3. The region with the highest average country population was identified by grouping the data by region and comparing the mean population.

The exact countries, region, and population values are available in the notebook output.

## Tools and Libraries

* Python
* Pandas
* NumPy
* Requests
* Matplotlib
* Seaborn
* ydata-profiling
* Jupyter Notebook / Google Colab
* World Bank API

## Files

* `Day-8.ipynb` — Data collection, cleaning, analysis, visualizations, and findings.
* `cleaned_population_dataset.csv` — Cleaned population dataset.
* `world_population_api_2022.csv` — Population data collected through the API.
* `csv_vs_api_comparison.csv` — Comparison of CSV and API population values.
* `population_eda_report.html` — Automated EDA report.

## Outcome

This task gave me practical experience in collecting data through different methods, working with CSV and JSON formats, inspecting and cleaning a real dataset, performing exploratory analysis, and generating an automated profiling report. It also helped me understand how to investigate a new dataset and extract useful information from it.

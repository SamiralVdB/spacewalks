# Spacewalks

## Overview
Spacewalks is a Python analysis tool for researchers to generate visualisations
and statistical summaries of NASA's extravehicular activity datasets.

## Features
Key features of Spacewalks:

- Generates a CSV table of summary statistics of extravehicular activity crew sizes
- Generates a line plot to show the cumulative duration of space walks over time

## Pre-requisites

Spacewalks was developed using Python version 3.12

To install and run Spacewalks you will need have Python >=3.12 
installed. You will also need the following libraries (minimum versions in brackets)

- [NumPy](https://www.numpy.org/) >=2.0.0 - Spacewalk's test suite uses NumPy's statistical functions
- [Matplotlib](https://matplotlib.org/stable/index.html) >=3.0.0  - Spacewalks uses Matplotlib to make plots
- [pytest](https://docs.pytest.org/en/8.2.x/#) >=8.2.0  - Spacewalks uses pytest for testing
- [pandas](https://pandas.pydata.org/) >= 2.2.0 - Spacewalks uses pandas for data frame manipulation

## Installation instructions
Clone the Spacewalk repository to your local machine using Git.
You can install all dependecies by running the following commands:

```python
python3 -m pip install -r src/requirements.txt
```
To ensure everything is working correctly you can run the test suite using pytest:

```python
python3 -m pytest tests
```

## Usage example
You can run the analysis in the `eva_data_analysis.py` file via the command line using the following syntax:
The following example can be run from the root of this repository:

```python
python3 src/eva_data_analysis data/raw/eva_data.json data/processed/eva_data.csv
```

The first argument is the path to the JSON input file.
The second argument is the path to the CSV output file.
# Stocks Data Visualizations

## Intro

The purpose of this project is to practice creating data visualizations using stocks data from a number of banks and analyzing how their stocks progressed through the financial crisis all the way to early 2016.

### Methods Used

- Data Visualization

### Technologies

- Python 3

### Python Modules

- Pandas
- Pandas DataReader
- Datetime
- Matplotlib
- Seaborn
- Plotly
- Cufflinks

## Project Description

The data visualizations created in this project came from stock data pulled from stooq (https://stooq.com/db/h/) a website that stores free historical market data. The main goal of this project is to visualize the stock trends of common banks like Bank of America and Morgan Stanley before and after the Financial Crisis in 2008 using the modules listed above. Some simple questions regarding the data include:

- What is the maximum close price for each bank's stock throughout the time period?
- Which stocks are 'risky' based on the standard deviation of their stock prices?
- What are the largest drops and largest returns for each bank's stock during the recession?

All the answers to these questions and visualizations of data are found within `analysis.md` file which also contains detailed step-by-step procedures to generate the visualizations.

## Installation of Interactive Modules 
First, clone the repo into a directory of your choice
````
git clone https://github.com/LanceRemigio/stocks-data-visualizations
````

This project contains interactive graphs the require the installation of **plotly** and  **cufflinks**  using pip.

Make sure to have the latest version of pip before installing the modules. This can be done by typing the following into your terminal:
````
python -m pip install --upgrade pip
````
and then install the interactive modules by typing
````
pip install plotly 
pip install cufflinks
````
To properly initialize the interactive graphs, make sure to add the following code at the beginning of your **.ipynb** file
````python
import plotly
import cufflinks as cf
cf.go_offline()
````



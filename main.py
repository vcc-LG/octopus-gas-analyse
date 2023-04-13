import datetime
import json
from collections import OrderedDict
from datetime import datetime, timedelta

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np


def calculate_daily_value(data):
    start_date = datetime.strptime(data['start_date'], '%d %b %Y')
    end_date = datetime.strptime(data['end_date'], '%d %b %Y')
    value = float(data['value'].replace('£',''))

    # Create a dictionary to hold the daily values for each month
    daily_values = {}

    # Loop through each day between the start and end dates
    current_date = start_date
    while current_date <= end_date:
        # Get the month and year for the current date
        month_year = current_date.strftime('%b %Y')

        # Add the current day's value to the dictionary for this month/year
        if month_year not in daily_values:
            daily_values[month_year] = []
        daily_values[month_year].append(value / (end_date - start_date + timedelta(days=1)).days)

        # Move to the next day
        current_date += timedelta(days=1)

    # Loop through the daily_values dictionary to calculate the total value for each month/year
    monthly_values = {}
    for month_year, daily_values_list in daily_values.items():
        monthly_value = round(sum(daily_values_list), 2)
        monthly_values[month_year] = monthly_value

    return monthly_values

def calculate_monthly_total(data):
    # Create a dictionary to hold the monthly totals
    monthly_totals = {}

    # Loop through each element in the data array
    for item in data:
        # Call the calculate_daily_value function to get the monthly values for this element
        monthly_values = calculate_daily_value(item)

        # Loop through the monthly values and add them to the monthly_totals dictionary
        for month_year, monthly_value in monthly_values.items():
            if month_year not in monthly_totals:
                monthly_totals[month_year] = 0

            monthly_totals[month_year] += monthly_value

    return monthly_totals

with open('data.json', 'r') as f:
    data = json.load(f)

def plot_monthly_totals(monthly_totals):
    # Extract the x and y values from the monthly_totals dictionary
    fig, ax = plt.subplots()

    # Convert month-year strings to datetime objects and sort them chronologically
    dates = [datetime.strptime(month_year, '%b %Y') for month_year in monthly_totals.keys()]
    sorted_dates = sorted(dates)

    # Convert sorted dates back to month-year strings
    month_years = [date.strftime('%b %Y') for date in sorted_dates]

    # Get corresponding monthly total values
    monthly_costs = [monthly_totals[month_year] for month_year in month_years]

    # Create the plot with markers for the data points
    ax.plot(month_years, monthly_costs, marker='o', markersize=6, linewidth=2)

    # Set the y-axis label
    ax.set_ylabel('Monthly gas cost (£)', fontsize=12)

    # Add faint gridlines
    ax.grid(which='major', axis='both', linestyle='--', alpha=0.2)

    # Set the title
    ax.set_title('Monthly gas cost', fontsize=16)

    plt.xticks(rotation=90)

    # Show the plot
    plt.show()

monthly_totals = calculate_monthly_total(data)
plot_monthly_totals(monthly_totals)

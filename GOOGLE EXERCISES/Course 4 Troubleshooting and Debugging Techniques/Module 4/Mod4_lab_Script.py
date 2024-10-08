#!/usr/bin/env python3

import csv
import datetime
import requests
from collections import defaultdict

FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"


def get_start_date():
    """Interactively get the start date to query for."""
    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()

    return datetime.datetime(year, month, day)


def get_file_lines(url):
    """Returns the lines contained in the file at the given URL"""
    response = requests.get(url, stream=True)
    return [line.decode("UTF-8") for line in response.iter_lines()]


def get_same_or_newer(start_date):
    """Returns the employees that started on or after the given date, for the same month."""
    data = get_file_lines(FILE_URL)

    # Create a dictionary to store dates and employees
    employee_dates = defaultdict(list)

    # Process the CSV data
    reader = csv.reader(data[1:])
    target_month = start_date.strftime('%Y-%m')
    target_day = start_date.day

    for row in reader:
        name = row[0]
        date = datetime.datetime.strptime(row[3], '%Y-%m-%d')

        # Only process dates in the target month and year
        if date.strftime('%Y-%m') == target_month and date.day >= target_day:
            employee_dates[date].append(name)

    # Sort dates and prepare output
    sorted_dates = sorted(employee_dates.keys())
    result = []
    for date in sorted_dates:
        formatted_date = date.strftime("%b %d, %Y")  # Format like "Oct 06, 2019"
        employees = employee_dates[date]
        result.append((formatted_date, employees))

    return result


def main():
    start_date = get_start_date()
    employee_data = get_same_or_newer(start_date)

    for date, employees in employee_data:
        print(f"Started on {date}: {employees}")


if __name__ == "__main__":
    main()
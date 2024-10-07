import datetime
from datetime import date


def add_year(date_obj):
    try:
        new_date_obj = date_obj.replace(year=date_obj.year + 1)
    except ValueError:
        # This gets executed when the above method fails,
        # which means that we're making a Leap Year calculation
        new_date_obj = date_obj.replace(year=date_obj.year + 4)

    # Debug line
    print(f"add_year: Input date: {date_obj}, Output date: {new_date_obj}")

    return new_date_obj


def next_date(date_string):
    # Convert the argument from string to date object
    date_obj = datetime.datetime.strptime(date_string, "%Y-%m-%d")
    next_date_obj = add_year(date_obj)

    # Convert the datetime object to string,
    # in the format of "yyyy-mm-dd"
    next_date_string = next_date_obj.strftime("%Y-%m-%d")

    # Debug line
    print(f"next_date: Input string: {date_string}, Output string: {next_date_string}")

    return next_date_string


# Test cases
today = date.today()  # Get today's date
print("Test case 1 (Today's date):")
print(next_date(str(today)))
# Should return a year from today, unless today is Leap Day

print("\nTest case 2 (Regular date):")
print(next_date("2021-01-01"))  # Should return 2022-01-01

print("\nTest case 3 (Leap day):")
print(next_date("2020-02-29"))  # Should return 2024-02-29
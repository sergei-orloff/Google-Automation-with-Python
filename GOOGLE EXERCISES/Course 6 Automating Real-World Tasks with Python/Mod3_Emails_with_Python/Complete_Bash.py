#!/usr/bin/env python3

import json
import locale
import sys
import reports
import emails


def load_data(filename):
    """Loads the contents of filename as a JSON file."""
    with open(filename) as json_file:
        data = json.load(json_file)
    return data


def format_car(car):
    """Given a car dictionary, returns a nicely formatted name."""
    return "{} {} ({})".format(car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
    """Analyzes the data, looking for maximums.
    Returns a list of lines that summarize the information.
    """
    max_revenue = {"revenue": 0}
    max_sales = {"total_sales": 0}
    year_count = {}

    for item in data:
        item_price = locale.atof(item["price"].strip("$"))
        item_revenue = item["total_sales"] * item_price
        if item_revenue > max_revenue["revenue"]:
            item["revenue"] = item_revenue
            max_revenue = item

        if item["total_sales"] > max_sales["total_sales"]:
            max_sales = item

        year = item["car"]["car_year"]
        year_count[year] = year_count.get(year, 0) + item["total_sales"]

    most_popular_year = max(year_count.items(), key=lambda x: x[1])

    summary = [
        "The {} generated the most revenue: ${:.2f}".format(
            format_car(max_revenue["car"]),
            max_revenue["revenue"]
        ),
        "The {} had the most sales: {}".format(
            format_car(max_sales["car"]),
            max_sales["total_sales"]
        ),
        "The most popular year was {} with {} sales.".format(
            most_popular_year[0],
            most_popular_year[1]
        )
    ]

    return summary


def cars_dict_to_table(car_data):
    """Turns the data in car_data into a list of lists."""
    table_data = [["ID", "Car", "Price", "Total Sales"]]
    for item in car_data:
        table_data.append([
            item["id"],
            format_car(item["car"]),
            item["price"],
            item["total_sales"]
        ])
    return table_data


def main(argv):
    """Process the JSON data and generate a full report out of it."""
    data = load_data("car_sales.json")

    # Generate summary and table data
    summary = process_data(data)
    table_data = cars_dict_to_table(data)

    # Create the PDF report content with proper line breaks
    summary_paragraph = "<br/>".join(summary)

    # Generate the PDF report
    pdf_path = "/tmp/cars.pdf"
    reports.generate(pdf_path, summary_paragraph, table_data)

    # Generate and send email
    sender = "automation@example.com"
    recipient = "student@example.com"
    subject = "Sales summary for last month"
    body = "\n".join(summary)  # Use \n for email body

    # Generate email with attachment
    message = emails.generate(sender, recipient, subject, body, pdf_path)

    # Send the email
    emails.send(message)

    # Print summary to console as well
    print(summary)


if __name__ == "__main__":
    main(sys.argv)

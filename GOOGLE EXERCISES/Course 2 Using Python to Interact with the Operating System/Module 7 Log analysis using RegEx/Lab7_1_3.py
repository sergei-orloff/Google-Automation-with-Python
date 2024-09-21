#!/usr/bin/env python3
import re
import csv
import operator

# Initialize dictionaries
error_messages = {}
user_statistics = {}

# Read the log file
logfile = "/home/student/syslog.log"

# Regular expressions for matching log entries
error_pattern = r"ticky: ERROR (.*) \((.*)\)$"
info_pattern = r"ticky: INFO .* \((.*)\)$"

# Process the log file
with open(logfile, "r") as f:
    for line in f:
        if "ERROR" in line:
            match = re.search(error_pattern, line)
            if match:
                error_msg = match.group(1)
                user = match.group(2)
                error_messages[error_msg] = error_messages.get(error_msg, 0) + 1
                user_statistics.setdefault(user, {"INFO": 0, "ERROR": 0})["ERROR"] += 1
        elif "INFO" in line:
            match = re.search(info_pattern, line)
            if match:
                user = match.group(1)
                user_statistics.setdefault(user, {"INFO": 0, "ERROR": 0})["INFO"] += 1

# Sort the errors by count in descending order
sorted_errors = sorted(error_messages.items(), key=operator.itemgetter(1), reverse=True)

# Prepare data for Error Message CSV, including the header
error_data = [("Error", "Count")] + sorted_errors

# Write Error Message CSV file
with open("error_message.csv", "w", newline='') as error_file:
    writer = csv.writer(error_file)
    writer.writerows(error_data)

# Sort users alphabetically and prepare data for User Statistics CSV
sorted_users = sorted(user_statistics.items())
user_data = [("Username", "INFO", "ERROR")] + [(user, data["INFO"], data["ERROR"]) for user, data in sorted_users]

# Write User Statistics CSV file
with open("user_statistics.csv", "w", newline='') as user_file:
    writer = csv.writer(user_file)
    writer.writerows(user_data)

print("Reports have been generated: error_message.csv and user_statistics.csv")
# ====================================
#
#      ./csv_to_html.py error_message.csv /var/www/html/html_new.html
#
#     ./csv_to_html.py user_statistics.csv /var/www/html/html_stat.html
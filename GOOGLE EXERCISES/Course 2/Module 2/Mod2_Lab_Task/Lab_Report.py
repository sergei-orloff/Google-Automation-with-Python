import csv


def count_employees_by_department(csv_file):
    """Counts the number of employees in each department from a CSV file.

  Args:
    csv_file: The path to the CSV file containing employee data.

  Returns:
    A dictionary where keys are department names and values are employee counts.
  """

    department_counts = {}
    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            department = row['Department']
            department_counts[department] = department_counts.get(department, 0) + 1
    return department_counts


def generate_report(department_counts, output_file):
    """Generates a report of employee counts by department to a text file.

  Args:
    department_counts: A dictionary of department names and employee counts.
    output_file: The path to the output text file.
  """

    with open(output_file, 'w') as report_file:
        report_file.write("Department\tEmployee Count\n")
        for department, count in department_counts.items():
            report_file.write(f"{department}\t{count}\n")


def main():
    csv_file = 'employees.csv'
    output_file = 'department_counts.txt'

    department_counts = count_employees_by_department(csv_file)
    generate_report(department_counts, output_file)


if __name__ == '__main__':
    main()

"""
1. Import necessary library: Imports the csv module for handling CSV files.
2. Define count_employees_by_department function:
    - Takes the CSV file path as input.
    - Initializes an empty dictionary department_counts to store department and count pairs.
    - pens the CSV file in read mode.
    - Creates a csv.DictReader object to read the CSV data as dictionaries.
    - Iterates over each row (employee) in the CSV:
        = Extracts the department name from the row.
        = Increments the count for the corresponding department in the department_counts dictionary.
    Returns the department_counts dictionary.
3. Define generate_report function:
    - Takes the department_counts dictionary and output file path as input.
    - Opens the output file in write mode.
    - Writes a header line to the output file.
    - Iterates over the department_counts dictionary:
        = Writes the department name and employee count to the output file in a tab-separated format.
4. Define main function:
    - Sets the input CSV file path and output text file path.
    - Calls count_employees_by_department to get department counts.
    - Calls generate_report to create the report.
5. Execute the script if run directly: Calls the main function.
Assumptions:
    - The CSV file employees.csv exists in the same directory as the script and has a header row.
    - The CSV file has a column named 'Department' containing the department information for each employee.
    - The output text file department_counts.txt will be created in the same directory as the script.
This script effectively reads the CSV file, counts employees per department, and generates a formatted report in a text file.
"""
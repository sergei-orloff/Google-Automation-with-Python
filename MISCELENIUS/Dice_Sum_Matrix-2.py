def matrix(initial_number, end_of_first_row):
    n1 = initial_number
    n2 = end_of_first_row + 1  # include the upper range value with +1

    # The first for loop will create the columns.
    for column in range(n1, n2):
        # The nested for loop will create the rows.
        for row in range(n1, n2):
            print(column + row, end=" ")

        # The row ends when the upper range value is encountered within the
        # nested for loop. The outer (column) for loop should insert a new line
        # to create the next row. Use the print() function new line default
        # behavior with an empty print() function:
        print()


# Call the function with 2 integer parameters.
matrix(1, 6)

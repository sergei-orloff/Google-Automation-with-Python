""" 1). print the numbers from 15 to 5, counting down by fives."""
number = 15  # Initialize the variable
while number >= 5:  # Complete the while loop condition
    print(number, end=" ")
    number -= 5  # Increment the variable

# Should print 15 10 5
print()

""" 2). The loop should check each number from 1 to 5 and identify if the number is odd or even."""
for number in range(1, 5 + 1):
    if number % 2 == 0:
        print("even")
    else:
        print("odd")

# Should print:
# odd
# even
# odd
# even
# odd
print()

""" 3). This function should count how many even numbers exist in a sequence from 0 to the given “n” number,
# where 0 counts as an even number.  For example, even_numbers(25) should return 13, and even_numbers(6) should
# return 4."""


def even_numbers(n):
    count = 0
    current_number = 0
    while current_number <= n:  # Complete the while loop condition
        if current_number % 2 == 0:
            count += 1  # Increment the appropriate variable
        current_number += 1  # Increment the appropriate variable
    return count


print(even_numbers(25))  # Should print 13
print(even_numbers(144))  # Should print 73
print(even_numbers(1000))  # Should print 501
print(even_numbers(0))  # Should print 1
print()

""" 4). This function should print rows of asterisks (*), where the number of rows is equal to the “rows” variable. The
 number of asterisks per row should correspond to the row number (row 1 should have 1 asterisk, row 2 should have 2
 asterisks, etc.). The code “row_asterisks(5)” should print:

 *

 * *

 * * *

 * * * *

 * * * * *   """


def rows_asterisks(rows):
    # Complete the outer loop range to control the number of rows
    for x in range(rows + 1):
        # Complete the inner loop range to control the number of
        # asterisks per row
        for y in range(x):
            # Prints one asterisk and one space
            print("*", end=" ")
        # An empty print() function inserts a line break at the
        # end of the row
        print()


rows_asterisks(5)
# Should print the asterisk rows shown above
print()

"""5). The “countdown” function. This function should begin at the “start” variable, which is an integer that is
passed to the function, and count down to 0."""


def countdown(start):
    x = start
    if x > 0:
        return_string = "Counting down to 0: "
        while x >= 0:  # Complete the while loop
            return_string += str(x)  # Add the numbers to the "return_string"
            if x > 0:
                return_string += ","
            x -= 1  # Decrement the appropriate variable
    else:
        return_string = "Cannot count down to 0"
    return return_string


print(countdown(10))  # Should be "Counting down to 0: 10,9,8,7,6,5,4,3,2,1,0"
print(countdown(2))  # Should be "Counting down to 0: 2,1,0"
print(countdown(0))  # Should be "Cannot count down to 0"

print()

"""6). The “odd_numbers” function should return a space-separated string of all odd positive numbers, 
up to and including the “maximum” variable that's passed into the function."""


def odd_numbers(maximum):
    """Returns a space-separated string of odd numbers up to maximum."""
    odd_nums = []
    for num in range(1, maximum + 1):
        if num % 2 != 0:
            odd_nums.append(str(num))
    return ' '.join(odd_nums)


# Example usage:
result = odd_numbers(6)
print(result)  # Output: 1 3 5
print()


# Another version: ==============================================
def odd_numbers(maximum):
    return_string = ""  # Initializes variable as a string

    # Complete the "for" loop with a range that includes all
    # odd numbers up to and including the "maximum" value.
    for num in range(maximum + 1):

        # Complete the body of the loop by appending the odd number
        # followed by a space to the "return_string" variable.
        if num % 2 != 0:
            return_string += str(num) + " "

    # This .strip command will remove the final space
    # at the end of the "return_string".
    return return_string.strip()


print(odd_numbers(6))  # Should be 1 3 5
print(odd_numbers(10))  # Should be 1 3 5 7 9
print(odd_numbers(1))  # Should be 1
print(odd_numbers(3))  # Should be 1 3
print(odd_numbers(0))  # No numbers displayed

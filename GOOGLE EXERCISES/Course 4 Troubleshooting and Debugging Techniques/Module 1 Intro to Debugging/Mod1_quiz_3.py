def binary_search(list, key):
    list.sort()  # Binary search requires a sorted list
    left = 0
    right = len(list) - 1

    while left <= right:
        middle = (left + right) // 2

        if list[middle] == key:
            return middle
        elif list[middle] > key:
            print("Checking the left side")
            right = middle - 1
        else:
            print("Checking the right side")
            left = middle + 1
    return -1

# Test cases
print("Searching for 1:")
result1 = binary_search([10, 2, 9, 6, 7, 1, 5, 3, 4, 8], 1)
print(f"Found at index: {result1}\n")

print("Searching for 5:")
result2 = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
print(f"Found at index: {result2}")
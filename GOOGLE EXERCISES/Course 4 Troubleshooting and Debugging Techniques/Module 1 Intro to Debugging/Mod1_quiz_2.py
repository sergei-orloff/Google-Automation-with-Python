def find_item(list, item, depth=0):
    list.sort()
    # Debug line to show the current recursive depth and list being searched
    indent = "  " * depth
    # print(f"{indent}Searching for {item} in {list}")

    # Returns True if the item is in the list, False if not.
    if len(list) == 0:
        # print(f"{indent}Empty list, returning False")
        return False

    # Is the item in the center of the list?
    middle = len(list) // 2
    # print(f"{indent}Middle index is {middle}, middle value is {list[middle]}")

    if list[middle] == item:
        # print(f"{indent}Item found at middle index!")
        return True

    # Is the item in the first half of the list?
    if item < list[middle]:
        # print(f"{indent}Item is less than middle value, searching first half")
        # Call the function with the first half of the list
        return find_item(list[:middle], item, depth + 1)
    else:
        # print(f"{indent}Item is greater than middle value, searching second half")
        # Call the function with the second half of the list
        return find_item(list[middle + 1:], item, depth + 1)


# Do not edit below this line - This code helps check your work!
list_of_names = ["Parker", "Drew", "Cameron", "Logan", "Alex", "Chris", "Terry", "Jamie", "Jordan", "Taylor"]

# Sort the list first - binary search requires a sorted list
# list_of_names.sort()
# print("Sorted list:", list_of_names)

# print("\nSearching for Alex:")
print(find_item(list_of_names, "Alex"))  # True

# print("\nSearching for Andrew:")
print(find_item(list_of_names, "Andrew"))  # False

# print("\nSearching for Drew:")
print(find_item(list_of_names, "Drew"))  # True

# print("\nSearching for Jared:")
print(find_item(list_of_names, "Jared"))  # False
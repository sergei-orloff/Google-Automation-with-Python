import re

def compare_strings(string1, string2):
    # Convert both strings to lowercase
    # and remove leading and trailing blanks
    string1 = string1.lower().strip()
    string2 = string2.lower().strip()

    # Ignore punctuation
    # Use a character set instead of a range, and escape the hyphen
    punctuation = r"[.?!,;:\'\-]"

    string1 = re.sub(punctuation, r"", string1)
    string2 = re.sub(punctuation, r"", string2)

    # DEBUG CODE
    print(f"After processing:")
    print(f"String 1: '{string1}'")
    print(f"String 2: '{string2}'")
    print(f"Strings are equal: {string1 == string2}")

    return string1 == string2

# Test cases
print("Test case 1:")
print(compare_strings("Have a Great Day!", "Have a great day?"))  # Should be True

print("\nTest case 2:")
print(compare_strings("It's raining again.", "its raining, again"))  # Should be True

print("\nTest case 3:")
print(compare_strings("Learn to count: 1, 2, 3.", "Learn to count: one, two, three."))  # Should be False

print("\nTest case 4:")
print(compare_strings("They found some body.", "They found somebody."))  # Should be False
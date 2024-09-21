import re


def check_aei(text):
    """Checks if the text contains vowels a, e, and i in the order a-e-i with one character between them."""
    result = re.search(r"a([^aei])e([^aei])i", text)
    return result != None


print(check_aei("academia"))  # True
print(check_aei("aerial"))  # False (no character between e and i)
print(check_aei("paramedic"))  # True
print(check_aei("baffled"))  # False (no 'a')
print(check_aei("failure"))  # False (more than one character between vowels)
print()
print("===" * 10)


# ============================================


def check_aei(text):
    """Checks if the text contains vowels a, e, and i in the order a-e-i with exactly one character between each."""
    result = re.search(r"a[^aei]e[^aei]i", text)
    return result is not None


print(check_aei("academia"))  # True
print(check_aei("aerial"))  # False
print(check_aei("paramedic"))  # True
print(check_aei("baffled"))  # False (no 'a')
print(check_aei("failure"))  # False (more than one character between vowels)
print()
print("===" * 10)


# =============================================


def repeating_letter_a(text):
    """Checks if the text contains the letter 'a' (lowercase or uppercase) at least twice.

  Args:
      text: The string to search.

  Returns:
      True if the text contains 'a' at least twice, False otherwise.
  """

    pattern = r"[aA].*[aA]"  # Matches at least two occurrences of 'a' or 'A'
    result = re.search(pattern, text)
    return result is not None


print(repeating_letter_a("banana"))  # True
print(repeating_letter_a("pineapple"))  # False
print(repeating_letter_a("Animal Kingdom"))  # True
print(repeating_letter_a("A is for apple"))  # True

print()
print("===" * 10)


# =================================

def check_character_groups(text):
    """Checks if the text has at least 2 groups of alphanumeric characters separated by whitespace.

  Args:
      text: The string to search.

  Returns:
      True if the text has at least two groups, False otherwise.
  """

    pattern = r"\b\w+\s+\w+\b"
    result = re.search(pattern, text)
    return result is not None


print(check_character_groups("One"))  # False
print(check_character_groups("123  Ready Set GO"))  # True
print(check_character_groups("username user_01"))  # True
print(check_character_groups("shopping_list: milk, bread, eggs."))  # False

print()

"""
Explanation:

\b: Matches word boundaries (beginning or end of a word). This ensures we capture separate groups.
\w+: Matches one or more alphanumeric characters (letters, numbers, and underscores).
\s+: Matches one or more whitespace characters (spaces, tabs, etc.).
Combining the elements: The pattern \b\w+\s+\w+\b searches for:
A word boundary (\b)
One or more alphanumeric characters (\w+)
One or more whitespace characters (\s+)
Another word boundary (\b)
One or more alphanumeric characters (\w+)
This ensures we find two distinct groups of alphanumeric characters separated by whitespace.
"""
print("===" * 10)

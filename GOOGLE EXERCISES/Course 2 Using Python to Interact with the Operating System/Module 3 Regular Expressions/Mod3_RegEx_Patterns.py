"""
The check_web_address function checks if the text passed qualifies as a top-level web address,
 meaning that it contains alphanumeric characters (which includes letters,
 numbers, and underscores), as well as periods, dashes, and a plus sign,
 followed by a period and a character-only top-level domain such as
 ".com", ".info", ".edu", etc.
 """
import re


def check_web_address(text):
    pattern = r"^[a-zA-Z0-9._+-]+\.[a-zA-Z]+$"
    return re.match(pattern, text) is not None


print(check_web_address("google.com"))  # True
print(check_web_address("example.info"))  # True
print(check_web_address("my-site.edu"))  # True
print(check_web_address("invalid_address"))  # False
print(check_web_address("site.com/path"))  # False

print()
print("====================================")

"""
The check_time function checks for the time format of a 12-hour clock, as follows: 
the hour is between 1 and 12, with no leading zero, followed by a colon, 
then minutes between 00 and 59, then an optional space, and 
then AM or PM, in upper or lower case. Fill in the regular expression to do that.
"""


def check_time(text):
    pattern = r"^(1[0-2]|1?[1-9]):[0-5][0-9]\s?(AM|am|PM|pm)$"
    return re.match(pattern, text) is not None


print(check_time("12:00 PM"))  # True
print(check_time("11:59 am"))  # True
print(check_time("3:45 pm"))  # True
print(check_time("09:00 AM"))  # False (leading zero in hour)
print(check_time("13:00 PM"))  # False (hour greater than 12)
print(check_time("12:60 PM"))  # False (invalid minutes)

print()
print("====================================")

""" 
The contains_acronym function checks the text for the presence of 2 or more characters 
or digits surrounded by parentheses, with at least the first character in uppercase 
(if it's a letter), returning True if the condition is met, or False otherwise. 
For example, "Instant messaging (IM) is a set of communication technologies 
used for text-based communication" should return True since (IM) satisfies the match conditions." 
"""


def contains_acronym(text):
    pattern = r"\(([A-Z0-9]+)\)"
    result = re.search(pattern, text)
    return result != None


print(contains_acronym(
    "Instant messaging (IM) is a set of communication technologies used for text-based communication"))  # True
print(contains_acronym(
    "American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic "
    "communication"))  # True
print(contains_acronym("Please do NOT enter without permission!"))  # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)"))  # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!"))  # True

print()
print("====================================")
# ======================================================
"""
The following function is a zip code checker, but it works only with five-digit zip codes. 
Your task is to update the checker to include all nine digits of the zip code; the leading five digits and 
the optional four after the hyphen. The zip code needs to be preceded by at least one space, and 
cannot be at the start of the text.
"""


def correct_function(text):
    result = re.search(r"\s\d{5}(?:-\d{4})?", text)  # Corrected regex pattern with space
    return result is not None


def check_zip_code(text):
    return correct_function(text)  # Call the correct_function


# Call the check_zip_code function with test cases
print(check_zip_code("The zip codes for New York are 10001 thru 11104."))  # True
print(check_zip_code("90210 is a TV show"))  # False (no space before 90210)
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001."))  # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9."))  # False

"""
Explanation of the regular expression:
-  \s: Matches a whitespace character (space, tab, newline, etc.). This ensures the zip code is preceded by at least one 
space.
-  \d{5}: Matches exactly five digits (the first five digits of the zip code).
-  (?:-\d{4})?: This is a non-capturing group that optionally matches a hyphen followed by four digits 
(the optional four digits after the hyphen).
-  -: Matches a hyphen.
-  \d{4}: Matches exactly four digits.
-  ?: Makes the entire group optional.
Improvements:
- Whitespace handling: The '\s' at the beginning ensures the zip code is not at the start of the text.
- Optional hyphen: The non-capturing group allows for both 5-digit and 9-digit zip codes.
- Clarity: The use of a non-capturing group and comments improves readability.
This updated function effectively checks for valid zip codes in the specified format, handling both 5-digit and 
9-digit options.
"""


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
print("====================================")
# ======================================================

"""
Pattern with middle names:
"""


def rearrange_name(name):
    result = re.search(r"(\w+),?\s*(\w+\s+(\w+\.?|\w+))?", name)
    if result == None:
        return name
    return "{} {}".format(result[2], result[1])


name = rearrange_name("Kennedy, John F.")
print(name)

print()
print("====================================")
# ======================================================
"""
The regular expression used in the extract_pid function, to return the uppercase message in parenthesis, 
after the process id."""


def extract_pid(log_line):
    regex = r"\[(\d+)\]:\s*(?:([^:]+):)?\s*([A-Z]+)"  # Removed trailing whitespace
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result.group(1), result.group(3))  # Corrected group index


print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"))  # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]"))  # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message"))  # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup"))  # 67890 (RUNNING)

print()
print("====================================")
# ======================================================

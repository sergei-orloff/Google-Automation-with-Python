"""You are reading an article that contains website urls in the format https://www.website-domain.com. You’d like to
extract the complete urls from the text automatically, instead of copying and pasting them by hand.

The function find_url extracts all encrypted websites that begin with https:// and end with any top level
domain, such as .org, .com, or .co from the text."""
import re


def find_url(website):
    """Extracts all encrypted website URLs (starting with https) from the text.

  Args:
      website: The string containing the text to search for URLs.

  Returns:
      A list of all extracted encrypted website URLs.
  """

    pattern = r"https://www\.[a-zA-Z0-9-]+\.[a-z]{2,}"  # Regular expression pattern
    result = re.findall(pattern, website)  # Use re.findall to find all matches
    return result


# Verify results
print(find_url("Go to the website https://www.coursera.com find more information about Google Certificate Programs. "
               "Then,"
               "visit https://www.python.org/ to learn more about Python."))  # Should return ['https://www.coursera.com','https://www.python.org']
print(find_url("You can find anything on https://www.google.com!"))  # Should return ['https://www.google.com']
print(find_url("You can find anything on http://www.google.com!"))  # Should return []
print(find_url("Check out python.org!"))  # Should return []

"""
Explanation of the regular expression:

https://: Matches the literal string "https://"
www\.: Matches "www." literally, with an escaped dot (.).
[a-z]{2,6}: Matches 2 to 6 lowercase letters (a-z), representing the subdomain.
\.: Matches a literal dot (.)
[a-z]{2,}: Matches 2 or more lowercase letters (a-z), representing the top-level domain (TLD) like ".com" or ".org".
Explanation of the function:

The function takes a string text as input. It defines a regular expression pattern (pattern) that matches URLs 
starting with "https://", followed by "www.", a subdomain (2 to 6 lowercase letters), another dot, and a TLD (2 or 
more lowercase letters). It uses re.findall(pattern, text) to find all non-overlapping matches of the pattern in the 
text. This returns a list of matched URLs. The function then returns the list of extracted URLs."""

print()
print("===============" * 5)
# ==============================================

"""You are exploring the punctuation at the end of sentences and want to split sentences so that each word is 
separate and any punctuation is included in the word next to it."""


def parse_sentences(sentence):
    # Match word characters followed by optional punctuation or non-whitespace characters
    pattern = r'[a-zA-Z0-9_]+\\p{P}?|\S+'  # Escape backslash before 'p'
    result = re.findall(pattern, sentence)
    return result


# Check the outputs
print(parse_sentences("Hello! How are you doing?"))  # should return ['Hello!', 'How', 'are', 'you', 'doing?']
print(parse_sentences("what a beautiful day it is"))  # should return ['what', 'a', 'beautiful', 'day', 'it', 'is']
print(parse_sentences("2 + 2 is definitely 4!"))  # should return ['2', '+', '2', 'is', 'definitely', '4!']

"""
If you need to keep the raw string prefix for other reasons, you can escape the backslash before p to treat it literally.
"""
print()
print("===============" * 5)
# ==============================================

"""
Task:
International Standard Book Numbers (ISBNs) are used to uniquely identify published books. 
They follow the 13-digit format XXX-X-XX-XXXXXX-X, where each X represents one numeric digit. 
You have a list of books, information about those books, and their ISBN numbers. You want to extract the 6 digits of 
the ISBN that come before the last hyphen of each book’s ISBN number. However, you need to be careful to avoid 6-digit 
strings that are not part of the ISBN numbers you’re interested in.
"""


def find_isbn(isbn):
    pattern = r'\b\d{3}-\d-\d{2}-(\d{6})-\d\b'  # Capture the 6 digits in a group
    result = re.search(pattern, isbn)
    if result:
        return result.group(1)
    else:
        return ""


print(find_isbn("123-4-12-098754-0"))  # Should return 098754
print(find_isbn("223094-AB-30"))  # result should be blank
print(find_isbn("1123-4-12-098754-0"))  # result should be blank
print()
print("===============" * 5)

"""Explanation: 
Word boundaries (\b): Added at the start and end of the pattern to ensure that the pattern matches 
only when it corresponds exactly to the ISBN format specified. Input String Mismatch: The string "1123-4-12-098754-0" 
doesn't match the pattern since it has an extra digit at the beginning, so the result will correctly be blank. Now, 
find_isbn("1123-4-12-098754-0") will return an empty string as expected."""
# ==============================================

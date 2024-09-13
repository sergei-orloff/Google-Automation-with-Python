"""
Some code that makes a list of specific letters found in any string.
The LetterCompiler( ) function finds all matches for the letters a through c in
an input string if followed by another character and returns them as a list of strings,
with each string representing one match.
"""

import re

my_txt = "An investment in knowledge pays the best interest."  # An example.


def LetterCompiler(txt):
    result = re.findall(r'([a-c]).', txt)
    return result


"""  r'([a-c]).':   This is a regular expression pattern explained as follows: [a-c]: Matches any single character 
between 'a' and 'c' (inclusive) (i.e., 'a', 'b', or 'c'). ([a-c]): The parentheses around [a-c] indicate a capturing 
group. This means that whenever a match is found, the specific character (either 'a', 'b', or 'c') will be captured. 
.:   The dot matches any single character (except for a newline). After finding an 'a', 'b', or 'c', this ensures that 
there is another character following it (but this second character is not captured)."""

print(LetterCompiler(my_txt))

# # ===========================================
"""
An automatic unit test that verifies whether input strings have the correct list
of string matches.
"""
import unittest


class TestCompiler(unittest.TestCase):

    def test_basic(self):
        testcase = "The best preparation for tomorrow is doing your best today."
        expected = ['b', 'a', 'a', 'b', 'a']
        self.assertEqual(LetterCompiler(testcase), expected)


class TestCompiler2(unittest.TestCase):

    def test_2(self):
        testcase = "A b c d e f g h i j k l m n o q r s t u v w x y z"
        expected = ['b', 'c']
        self.assertEqual(LetterCompiler(testcase), expected)

    def test_3(self):
        testcase = "Vika Orlova"
        expected = ['a']  # The input string is followed by another character or "space"
        # ((but this second character is not captured))
        self.assertEqual(LetterCompiler(testcase), expected)

    def test_4(self):
        testcase = "abc def cab"
        expected = ['a', 'c', 'c']  # The input string is followed by another character ((but this second character
        # is not captured))
        self.assertEqual(LetterCompiler(testcase), expected)

    def test_5(self):
        testcase = "abc def c ab"
        expected = ['a', 'c', 'c', 'a']  # The input string is followed by another character ((but this second
        # character is not captured))
        self.assertEqual(LetterCompiler(testcase), expected)

    def test_6(self):
        testcase = "aaa bbb ccc"
        expected = ['a', 'a', 'b', 'b', 'c']  # The input string is followed by another character or "space"
        # ((but this second character is not captured))
        self.assertEqual(LetterCompiler(testcase), expected)

    def test_7(self):
        testcase = "a a a "
        expected = ['a', 'a', 'a']  # The input string is followed by another character, "space" ((but this second
        # character is not captured))
        self.assertEqual(LetterCompiler(testcase), expected)

    def test_8(self):
        testcase = "a@a#a$"
        expected = ['a', 'a', 'a']  # The input string is followed by another character, "space" ((but this second
        # character is not captured))
        self.assertEqual(LetterCompiler(testcase), expected)

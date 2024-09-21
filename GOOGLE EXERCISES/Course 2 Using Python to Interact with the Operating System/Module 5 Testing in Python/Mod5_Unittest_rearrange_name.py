import re
import unittest


def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    if result:  # Ensure there is a match
        return "{} {}".format(result.group(2), result.group(1))
    return name  # If no match, return the original name


class TestRearrange(unittest.TestCase):

    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_empty_string(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)

    def test_no_comma(self):
        testcase = "SingleName"
        expected = "SingleName"
        self.assertEqual(rearrange_name(testcase), expected)


# Run the tests
if __name__ == "__main__":
    unittest.main()

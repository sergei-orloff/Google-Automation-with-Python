import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_assertNotEqual(self):
        self.assertNotEqual('foo', 'bar')  # Test that two strings are not equal

    def test_assertIs(self):
        x = None
        y = None
        self.assertIs(x, y)  # Test that x is y (both are None)

    def test_assertIsNot(self):
        x = 'foo'
        y = 'bar'
        self.assertIsNot(x, y)  # Test that x is not y

    def test_assertIsNone(self):
        x = None
        self.assertIsNone(x)  # Test that x is None

    def test_assertIsNotNone(self):
        x = 'hello'
        self.assertIsNotNone(x)  # Test that x is not None

    def test_assertIn(self):
        self.assertIn('h', 'hello')  # Test that 'h' is in the string 'hello'

    def test_assertNotIn(self):
        self.assertNotIn('z', 'hello')  # Test that 'z' is not in the string 'hello'

    def test_assertIsInstance(self):
        self.assertIsInstance('hello', str)  # Test that 'hello' is an instance of str

    def test_assertNotIsInstance(self):
        self.assertNotIsInstance(123, str)  # Test that 123 is not an instance of str


if __name__ == '__main__':
    unittest.main()

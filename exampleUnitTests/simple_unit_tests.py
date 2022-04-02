import unittest
from helloworld import get_greetings


class FirstTestClass(unittest.TestCase):

    def test_upper(self):
        expected = "RUBIKS CODE"            # arrange

        actual = "rubiks code".upper()      # act

        self.assertEqual(actual, expected)  # assert


class HelloWorldTests(unittest.TestCase):

    def test_get_greetings_returns_hello_world_string(self):
        expected = 'Hello World!'           # arrange

        actual = get_greetings()            # act

        self.assertEqual(actual, expected)  # assert


if __name__ == '__main__':
    unittest.main()

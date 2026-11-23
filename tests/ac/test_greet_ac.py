import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from greet import greet


class GreetAC(unittest.TestCase):
    def test_ac1_greets_a_person_by_name(self):
        self.assertEqual(greet("Ann"), "Hello, Ann!")

    def test_ac2_an_empty_name_is_a_stranger(self):
        self.assertEqual(greet(""), "Hello, stranger!")


if __name__ == "__main__":
    unittest.main()

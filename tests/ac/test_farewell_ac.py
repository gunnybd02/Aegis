import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from farewell import farewell


class FarewellAC(unittest.TestCase):
    def test_ac1_says_goodbye_by_name(self):
        self.assertEqual(farewell("Ann"), "Goodbye, Ann!")

    def test_ac2_an_empty_name_is_a_stranger(self):
        self.assertEqual(farewell(""), "Goodbye, stranger!")


if __name__ == "__main__":
    unittest.main()

import unittest

class TestApp(unittest.TestCase):
    def test_addition(self):
        # A simple passing test
        self.assertEqual(2 + 3, 5)

if __name__ == "__main__":
    unittest.main()

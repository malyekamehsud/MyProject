import unittest

class TestApp(unittest.TestCase):
    def test_addition(self):
        # This will fail: 2+3 is not 6
        self.assertEqual(2 + 3, 6)

if __name__ == "__main__":
    unittest.main()

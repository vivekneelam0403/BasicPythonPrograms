import unittest
from fruit_tracker import calculate_item_total


class TestFruitTracker(unittest.TestCase):

    def test_calculate_item_total_standard(self):
        self.assertEqual(calculate_item_total(5, 2), 10)

    def test_calculate_item_total_zero(self):
        self.assertEqual(calculate_item_total(0, 2), 0)

    def test_calculate_item_total_single(self):
        self.assertEqual(calculate_item_total(10, 1), 10)


if __name__ == "__main__":
    unittest.main()
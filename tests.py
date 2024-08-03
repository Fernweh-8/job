import unittest

from main import days_until_first_sunday, format_year_month, select_keys_from_dict


class TestMyFunctions(unittest.TestCase):
    def test_days_until_first_sunday(self):
        assert days_until_first_sunday(2023, 9) == [1, 2, 3]
        assert days_until_first_sunday(2023, 10) == [1]
        assert days_until_first_sunday(2024, 8) == [1, 2, 3, 4]

    def test_format_year_month(self):
        assert format_year_month("2023-04") == (2023, 4)

    def test_select_keys_from_dict(self):
        a_dict = {
            "A": 1,
            "B": 2,
            "C": 8,
            "D": 12,
            "E": [1, 2, 3, 4],
        }
        assert select_keys_from_dict(a_dict, ["B", "E", "C"]) == {
            "B": 2,
            "E": [1, 2, 3, 4],
            "C": 8,
        }


if __name__ == "__main__":
    unittest.main()

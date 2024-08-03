import calendar
import statistics
from typing import Optional


def format_year_month(year_month: str) -> tuple:
    return tuple(int(element) for element in year_month.split("-"))


def days_until_first_sunday(year: int, month: int) -> list:
    day = 1
    days = []
    while True:
        if calendar.weekday(year, month, day) != 6:
            days.append(day)
            day += 1
        else:
            days.append(day)
            break
    return days


def format_day(day: int) -> str:
    return str(day).zfill(2)


def select_keys_from_dict(current_dict: dict, keys: list) -> dict:
    new_dict = {}
    for key in keys:
        if key in current_dict:
            value = current_dict[key]
            new_dict[key] = value
    return new_dict


def flatten_list(a_list: list) -> list:
    result = []
    for sub_list in a_list:
        result.extend(sub_list)
    return result


def get_monthly_expenses_to_calculate(data: dict) -> list:
    all_expenses = []
    for categories_dict in data.values():
        amounts = [amount for amount in categories_dict.values()]
        all_expenses.extend(flatten_list(amounts))
    return all_expenses


def safe_median(numbers: list) -> Optional[float]:
    try:
        return statistics.median(numbers)
    except statistics.StatisticsError:
        return None


def solution(expenses):
    all_expenses = []

    # we iterate over year, month keys in the expense input data
    for expense in expenses:
        # we split string "2023-01" into 2 integers 2023, 1 on "-"
        year, month = format_year_month(expense)
        # we check which days to consider for calculations until and including the first sunday
        until_sunday = days_until_first_sunday(year, month)
        # we turn integer days into strings starting with 0
        until_sunday = [format_day(day) for day in until_sunday]
        # we take only days needed for calculation
        unprocessed_data_for_calculation = select_keys_from_dict(expenses[expense], until_sunday)
        # we clean data to leave only a list of amounts
        all_expenses_for_year_month = get_monthly_expenses_to_calculate(unprocessed_data_for_calculation)
        all_expenses.extend(all_expenses_for_year_month)

    # we calculate the median
    return safe_median(all_expenses)


def main():
    expenses = {
        "2023-01": {
            "01": {
                "food": [22.11, 43, 11.72, 2.2, 36.29, 2.5, 19],
                "fuel": [210.22]
            },
            "09": {
                "food": [11.9],
                "fuel": [190.22]
            }
        },
        "2023-03": {
            "07": {
                "food": [20, 11.9, 30.20, 11.9]
            },
            "04": {
                "food": [10.20, 11.50, 2.5],
                "fuel": []
            }
        },
        "2023-04": {}
    }

    print(solution(expenses))


if __name__ == "__main__":
    main()

"""Module totolotek

This a functional realisation of lotto program
- many functions must be refactor and re-create as OOP
- a few doctype to filling
"""
from random import randint

def draw_numbers() -> set:
    """Drawing 6 numbers

    Returns:
        set: 6 drawing numbers between 1 and 49
    """
    result = set()

    while len(result) < 6:
        result.add(randint(1, 49))

    return result


def check_win(my_numbers: set, drawed_numbers: set) -> int:
    """Comparing 2 sets

    Args:
        my_numbers (set): numbers choosen by user
        drawed_numbers (set): result of drawing

    Returns:
        int: //opis//
    """
    return len(my_numbers.intersection(drawed_numbers))


def input_numbers() -> set:
    """get 6 unique numbers from user

    Raises:
        ValueError: user try add wrong number (>49 or <1)

    Returns:
        set: number's set to reuse in next functions
    """
    my_numbers = set()

    while len(my_numbers) < 6:

        try:
            number = int(input('Add number: '))
            if number < 0 or number > 50:
                raise ValueError
        except ValueError:
            print("It isn't correct number! Type a integer number > 0 and <50")
            continue

        my_numbers.add(number)

    return my_numbers


def calculate_plays_to_win(my_numbers: set, min_reward: int = 6) -> int:
    """Calculating how many plays you play to win

    Args:
        my_numbers (set): 6 unique numbers from user
        min_reward (int, optional): minimal rewards. Defaults to 6.

    Returns:
        int: how many plays to win
    """
    reward = 0
    drawing = 0

    while reward < min_reward:
        drawing += 1
        win_numbers = draw_numbers()
        reward = check_win(my_numbers, win_numbers)

    return drawing


def count_years(my_numbers: set = None, plays_in_week: int = 1, plays: int = None) -> float:
    """_summary_

    Args:
        my_numbers (set, optional): _description_. Defaults to None.
        plays_in_week (int, optional): _description_. Defaults to 1.
        plays (int, optional): _description_. Defaults to None.

    Returns:
        float: _description_
    """
    weeks_of_year = 52.177457

    if plays is None:
        plays = calculate_plays_to_win(my_numbers, 6)

    return plays/(weeks_of_year*plays_in_week)


def count_costs(my_numbers: set = None, plays: int = None, one_ticket_cost: float = 3.0) -> float:
    """_summary_

    Args:
        my_numbers (set, optional): _description_. Defaults to None.
        plays (int, optional): _description_. Defaults to None.
        one_ticket_cost (float, optional): _description_. Defaults to 3.0.

    Returns:
        float: _description_
    """
    if plays is None:
        plays = calculate_plays_to_win(my_numbers, 6)

    return plays*one_ticket_cost


if __name__ == '__main__':
    LOTTO = calculate_plays_to_win(input_numbers())
    print(f'Trafisz "6" za {count_years(plays=LOTTO, plays_in_week=1):.2f} lat')
    print(f'Na kupny wydasz {count_costs(plays=LOTTO):.2f} PLN')

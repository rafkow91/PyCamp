"""OOP application of Lotto Game"""
from random import randint

THIRD_DEGREE_REWARD = 24.00
FOURTH_DEGREE_REWARD = 245.10
FIFTH_DEGREE_REWARD = 7706.80


class Game:
    """class Game"""

    def __init__(self, numbers: set = None) -> None:
        """Initiation object Game

        Args:
            numbers (set, optional): 6 unique user's numbers. Defaults to None.
        """
        self.numbers = numbers

    @staticmethod
    def _draw() -> set:
        """Drawing numbers

        Returns:
            set: 6 unique numbers
        """
        result = set()

        while len(result) < 6:
            result.add(randint(1, 50))

        return result

    def winning_degree(self) -> int:
        """_summary_"""
        drawing_numbers = self._draw()
        # print(drawing_numbers)
        # print(self.numbers.intersection(drawing_numbers))
        return len(self.numbers.intersection(drawing_numbers))


if __name__ == '__main__':
    gra = Game(set(range(1,7)))
    list = []
    for _ in range(256):
        list.append(gra.winning_degree())

    print(list)

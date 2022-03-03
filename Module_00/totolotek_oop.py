"""OOP application of Lotto Game"""
from random import randint

THIRD_DEGREE_REWARD = 24.00
FOURTH_DEGREE_REWARD = 245.10
FIFTH_DEGREE_REWARD = 7706.80
SIX_DEGREE_REWARD = 6000000.00

REWARDS = [0, 0, 0, THIRD_DEGREE_REWARD, FOURTH_DEGREE_REWARD, FIFTH_DEGREE_REWARD, SIX_DEGREE_REWARD]

WEEKS_OF_YEAR = 52.177457

class User:
    def __init__(self, name: str = None, age: int = None, numbers: set = {1, 2, 3, 4, 5, 6}) -> None:
        self.name = name
        self.age = age
        self.numbers = numbers

    def input_personal_data(self):
        if self.name is None:
            self.name = input("Input your name: ")

        if self.age is None:
            while True:
                try:
                    self.age = int(input("Input your age: "))
                except ValueError:
                    print('You must input a positive integer!')
                    choice = input('Do you try again? [y/n]  ')
                    if choice == '' or choice[0].lower() == 'y':
                        continue
                    else:
                        break

                break

    def input_numbers(self, numbers: set = None):
        if numbers is not None:
            self.numbers = numbers
        
        else:
            new_numbers = set()

            print('Choose new numbers. Numbers must be a positive integers >0 and <50!')

            while len(new_numbers) < 6:
                try:
                    number = int(input(f'Input {len(new_numbers)+1} number: '))
                    if 0 < number < 50:
                        new_numbers.add(number)
                    else:
                        raise ValueError
                except ValueError:
                    print("A number {number} isn't correct! Try again!")

            choice = input(f'Are you sure to change {self.numbers} -> {new_numbers}? [y/n]')
            if choice == '' or choice[0].lower() == 'y':
                self.numbers = new_numbers

    def __str__(self) -> str:
        return f'User: {self.name}\nAge: {self.age}\nNumbers: {self.numbers}'


class Game:
    """class Game"""

    def __init__(self, player: User = User()) -> None:
        """Initiation object Game

        Args:
            numbers (set): 6 unique user's numbers.
            scores (list): List of winnings degree. Index of list is a winning degree.
        """
        self.player = player
        self.numbers = player.numbers
        self.scores = [0, 0, 0, 0, 0, 0, 0]

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
        
        return len(self.numbers.intersection(drawing_numbers))

    def add_to_scores_list(self, winning_degree: int = 0):
        self.scores[winning_degree] += 1

    def calculate_rewards(self):
        summary = 0
        for index, score in enumerate(self.scores):
            summary += score * REWARDS[index]

        return summary


if __name__ == '__main__':
    raf = User()
    raf.input_numbers({13, 9, 29, 6, 24, 4})

    gra = Game(raf)
    plays = 0

    while gra.scores[6] < 1:
        gra.add_to_scores_list(gra.winning_degree())
        plays += 1

    print(gra.player)
    print(f'{plays:_}')
    print(f'{gra.calculate_rewards():_}')
    print(f'{gra.calculate_rewards()-3*plays:_}')


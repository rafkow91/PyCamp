"""OOP application of Lotto Game"""
from random import randint
from os import system
from time import sleep
import sys


TICKET_COST = 3.00

THIRD_DEGREE_REWARD = 24.00
FOURTH_DEGREE_REWARD = 245.10
FIFTH_DEGREE_REWARD = 7706.80
SIX_DEGREE_REWARD = 6000000.00

REWARDS = [0, 0, 0, THIRD_DEGREE_REWARD, FOURTH_DEGREE_REWARD,
           FIFTH_DEGREE_REWARD, SIX_DEGREE_REWARD]

WEEKS_OF_YEAR = 52.177457


class User:
    """class represanting player"""

    def __init__(self, name: str = None, age: int = None, numbers: set = None) -> None:
        self.name = name
        self.age = age
        self.numbers = numbers
        if self.numbers is None:
            self.numbers = {1, 2, 3, 4, 5, 6}

    def input_personal_data(self):
        """input personal data:
            - name: string
            - age: int
        """
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

                break

    def input_numbers(self, numbers: set = None):
        """input user numbers

        Args:
            numbers (set, optional): user's set of number. Defaults to None.

        Raises:
            ValueError: input wrong type or numbers out of scope
        """
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

    def check_winning_degree(self) -> int:
        """_summary_"""
        drawing_numbers = self._draw()

        return len(self.player.numbers.intersection(drawing_numbers))

    def add_to_scores_list(self, winning_degree: int = 0) -> list:
        """adding simple winning degree to scores list"""
        self.scores[winning_degree] += 1

    def play_while(self, winning_degree: int = 6) -> int:
        """plays while not win declared winning degree

        Args:
            winning_degree (int, optional): winning degree what you want to win. Defaults to 6.

        Returns:
            int: number of played games
        """
        plays = 0
        while self.scores[winning_degree] < 1:
            self.add_to_scores_list(self.check_winning_degree())
            plays += 1

        return plays

    def calculate_rewards(self) -> float:
        """calculating rewards

        Returns:
            float: sum of rewards
        """
        summary = 0
        for index, score in enumerate(self.scores):
            summary += score * REWARDS[index]

        return round(summary, 2)

    def calculate_costs(self) -> float:
        """calculating cost of ticket

        Returns:
            float: total cost
        """
        cost = 0
        for score in self.scores:
            cost += score * TICKET_COST

        return round(cost, 2)

    def calculate_profit(self) -> float:
        """calculate bilans of played games

        Returns:
            float: bilans
        """
        return round(self.calculate_rewards() - self.calculate_costs(), 2)

    def calculate_age(self) -> float:
        """calculating age when player

        Returns:
            float: age in years
        """
        years = 0
        for score in self.scores:
            years += score / WEEKS_OF_YEAR

        return round(self.player.age + years, 2)

    def print_summary(self):
        """printed summary of game in console
        """
        print('\n\n' + '-'*10 + '   S U M M A R Y   ' + '-'*10)
        print(f'Plays:\t{sum(self.scores)}')
        print(f'Tickets cost:\t{self.calculate_costs()} PLN')
        print(f'Sum of rewards:\t{self.calculate_rewards()} PLN')
        print(f'Bilans:\t{self.calculate_profit()} PLN\n')

        if self.calculate_profit() < 0:
            print('Oh no! You are bankrupt!!')
        else:
            print('Congratulation :)')


class Application:
    """class represanting Application
    """
    MENU = {
        1: 'Show user data',
        2: 'Input user data',
        3: 'Input numbers',
        4: 'Play "x" times',
        5: 'Play while you win x',
        0: 'Exit',
    }

    def __init__(self) -> None:
        self.user = User()
        self.choice = None
        self.label = None

    def __str__(self) -> str:
        return self.label

    def _draw_logo(self):
        system('clear')
        weight = len(self.label) + 35
        print('', '-' * weight, '\n |', ' ' * 15, self.label, ' ' * 14, '|\n',
              '-' * weight, '\n\n')

    def _draw_main_menu(self):
        self.label = 'Main menu'
        self._draw_logo()
        for key, value in self.MENU.items():
            print(f'{key} -> {value}')
        print()

    def _get_choice(self) -> int:
        choice = None
        keys = self.MENU.keys()

        while choice not in keys:
            try:
                choice = int(input('Choose option: '))
                if choice not in keys:
                    raise ValueError
            except ValueError:
                print('You input a wrong number')
                continue

        self.choice = choice

    def _go_to_choiced_option(self):
        if self.choice == 0:
            if self.user.name is not None:
                print(f'See you later {self.user.name} ;)')
            else:
                print('Goodbye')
            sleep(1)
            sys.exit()
        elif self.choice == 1:
            print(self.user)
        elif self.choice == 2:
            self.user.input_personal_data()
        elif self.choice == 3:
            self.user.input_numbers()
        elif self.choice == 4:
            self._play_x_times()
        elif self.choice == 5:
            self._play_while()

    def _play_x_times(self):
        game = Game(self.user)

        while True:
            try:
                amount_of_repetitions = int(input('How many times to draw? '))
                if amount_of_repetitions < 1:
                    raise ValueError
            except ValueError:
                print('You must input a positive integer. Try again!')
                continue

            break

        for _ in range(amount_of_repetitions):
            game.add_to_scores_list(game.check_winning_degree())

        game.print_summary()

    def _play_while(self):
        game = Game(self.user)

        while True:
            try:
                winning_degree = int(input('How many degree you want to win? '))
                if winning_degree < 0 or winning_degree > 7:
                    raise ValueError
            except ValueError:
                print('You must input a positive integer >0 and <7. Try again!')
                continue

            break

        game.play_while(winning_degree)
        game.print_summary()

        if self.user.age is not None:
            print(f'When you win you will be {game.calculate_age()} years old.')

    def run(self):
        """start the app :)
        """
        self._draw_main_menu()
        self._get_choice()
        self.label = self.MENU[self.choice]
        self._draw_logo()
        self._go_to_choiced_option()
        input('\n\nPress any key to continue')
        self.run()


if __name__ == '__main__':
    app = Application()
    app.run()

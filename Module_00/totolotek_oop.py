"""OOP application of Lotto Game"""
from random import randint

TICKET_COST = 3.00

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
        self.scores[winning_degree] += 1


    def play_while(self, winning_degree: int = 6) -> int:
        plays = 0
        while self.scores[winning_degree] < 1:
            self.add_to_scores_list(self.check_winning_degree())
            plays += 1

        return plays
        
    def calculate_rewards(self) -> float:
        summary = 0
        for index, score in enumerate(self.scores):
            summary += score * REWARDS[index]

        return round(summary, 2)

    def calculate_costs(self) -> int:
        cost = 0
        for score in self.scores:
            cost += score * TICKET_COST 

        return round(cost, 2)
        
    def calculate_profit(self) -> int:
        return self.calculate_rewards() - self.calculate_costs()

    def calculate_age(self) -> int:
        years = 0
        for score in self.scores:
            years += score / WEEKS_OF_YEAR

        return self.player.age + years

# class Application:
#     def __init__(self) -> None:
#         self.LABEL = 'Main menu'
#         self.MENU = {
#             1: self.show_user_data,
#         #     2: self.input_user_data,
#         #     3: self.input_numbers,
#         #     4: self.play_x_times,
#         #     5: self.play_while,
#         #     0: self.quit
#         }
#         self.user = User()

#     def __str__(self) -> str:
#         return self.LABEL

#     def draw(self):
#         print(self.LABEL)
#         for key, value in self.MENU.items():
#             print(f'{key} -> {value}')
#         return int(input('What do you want to do?  '))
        

#     def show_user_data(self):
#         class Meta:
#             self.LABEL = 'Show User data'
        
    
        self.draw()
        
        print(self.user)

if __name__ == '__main__':
    raf = User('Rafal', 31, {13, 9, 29, 6, 24, 4})
    
    gra = Game(raf)
    # app = Application()
    # app.draw()
    degree = int(input('Winning degree to calculate: '))
    print(gra.player)
    print(f'Plays: {gra.play_while(degree):_}')
    print(f'Rewards sum: {gra.calculate_rewards():_} zł')
    print(f'Tickets costs: {gra.calculate_costs():_} zł')
    print(f'Bilans: {gra.calculate_profit():_} zł')
    print(f'Age when you win {degree}: {gra.calculate_age():_} y/o')



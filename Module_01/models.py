from random import shuffle
from os import system

LABEL = 'BlackJack Game'

class Card:
    def __init__(self, name, value, color) -> None:
        self.name = name
        self.value = value
        self.color = color

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name


class Deck:
    def __init__(self) -> None:
        self.is_shuffled = False
        self.cards = []
        values = ['A', 'K', 'Q', 'J', 10, 9, 8, 7, 6, 5, 4, 3, 2]
        colors = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        for value in values:
            for color in colors:
                try:
                    card_value = int(value)
                except ValueError:
                    card_value = 10
                name = f'{value} {color}'
                self.cards.append(Card(name, card_value, color))

    def shuffle_cards(self) -> None:
        shuffle(self.cards)
        self.is_shuffled = True


class Player:
    def __init__(self, deck=None) -> None:
        self.hand = []
        self.deck = deck

    def calculate_hand(self) -> int:
        summary = 0
        for card in self.hand:
            summary += card.value
            if card.name[0] == 'A' and summary > 21:
                summary -= 9

        return summary

    def add_next_card(self):
        self.hand.append(self.deck.cards.pop(-1))

    def end_game(self) -> tuple:
        return (self.deck, self.calculate_hand())


class Croupier(Player):
    def __init__(self, deck=None, player_store=None) -> None:
        super().__init__(deck)
        self.player_store = player_store

    def is_winner(self):
        return self.calculate_hand() > self.player_store


class Game:
    def __init__(self) -> None:
        deck = Deck()
        deck.shuffle_cards()
        self.deck = deck
        self.player = Player()
        self.croupier = Croupier()

    @staticmethod
    def _draw_logo():
        system('clear')
        weight = len(LABEL) + 65
        print('', '-' * weight, '\n |', ' ' * 30, LABEL, ' ' * 29, '|\n',
              '-' * weight, '\n\n')

    def _start_game(self) -> None:
        self._draw_logo()
        for _ in range(3):
            self.deck.cards.pop(-1)
        for _ in range(2):
            self.player.deck = self.deck
            self.player.add_next_card()
            self.croupier.deck = self.player.end_game()[0]
            self.croupier.add_next_card()
            self.deck = self.croupier.end_game()[0]

    def _player_game(self):
        while self.player.calculate_hand() < 21:
            self._draw_logo()
            print(
                f'You have in hand: {self.player.hand} - it\'s {self.player.calculate_hand()} points')
            choice = input('Do you want to continue playing? [Y/n] ')
            if choice == '' or choice[0].lower() == 'y':
                self.player.add_next_card()
            else:
                break

        self._draw_logo()
        print(
            f'Finnally you have in hand: {self.player.hand} - it\'s {self.player.calculate_hand()} points')

        if self.player.calculate_hand() > 21:
            print('\n\tYou lose! You have more than 21 points!')

        player_game = self.player.end_game()

        self.croupier.deck = player_game[0]
        self.croupier.player_store = player_game[1]

    def _croupier_game(self):
        while self.croupier.calculate_hand() < 21:
            self._draw_logo()
            if self.croupier.is_winner():
                break
            self.croupier.add_next_card()

    def _summary(self):
        self._draw_logo()
        points = self.croupier.calculate_hand()

        print(
            f'Finnally you have in hand: {self.player.hand} - it\'s {self.player.calculate_hand()} points')
        print(f'In hand I have {self.croupier.hand} - it\'s {points} points')
        if points > 21:
            print('\n\tI lose! Congratulations!!')
        else:
            print('\n\tI\'m winner!')

    def play(self):
        self._start_game()
        self._player_game()
        if self.croupier.player_store < 21:
            self._croupier_game()
            self._summary()
        elif self.croupier.player_store == 21:
            print('You are master of BlackJack!!')

# --------------------------------------------------------------------------------------------------

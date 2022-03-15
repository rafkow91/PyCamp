"""Main application of BlackJack Game by rafkow91"""
from models import Game

if __name__ == '__main__':
    CHOICE = ''
    while CHOICE == '' or CHOICE[0].lower() == 'y':
        game = Game()
        game.play()
        print()
        CHOICE = input('Do you want to play again? [Y/n] ')

    print('See you later :)')

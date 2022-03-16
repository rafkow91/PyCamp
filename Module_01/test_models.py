from random import randint
from models import Croupier, Deck, Game, Player, Card

deck = Deck()
player = Player(deck)
croupier = Croupier(deck)
game = Game()


def test_create_deck():
    assert len(deck.cards) == 52
    assert deck.is_shuffled is False


def test_unique_cards_in_deck():
    assert len(deck.cards) == len(set(deck.cards))


def test_shuttling_cards_in_deck():
    deck_copy = deck.cards[:]
    deck.shuffle_cards()

    assert deck.cards != deck_copy
    assert deck.is_shuffled is True


def test_add_next_card():
    card = deck.cards[-1]
    deck_len = len(deck.cards)
    hand_len = len(player.hand)
    player.add_next_card()

    assert player.hand[-1] == card
    assert len(player.hand) == hand_len + 1
    assert len(deck.cards) == deck_len - 1


def test_calculate_hand():
    card1 = Card('Card1', 1, 'Color1')
    card2 = Card('Card2', 2, 'Color2')
    player.hand = [card1, card2]

    assert player.calculate_hand() == 3


def test_end_game():
    result = player.end_game()

    assert result[0] == deck
    assert result[1] == 3


def test_is_winner():
    card1 = Card('Card1', 1, 'Color1')
    croupier.hand = [card1]
    croupier.player_store = 3

    assert croupier.is_winner() is False

    croupier.add_next_card()

    assert croupier.is_winner() is True


def test_start_game():
    cards = game.deck.cards[:]
    game._start_game()
    i = randint(0, 50)

    assert len(game.deck.cards) == len(cards) - 7
    assert game.deck.cards[i] == cards[i]
    assert game.deck.cards[-1] != cards[-1]

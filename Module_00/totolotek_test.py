from totolotek import draw_numbers, check_win

def test_draw_6_numbers():
    score = draw_numbers()
    assert len(score) == 6

def test_win_6():
    my_numbers = set(range(6))
    draw_numbers = set(range(6))
    result = check_win(my_numbers, draw_numbers)
    assert result == 6

def test_win_5():
    my_numbers = set(range(5))
    my_numbers.add(7)
    draw_numbers = set(range(6))
    result = check_win(my_numbers, draw_numbers)
    assert result == 5

def test_win_4():
    my_numbers = set(range(4))
    draw_numbers = set(range(6))
    result = check_win(my_numbers, draw_numbers)
    assert result == 4


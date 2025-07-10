import main

def test_positive():

    text = "hello, world!"
    pattern = "world"
    expected = 7

    result = main.find_substr("hello, world!", "world")

    assert result == expected, f'Ожидалось: {expected}, получили: {result}'

test_positive()


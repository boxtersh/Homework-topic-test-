import pytest
import main

# *************** Тестирование ДЗ №1 *********************************************
def test_positive_find_substr():

    text = 'hello, world!'
    pattern = 'world'
    expected = 7

    result = main.find_substr(text, pattern)

    assert result == expected, f'Ожидалось: {expected}, получили: {result}'


def test_find_substr_line_empty():

    text = ''
    pattern = 'world'
    expected = -1

    result = main.find_substr(text, pattern)

    assert result == expected, f'Ожидалось: {expected}, получили: {result}'


def test_typeerror_param_text():

    text = 13
    pattern = 'world'

    with pytest.raises(TypeError,f'Ожидалось: <class str>, получили: {type(text)}'):
        main.find_substr(text, pattern)


def test_typeerror_param_pattern():

    text = 'hello, world!'
    pattern = 3

    with pytest.raises(TypeError,f'Ожидалось: <class str>, получили: {type(pattern)}'):
        main.find_substr(text, pattern)


# *************** Тестирование ДЗ №2 *********************************************
def test_find_yes_elem():

    lst = [1,2,3,2,5,2,3,5,4]
    value = 5
    expected = 4

    result =  main.find_elem(lst, value)

    assert result == expected, f'Ожидалось: {expected}, получили: {result}'


def test_find_no_value():

    lst = [1,2,3,2,2,3,1,4,6]
    value = 5
    expected = -1

    result =  main.find_elem(lst, value)

    assert result == expected, f'Ожидалось: {expected}, получили: {result}'


def test_find_lst_empty():

    lst = []
    value = 5
    expected = -1

    result =  main.find_elem(lst, value)

    assert result == expected, f'Ожидалось: {expected}, получили: {result}'


def test_parameter_not_list():

    lst = 4
    value = 5

    with pytest.raises(TypeError,f'Ожидалось: <class list>, получили: {type(lst)}'):
        main.find_elem(lst, value)

# *************** Тестирование ДЗ №3 *********************************************
def test_count_yes_value():

    lst = [1,2,3,2,5,2,3,5,3]
    value = 3
    expected = 3

    result =  main.count_occurrences(lst, value)

    assert result == expected, f'Ожидалось: {expected}, получили: {result}'


def test_count_no_value():

    lst = [1,2,3,2,2,3,1,4,6]
    value = 5
    expected = -1

    result =  main.count_occurrences(lst, value)

    assert result == expected, f'Ожидалось: {expected}, получили: {result}'


def test_count_lst_empty():

    lst = []
    value = 5
    expected = -1

    result =  main.count_occurrences(lst, value)

    assert result == expected, f'Ожидалось: {expected}, получили: {result}'


def test_count_parameter_not_list():

    lst = 4
    value = 5

    with pytest.raises(TypeError,f'Ожидалось: <class list>, получили: {type(lst)}'):
        main.count_occurrences(lst, value)

# *************** Тестирование ДЗ №4 *********************************************
def test_reverse_positive():

    s = 'one two three'
    expected = 'three two one'

    result = main.reverse_words(s)

    assert result == expected, f'Ожидалось: {expected}, получили: {result}'


def test_reverse_parameter_not_str():

    s = 4

    with pytest.raises(TypeError,f'Ожидалось: <class str>, получили: {type(s)}'):
        main.reverse_words(s)

# *************** Тестирование ДЗ №5 *********************************************
def test_is_positive_palindrome_yes():

    s = '1 2  3   4   54 3  2  1'
    expected = True

    result = main.is_palindrome(s)

    assert result == expected, f'Ожидали получить {expected}, получили {result}'


def test_is_positive_palindrome_no():

    s = '1 2  3   4   5'
    expected = False

    result = main.is_palindrome(s)

    assert result == expected, f'Ожидали получить {expected}, получили {result}'

def test_is_palindrome_parameter_not_str():
    s = 5

    with pytest.raises(TypeError,f'Ожидали получить <class str>, получили {type(s)}'):
        main.is_palindrome(s)

import main

# test 1 *************************************************************************
def test_positive_find_substr():

    text = "hello, world!"
    pattern = "world"
    expected = 7

    result = main.find_substr(text, pattern)

    assert result == expected, f'Ожидалось: {expected}, получили: {result}'

test_positive_find_substr()
# test 2 *************************************************************************
def test_find_substr_line_empty():

    text = ''
    pattern = 'world'
    expected = -1

    result = main.find_substr(text, pattern)

    assert result == expected, f'Ожидалось: {expected}, получили: {result}'

test_positive_find_substr()
test_find_substr_line_empty()


# test 1 *************************************************************************
def test_find_yes_elem():

    lst = [1,2,3,2,5,2,3,5,4]
    value = 5
    expected = 4

    result =  main.find_elem(lst, value)

    assert result == expected, f'Ожидалось: {expected}, получили: {result}'

# test 2 *************************************************************************
def test_find_no_value():

    lst = [1,2,3,2,2,3,1,4,6]
    value = 5
    expected = -1

    result =  main.find_elem(lst, value)

    assert result == expected, f'Ожидалось: {expected}, получили: {result}'

# test 3 *************************************************************************
def test_find_lst_empty():

    lst = []
    value = 5
    expected = -1

    result =  main.find_elem(lst, value)

    assert result == expected, f'Ожидалось: {expected}, получили: {result}'

test_find_yes_elem()
test_find_no_value()
test_find_lst_empty()


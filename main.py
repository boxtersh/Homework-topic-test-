def __check_parameter_for_str(text: str)->None:

    if not isinstance(text, str):
        raise TypeError(f'Не соответствие типов, ожидалось <class str>, получили {type(text)}')

def __check_parameter_for_list(lst: list)->None:
    if not isinstance(lst, list):
        raise TypeError(f'Не соответствие типов, ожидалось <class list>, получили {type(lst)}')

# *************** Тестирование ДЗ №1 *********************************************
def find_substr(text: str, pattern: str) -> int:
    """
    Поиск первого вхождения (индекс) подстроки pattern в строке text
    Пример:
    text = "hello, world!"
    pattern = "world"
    -> 7

    :param text: Строка
    :param pattern: Подстрока
    :return: индекс первого вхождения
    """
    __check_parameter_for_str(text)
    __check_parameter_for_str(pattern)

    return text.find(pattern)

# *************** Тестирование ДЗ №2 *********************************************
def find_elem(lst: list, value) -> int:
    """
    Поиск первого искомого элемента в списке
    Пример:
    lst = [1,2,3,1,4,5]
    value = 2
    -> 1
    :param lst: список
    :param value: элемент
    :return: индекс найденного элемента
    """
    __check_parameter_for_list(lst)

    if value in lst:
        return lst.index(value)

    return -1

# *************** Тестирование ДЗ №3 *********************************************
def count_occurrences(lst: list, value) -> int:
    """
    Поиск количества вхождений искомого элемента в списке
    Пример:
    lst = [1,2,3,1,4,3]
    value = 3
    -> 2
    :param lst: список
    :param value: элемент
    :return: количество вхождений
    """
    __check_parameter_for_list(lst)

    if value in lst:
        return lst.count(value)

    return -1

# *************** Тестирование ДЗ №4 *********************************************
def reverse_words(s: str) -> str:
    """
    Переставляет строку из слов в обратном порядке:
    Пример:
    s = one two three
    -> three two one
    :param s: строка
    :return: реверс строки
    """
    __check_parameter_for_str(s)

    return ' '.join(s.split(' ')[::-1])

# *************** Тестирование ДЗ №5 *********************************************
def is_palindrome(s: str) -> bool:

    __check_parameter_for_str(s)

    s_nwe = s.replace(' ','')

    return s_nwe.lower()==s_nwe.lower()[::-1]

# ********************************************************************************

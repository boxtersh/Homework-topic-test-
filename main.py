def __check_parameter_for_str(text: str)->None:

    if not isinstance(text, str):
        raise TypeError(f'Не соответствие типов, ожидалось <class str>, получили {type(text)}')

def __check_parameter_for_list(lst: list)->None:
    if not isinstance(lst, list):
        raise TypeError(f'Не соответствие типов, ожидалось <class list>, получили {type(lst)}')

# *************** Тестирование ДЗ №1 *********************************************
def find_substr(text: str, pattern: str) -> int:
    """
    Возвращает индекс первого вхождения подстроки pattern в строке text
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

    len_pattern = len(pattern)
    if pattern[0] in text:
        for i in range(len(text)):
            if text[i] == pattern[0]:
                if text[i:i + len_pattern] == pattern:
                    return i

    return -1

# *************** Тестирование ДЗ №2 *********************************************
def find_elem(lst: list, value) -> int:
    """
    Возвращает индекс первого найденного элемента в списке
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
        for i in range(len(lst)):
            if lst[i] == value:
                return i

    return -1

# *************** Тестирование ДЗ №3 *********************************************
def count_occurrences(lst: list, value) -> int:
    """
    Возвращает количество вхождений искомого элемента в списке
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
        count = 0

        for elm in lst:

            if elm == value:
                count += 1

        return count

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

    flag = True
    new_s = ''
    buff_i = None
    for i in range(-1, -(len(s) + 1), -1):
        if s[i] == ' ':
            if flag:
                new_s += s[i + 1:]
                buff_i = i
                flag = False

            else:
                new_s += s[i:buff_i]
                buff_i = i

        if i == -len(s):
            new_s += ' ' + s[:buff_i]

    return new_s

# *************** Тестирование ДЗ №5 *********************************************
def is_palindrome(s: str) -> bool:

    __check_parameter_for_str(s)

    s_nwe = s.replace(' ','')

    return s_nwe.lower()==s_nwe.lower()[::-1]

# ********************************************************************************

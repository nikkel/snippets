import timeit
import functools
import profile
import re

from timeit import timeit

"""
    Loop Efficency
"""


def forLoop_square():
    number = 100000
    my_list = []
    for i in range(number):
        my_list.append(i)
    return my_list


def listComp_square():
    number = 100000
    my_list = [i for i in range(number)]
    return my_list


def loop_efficentcy():
    print(
        "{}\n{}".format(
            timeit.timeit(forLoop_square, number=1000),
            timeit.timeit(listComp_square, number=1000),
        )
    )


"""
    String Concatenation Efficency
"""


def string_concatenation():
    string_1 = "This  is an example"
    string_2 = "To show concatenation of long strings"
    string_3 = "and related associated efficiencies"
    return string_1 + "." + string_2 + "," + string_3 + "!"


def string_concatenation2():
    string_1 = "This  is an example"
    string_2 = "To show concatenation of long strings"
    string_3 = "and related associated efficiencies"
    return f"{string_1}. {string_2}, {string_3}!"


def stringCon_efficentcy():
    print(
        "{}\n{}".format(
            timeit(string_concatenation, number=1000),
            timeit(string_concatenation2, number=1000),
        )
    )


"""
    Use cacheing for speed
"""


def fibonacci(n=36):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


@functools.lru_cache(maxsize=128)
def fibonacci_cache(n=36):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def cache_efficentcy():
    print(
        "{} - Normal\n{} - cache\n{} - cache\n{} - cache\n{} - cache\n{} - normal\n{} - cache".format(
            fibonacci(36),
            fibonacci_cache(36),
            fibonacci_cache(36),
            fibonacci_cache(36),
            fibonacci_cache(36),
            fibonacci(36),
            fibonacci_cache(36),
        )
    )
    return 0


def sorting_by_key_efficentcy():
    import operator

    my_list = [
        ("Josh", "Grobin", "Singer"),
        ("Marco", "Polo", "General"),
        ("Ada", "Lovelace", "Scientist"),
    ]
    print(my_list)
    my_list.sort(key=operator.itemgetter(2))
    print(my_list)


def string_concat2(list):
    """
    Better way to concat a string
    """
    slist = []
    return s

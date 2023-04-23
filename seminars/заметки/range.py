# range(5) -> 0, 1, 2, 3, 4
# range(5, 10) -> 5, 6, 7, 8, 9
# range(1, 10, 2) -> 1, 3, 5, 7, 9


def f(some_list=None):
    if some_list is None:
        some_list = []
    some_list.append(2)
    print(some_list)

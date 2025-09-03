"""calc which list has the larger sum
    """

# First go


def larger_sum(list1, list2):
    """_summary_

    Args:
        list1 (_type_): _description_
        list2 (_type_): _description_
    """
    list1sum = 0
    list2sum = 0

    for num in list1:
        list1sum = + num
    for num in list2:
        list2sum = + num
    if list1sum > list2sum:
        return list1
    else:
        return list2


print(larger_sum([1, 9, 5], [2, 3, 7]))

# Concatinated Version


def con_larger_sum(lst1, lst2):
    if sum(lst1) > sum(lst2):
        return lst1
    else:
        return lst2


print(con_larger_sum([1, 9, 5], [2, 3, 7]))


def one_line(lst1, lst2):
    return lst1 if sum(lst1) > sum(lst2) else lst2


print(one_line([1, 9, 5], [2, 3, 7]))

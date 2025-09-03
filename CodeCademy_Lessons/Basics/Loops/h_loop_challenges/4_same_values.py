"""identify the indexs of two equally sized lists 
    where the numbers match
    """

"""In this challenge, we need to find the indices in two equally sized lists
      where the numbers match. We will be iterating through both
        of them at the same time and comparing the values, 
        if the numbers are equal, then we record the index. 
    
    """


def same_values(lst1, lst2):
    """_summary_

    Args:
        lst1 (_type_): _description_
        lst2 (_type_): _description_

    Returns:
        _type_: _description_
    """

    same_index = []
    for num in range(len(lst1)):
        if lst1[num] == lst2[num]:
            same_index.append(num)
    return same_index


print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

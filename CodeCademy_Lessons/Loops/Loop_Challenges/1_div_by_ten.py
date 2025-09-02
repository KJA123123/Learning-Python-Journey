"""Count how many nums are divisible by 10
      from a list of numbers
"""


def numbers_div_10(nums):
    """Loop through all numbers which are divisible by 10

    Args:
        nums (list of integers): list of numbers

    Returns:
        integer: count of numbers divisible by 10
    """
    count = 0
    for num in nums:
        if num % 10 == 0:
            count = +1
        else:
            pass
    return count


print(numbers_div_10([20, 25, 30, 35, 40]))

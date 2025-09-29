"""Challenge 1: Tenth Power
    Power is the number multiplied by itself 10 times.
    """


def Tenth_Power(num):
    """outputs the tenth power

    Args:
        num (integer): input number

    Returns:
        integer: tenth power
    """
    count = 1
    result = 1 * num

    while count < 10:

        result *= num

        count += 1
    return result
# Note, I forgot about ** operator doing powers.


def Example_Tenth_Power(num):
    """Shorter tenth power method

    Args:
        num (int): _description_

    Returns:
        int: _description_
    """
    return num ** 10


print(Tenth_Power(2))


Example_Tenth_Power(2)

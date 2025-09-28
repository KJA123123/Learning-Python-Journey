"""Challenge 1: Tenth Power
    Power is the number multiplied by itself 10 times.
    """


def tenth_power(num):
    count = 1
    ans = 1

    while count < 10:
        ans = num*ans  # power of 1

        ans = ans

        count = +1

# Note, I forgot about ** operator doing powers.


def example_tenth_power(num):
    return num ** 10

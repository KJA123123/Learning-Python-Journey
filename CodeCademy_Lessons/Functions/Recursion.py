"""calling the function within itself
    """


def factorial1(num):
    if num == 1:  # base case, as function stops calling itself
        return 1
    else:
        return num * factorial1(num-1)

# Recursive functions contain the recursive step and the base case

# Applying recursion to call stacks


def factorial2(num):
    call_stack = []
    if num == 1:
        print('base case reached! Num is 1.')
        return 1
    else:
        call_stack.append({'input': num})
        print('call stack: ', call_stack)
        return num * factorial2(num-1)


factorial2(5)

# call stack:  [{'input': 5}]
# call stack:  [{'input': 4}]
# call stack:  [{'input': 3}]
# call stack:  [{'input': 2}]
# base case reached! Num is 1.
# 120

# more resources on recursion: https://www.codecademy.com/enrolled/courses/learn-recursion-python


def factorial3(num):
    call_stack = []
    if num == 1:
        print('base case reached! Num is 1.')
        return 1
    else:
        call_stack.append({'input': num})
        print('call stack: ', call_stack)
        return num * factorial3(num-1)


factorial3(5)

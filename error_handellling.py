"""Error handelling using try, except and finally.
    """

nums = [0, 1, 2, 3]

try:
    print(sum(nums))

except:
    print('Cannot print the sum! Your variables are not numbers.')


nums = ['x', 'y', 'z']

try:
    print(sum(nums))

except:
    print('Cannot print the sum! Your variables are not numbers.')

# Finally is used when both the try and except causes may fail:
nums = ['x', 'y', 'z']

try:
    print(sum(nums))

except:
    print('Cannot print the sum! Your variables are not numbers.')

finally:
    print('Hope you got the result you want!')

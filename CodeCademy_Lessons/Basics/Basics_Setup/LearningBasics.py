# This line is needed so Python's inbuilt interpreter
# runs the the function or method the programmer wants it to run from
# as it is defaulted to the name of the program when executed.

if __name__ == '__getting_a_user_input___':


def main():
    print('This line is printed directly from the main function of the program')
    secondary_function()


def secondary_function():
    print('This line is printed from a secondary function call within the main function')


getting_a_user_input()


def getting_a_user_input():
    # input and output are inbuilt-functions in python;
    input('What is your name?')
    name = ('What is your name?')

    # Can be saved to a variable
    age = input('How old are you? ')
    age = ('How old are you? ')

    print('It is very nice to meet you, ', name, '!')

    # Concatenation can also be used (using +),
    # assuming the variables are strings

    print('Very nice to meet you! My name is ' +
          name + ' and I am ' + age + ' years old')


def declaringVairables():
    # Casting is used to specify the type of variable in python:

    temparature = str(97.5)
    print(type(temparature))

    int_value = 4

    print(int_value)
    print(type(int_value))

    float_value = float(int_value)
    print(float_value)
    print(type(float_value))

    raining = True
    raining = bool('True')


def Operators():
    x = 5
    y = 2

    print('Examples of operators')

    print('arithmetic operator (x + y): ', x + y)
    print('comparison operator (x >= y): ', x >= y)
    print('logical operator (x == y and x > y): ', x == y and x > y)

    print()

    print('Exponentiation operator (x ** y)', x ** y)
    print('Floor Division (x // y) (x divided by y, returning the integer)', x // y)
    print('The remainder of x divided by y (x %y)', x % y)

    print()

    print('Examples of Assignments')
    print('x/=4, x =', x /= 4)
    print('x*=4, x =', x*4)
    print('x == 5, x now =', x == 5)

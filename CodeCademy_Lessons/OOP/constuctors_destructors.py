"""constructor / destructor functions to create/delete objects
    """

# Constructors
# Its common for classes to contain their own init function
# An init class will create a class schedule every time the
# class is instatated to create a new object


class ClassSchedule:
    """_Class Schedule
    """

    def __init__(self, course):
        self.course = course

# calling itself using self.
# Note more research needed as pylance is not happy :(

    first = ClassSchedule('Chemistry')
    print(first.course)

# Destructors

    def __del__(self):
        print('You successfully deleted your schedule')


sched = ClassSchedule('Chemistry')
del sched

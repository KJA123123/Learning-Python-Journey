"""Learning Script about access modifiers
    """


# Public Access Modifier
# Default: all members within the class are public
# These can easily be accessed outside the class
# in another part of the program


class ClassSchedule:
    """
    """

    def __init__(self, course, instructor):
        self.course = course
        self.instructor = instructor

    def display_course(self):
        print(f'Course: {self.course}, Instructor: {self.instructor}')


# Testing
sched = ClassSchedule('Chemistry', 'Mr. Doe')  # Initalising

sched.display_course()
sched.course


# Private Access Modifier
# these are denoted with __ prefix, and to be accessed within
# the class only, sand attempts to access these will cause and Attribute Error.


sched = ClassSchedule('Biology', 'Ms. Smith')

sched.__course  # this will throw an Attribute Error because we're trying to access a private member

# this won't throw an Attribute Error because this method is public
sched.display_course()

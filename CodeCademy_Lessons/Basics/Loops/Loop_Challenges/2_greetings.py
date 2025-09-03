"""Using append to say hello to a list of names
    """


def add_greetings(names):
    """_summary_

    Args:
        names (list of strings): list of names

    Returns:
        string: greetings
    """
    greetings = []
    for name in names:
        greetings.append("hello" + name)
    return greetings


print(add_greetings(["Owen", "Max", "Sophie"]))

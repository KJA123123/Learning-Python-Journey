from pony.orm import *
db = Database()


class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    age = Required(int)


class Post(db.Entity):
    id = PrimaryKey(int, auto=True)
    title = Required(str)
    content = Required(str)
    author = Required(User)

from uuid import uuid4


DATABASE = {}  # a dict for now, figure out a key value db later ;)


def create(todo):
    todo = dict(todo)
    todo.setdefault('completed', False)
    todo.setdefault('url', uuid4().hex)
    DATABASE[todo['url']] = todo
    return todo


def get_by_url(url):
    return DATABASE.get(url, None)


def get_all():
    return list(DATABASE.values())
from uuid import uuid4
import dbm
import json


DATABASE = dbm.open('/tmp/dbm', 'c')


def create(todo, host=''):
    todo = dict(todo)
    todo.setdefault('completed', False)
    todo.setdefault('url', host + uuid4().hex)
    update(todo)
    return todo


def get_by_url(url):
    return json.loads(DATABASE.get(url, '').decode())


def get_all():
    return [get_by_url(url) for url in DATABASE.keys()]


def delete(url=None):
    if not url:
        for url in DATABASE.keys():
            del DATABASE[url]
    else:
        del DATABASE[url]


def update(todo):
    DATABASE[todo['url']] = json.dumps(dict(todo))


def patch(url, changes):
    todo = get_by_url(url)
    todo.update(changes)
    update(todo)
    return get_by_url(url)

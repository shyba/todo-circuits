import unittest
from todo import db


class DatabaseOperationsTestCase(unittest.TestCase):

    def setUp(self):
        self.db = db
        self.db.DATABASE = {}  # reset it
        self.example_todo = {'title': 'make all tests go green'}

    def test_create_as_not_completed(self):
        # given
        todo = self.example_todo

        # when
        persisted_todo = self.db.create(todo)

        # then
        self.assertFalse(persisted_todo['completed'])
        self.assertIn('url', persisted_todo)

    def test_recover_by_url(self):
        # given
        persisted_todo = self.db.create(self.example_todo)

        # when
        todo = self.db.get_by_url(persisted_todo['url'])

        # then
        self.assertEqual(persisted_todo, todo)

    def test_recover_all(self):
        # given
        persisted_todo1 = self.db.create(self.example_todo)
        persisted_todo2 = self.db.create(self.example_todo)

        # when
        all_todos = self.db.get_all()

        # then
        self.assertIn(persisted_todo1, all_todos)
        self.assertIn(persisted_todo2, all_todos)

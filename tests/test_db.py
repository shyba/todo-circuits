import unittest
from todo import db


class DatabaseOperationsTestCase(unittest.TestCase):

    def setUp(self):
        self.db = db
        self.db.DATABASE = {}  # reset it
        self.example_todo = {'title': 'make all tests go green'}

    def test_create_as_not_completed_and_valid_url(self):
        # given
        todo = self.example_todo

        # when
        persisted_todo = self.db.create(todo, host='http://example.com/')

        # then
        self.assertFalse(persisted_todo['completed'])
        self.assertIn('url', persisted_todo)
        new_url = persisted_todo['url']
        self.assertTrue(new_url.startswith('http://example.com/'))

    def test_recover_by_url(self):
        # given
        persisted_todo = self.db.create(self.example_todo)

        # when
        todo = self.db.get_by_url(persisted_todo['url'])

        # then
        self.assertEqual(persisted_todo, todo)

    def test_update_by_url(self):
        # given
        persisted_todo = self.db.create(self.example_todo)

        # when
        persisted_todo['completed'] = True
        persisted_todo['title'] = 'celebrate green tests'
        self.db.update(persisted_todo)

        # then
        todo = self.db.get_by_url(persisted_todo['url'])
        self.assertEqual(persisted_todo, todo)

    def test_patch_by_url(self):
        # given
        persisted_todo = self.db.create(self.example_todo)

        # when
        patch = {}
        patch['completed'] = True
        patch['title'] = 'celebrate green tests'
        self.db.patch(persisted_todo['url'], patch)

        # then
        todo = self.db.get_by_url(persisted_todo['url'])
        self.assertEqual(patch['title'], todo['title'])
        self.assertEqual(patch['completed'], todo['completed'])

    def test_recover_all(self):
        # given
        persisted_todo1 = self.db.create(self.example_todo)
        persisted_todo2 = self.db.create(self.example_todo)

        # when
        all_todos = self.db.get_all()

        # then
        self.assertIn(persisted_todo1, all_todos)
        self.assertIn(persisted_todo2, all_todos)

    def test_delete_all(self):
        # given
        persisted_todo1 = self.db.create(self.example_todo)
        persisted_todo2 = self.db.create(self.example_todo)

        # when
        self.db.delete()
        all_todos = self.db.get_all()

        # then
        self.assertNotIn(persisted_todo1, all_todos)
        self.assertNotIn(persisted_todo2, all_todos)

    def test_delete_by_url(self):
        # given
        persisted_todo1 = self.db.create(self.example_todo)
        persisted_todo2 = self.db.create(self.example_todo)

        # when
        self.db.delete(persisted_todo1['url'])
        all_todos = self.db.get_all()

        # then
        self.assertNotIn(persisted_todo1, all_todos)
        self.assertIn(persisted_todo2, all_todos)

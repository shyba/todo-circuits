import unittest
from unittest import mock
from todo import Root


class TestCORS(unittest.TestCase):

    def test_root_controller_sets_CORS_for_index(self):
        # given
        root_controller = Root()
        request = mock.Mock()
        response = mock.Mock()

        headers = {}
        response.headers = headers

        # when
        root_controller.index(request, response)

        # then
        self.assertIn('Access-Control-Allow-Origin', headers)
        self.assertEqual('*', headers['Access-Control-Allow-Origin'])

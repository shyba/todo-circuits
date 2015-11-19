import unittest
from unittest import mock
from todo import Root


class TestCORS(unittest.TestCase):

    def test_root_controller_sets_CORS_for_index(self):
        # given
        root_controller = Root()
        root_controller.response = mock.Mock()
        headers = {}
        root_controller.response.headers = headers

        # when
        root_controller._set_CORS()

        # then
        self.assertIn('Access-Control-Allow-Origin', headers)
        self.assertEquals('*', headers['Access-Control-Allow-Origin'])

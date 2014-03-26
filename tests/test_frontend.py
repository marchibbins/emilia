import unittest

from emilia import init


class FrontendTests(unittest.TestCase):

    """ Tests for Frontend. """

    def setUp(self):
        self.app = init().test_client()

    def test_index(self):
        """ Tests that frontend route returns 200. """
        rv = self.app.get('/')
        self.assertTrue(rv.data)
        self.assertEqual(rv.status_code, 200)

    def test_favicon(self):
        rv = self.app.get('/static/favicon.ico')
        self.assertTrue(rv.data)
        self.assertEqual(rv.status_code, 200)
        rv.close()

    def test_generic_404(self):
        """ Tests that missing frontend route returns 404. """
        rv = self.app.get('/404/')
        self.assertEqual(rv.status_code, 404)

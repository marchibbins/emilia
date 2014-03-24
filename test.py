from manage import app
import unittest


class TestCase(unittest.TestCase):

    """ Base test case, common set up and tear down. """

    def setUp(self):
        self.app = app.test_client()


class FrontendTests(TestCase):

    """ Tests for Frontend blueprint. """

    def test_index(self):
        rv = self.app.get('/')
        self.assertTrue(rv.data)
        self.assertEqual(rv.status_code, 200)

    def test_generic_404(self):
        rv = self.app.get('/not-found/')
        self.assertEqual(rv.status_code, 404)


if __name__ == '__main__':
    unittest.main()

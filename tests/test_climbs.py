import inspect
import unittest

from emilia.climbs.models import Book


class BookModelTests(unittest.TestCase):

    """ """

    def test_init(self):
        """ Tests init takes slug, short name and long name. """
        args = inspect.getargspec(Book.__init__).args[1:]
        self.assertEqual(args, ['slug', 'short_name', 'long_name'])

    def test_required_fields(self):
        """ Tests slug, short name and long name cannot be blank. """
        self.assertFalse(Book.slug.property.columns[0].nullable)
        self.assertFalse(Book.short_name.property.columns[0].nullable)
        self.assertFalse(Book.long_name.property.columns[0].nullable)

    def test_unique_fields(self):
        """ Tests slug is unique. """
        self.assertTrue(Book.slug.property.columns[0].unique)

    def test_field_length_defaults(self):
        """ Tests model default string lengths are set. """
        self.assertEqual(Book.SLUG_STR_MAX, 32)
        self.assertEqual(Book.NAME_STR_MAX, 64)

    def test_field_lengths(self):
        """ Tests slug, short name and long name lengths are set. """
        self.assertEqual(Book.slug.property.columns[0].type.length, Book.SLUG_STR_MAX)
        self.assertEqual(Book.short_name.property.columns[0].type.length, Book.NAME_STR_MAX)
        self.assertEqual(Book.long_name.property.columns[0].type.length, Book.NAME_STR_MAX)

    def test_serialize(self):
        """ Test serialize returns correct id, slug, short name and long name. """
        book = Book('slug', 'Short name', 'Long name')
        keys = ['id', 'slug', 'short_name', 'long_name']
        serialized = book.serialize()
        self.assertEqual(serialized.keys().sort(), keys.sort())
        for key in keys:
            self.assertEqual(serialized[key], getattr(book, key))

    def test_repr(self):
        """ Tests repr contains class and short name. """
        book = Book('slug', 'Short name', 'Long name')
        self.assertIn(Book.__name__, book.__repr__())
        self.assertIn(book.short_name, book.__repr__())

    def test_unicode(self):
        """ Tests unicode matches short name. """
        book = Book('slug', 'Short name', 'Long name')
        self.assertEqual(book.short_name, book.__unicode__())

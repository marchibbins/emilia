import inspect
import unittest

from emilia.climbs.models import Book, Climb, Region


class BookModelTests(unittest.TestCase):

    """ Tests for Book model. """

    def test_init(self):
        """ Tests init takes correct arguments. """
        list = ['slug', 'short_name', 'long_name']
        args = inspect.getargspec(Book.__init__).args[1:]
        self.assertEqual(args, list)

    def test_required_fields(self):
        """ Tests required fields cannot be blank. """
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
        """ Tests slug, short name and long name string lengths are set. """
        self.assertEqual(Book.slug.property.columns[0].type.length, Book.SLUG_STR_MAX)
        self.assertEqual(Book.short_name.property.columns[0].type.length, Book.NAME_STR_MAX)
        self.assertEqual(Book.long_name.property.columns[0].type.length, Book.NAME_STR_MAX)

    def test_serializable(self):
        """ Tests model has serialize method. """
        self.assertIsNotNone(getattr(Book, 'serialize', None))

    def test_serialize(self):
        """ Tests serialize returns correct object. """
        book = self.book()
        serialized = book.serialize()
        serialized_keys = serialized.keys()
        serialized_keys.sort()
        keys = ['id', 'slug', 'short_name', 'long_name']
        keys.sort()
        self.assertEqual(serialized_keys, keys)
        for key in keys:
            self.assertEqual(serialized[key], getattr(book, key))

    def test_repr(self):
        """ Tests repr contains class and short name. """
        book = self.book()
        self.assertIn(Book.__name__, book.__repr__())
        self.assertIn(book.short_name, book.__repr__())

    def test_unicode(self):
        """ Tests unicode matches short name. """
        book = self.book()
        self.assertEqual(book.short_name, book.__unicode__())

    def book(self):
        """ Creates a new Book object for tests. """
        return Book('slug', 'Short name', 'Long name')


class ClimbModelTests(unittest.TestCase):

    """ Tests for Climb model. """

    def test_init(self):
        """ Tests init takes correct arguments. """
        list = ['slug', 'number', 'name', 'location', 'strava_id', 'book', 'region']
        args = inspect.getargspec(Climb.__init__).args[1:]
        self.assertEqual(args, list)

    def test_required_fields(self):
        """ Tests required fields cannot be blank. """
        self.assertFalse(Climb.slug.property.columns[0].nullable)
        self.assertFalse(Climb.number.property.columns[0].nullable)
        self.assertFalse(Climb.name.property.columns[0].nullable)
        self.assertFalse(Climb.location.property.columns[0].nullable)
        self.assertFalse(Climb.strava_id.property.columns[0].nullable)

    def test_unique_fields(self):
        """ Tests slug is unique. """
        self.assertTrue(Climb.slug.property.columns[0].unique)

    def test_field_length_defaults(self):
        """ Tests model default string lengths are set. """
        self.assertEqual(Climb.SLUG_STR_MAX, 32)
        self.assertEqual(Climb.NAME_STR_MAX, 64)
        self.assertEqual(Climb.LOCATION_STR_MAX, 64)

    def test_field_lengths(self):
        """ Tests slug, name and location string lengths are set. """
        self.assertEqual(Climb.slug.property.columns[0].type.length, Climb.SLUG_STR_MAX)
        self.assertEqual(Climb.name.property.columns[0].type.length, Climb.NAME_STR_MAX)
        self.assertEqual(Climb.location.property.columns[0].type.length, Climb.LOCATION_STR_MAX)

    def test_serializable(self):
        """ Tests model has serialize method. """
        self.assertIsNotNone(getattr(Climb, 'serialize', None))

    def test_serialize(self):
        """ Tests serialize returns correct object. """
        climb = self.climb()
        serialized = climb.serialize()
        serialized_keys = serialized.keys()
        serialized_keys.sort()
        keys = ['id', 'slug', 'number', 'name', 'location', 'strava_id', 'book_id', 'region_id']
        keys.sort()
        self.assertEqual(serialized_keys, keys)
        for key in keys:
            self.assertEqual(serialized[key], getattr(climb, key))

    def test_repr(self):
        """ Tests repr contains class and name. """
        climb = self.climb()
        self.assertIn(Climb.__name__, climb.__repr__())
        self.assertIn(climb.name, climb.__repr__())

    def test_unicode(self):
        """ Tests unicode matches name. """
        climb = self.climb()
        self.assertEqual(climb.name, climb.__unicode__())

    def climb(self):
        """ Creates a new Climb object for tests. """
        return Climb(1, 'slug', 'name', 'location', 1)


class RegionModelTests(unittest.TestCase):

    """ Tests for Region model. """

    def test_init(self):
        """ Tests init takes correct arguments. """
        list = ['slug', 'name']
        args = inspect.getargspec(Region.__init__).args[1:]
        self.assertEqual(args, list)

    def test_required_fields(self):
        """ Tests required fields cannot be blank. """
        self.assertFalse(Region.slug.property.columns[0].nullable)
        self.assertFalse(Region.name.property.columns[0].nullable)

    def test_unique_fields(self):
        """ Tests slug is unique. """
        self.assertTrue(Region.slug.property.columns[0].unique)

    def test_field_length_defaults(self):
        """ Tests model default string lengths are set. """
        self.assertEqual(Region.SLUG_STR_MAX, 32)
        self.assertEqual(Region.NAME_STR_MAX, 64)

    def test_field_lengths(self):
        """ Tests slug, name and location string lengths are set. """
        self.assertEqual(Region.slug.property.columns[0].type.length, Region.SLUG_STR_MAX)
        self.assertEqual(Region.name.property.columns[0].type.length, Region.NAME_STR_MAX)

    def test_serializable(self):
        """ Tests model has serialize method. """
        self.assertIsNotNone(getattr(Region, 'serialize', None))

    def test_serialize(self):
        """ Tests serialize returns correct object. """
        region = self.region()
        serialized = region.serialize()
        serialized_keys = serialized.keys()
        serialized_keys.sort()
        keys = ['id', 'slug', 'name']
        keys.sort()
        self.assertEqual(serialized_keys, keys)
        for key in keys:
            self.assertEqual(serialized[key], getattr(region, key))

    def test_repr(self):
        """ Tests repr contains class and name. """
        region = self.region()
        self.assertIn(Region.__name__, region.__repr__())
        self.assertIn(region.name, region.__repr__())

    def test_unicode(self):
        """ Tests unicode matches name. """
        region = self.region()
        self.assertEqual(region.name, region.__unicode__())

    def region(self):
        """ Creates a new Region object for tests. """
        return Region('slug', 'name')

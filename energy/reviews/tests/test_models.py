from django.test import TestCase

from reviews.models import Supplier, Review

class SupplierModelTestCase(TestCase):
    def setUp(self):
        self.ts1 = Supplier.objects.get_or_create(name="Test Supplier 1")[0]
        self.ts2 = Supplier.objects.get_or_create(name="Test Supplier 2")[0]
        self.ts3 = Supplier.objects.get_or_create(name="Test Supplier 3")[0]

    def test_has_slug(self):
        """ Suppliers slugs are generated correctly """
        self.assertEqual(self.ts1.slug, "test-supplier-1")
        self.assertEqual(self.ts2.slug, "test-supplier-2")
        self.assertEqual(self.ts3.slug, "test-supplier-3")

    def test_has_created(self):
        assert(hasattr(self.ts1, 'created'))

    def test_created_is_not_none(self):
        self.assertIsNotNone(self.ts1.created)

    def test_ts1_created_less_than_ts3_created(self):
        self.assertLess(self.ts1.created, self.ts3.created)


class ReviewModelTestCase(TestCase):
    def setUp(self):
        self.ts4 = Supplier.objects.get_or_create(name="Test Supplier 4")[0]
        self.ts5 = Supplier.objects.get_or_create(name="Test Supplier 5")[0]
        self.ts6 = Supplier.objects.get_or_create(name="Test Supplier 6")[0]
        self.tr1s4 = Review.objects.get_or_create(supplier=self.ts4, rating=1, author="Author 1", content="review1 for supplier4")[0]
        self.tr2s4 = Review.objects.get_or_create(supplier=self.ts4, rating=2, author="Author 2", content="review2 for supplier4")[0]
        self.tr3s4 = Review.objects.get_or_create(supplier=self.ts4, rating=3, author="Author 3", content="review3 for supplier4")[0]
        self.tr1s5 = Review.objects.get_or_create(supplier=self.ts5, rating=5, author="Author 4", content="review1 for supplier5")[0]

    def test_has_created(self):
        assert(hasattr(self.tr1s4, 'created'))

    def test_created_is_not_none(self):
        self.assertIsNotNone(self.tr1s4.created)

    def test_tr1s4_created_less_than_tr2s4_created(self):
        self.assertLess(self.tr1s4.created, self.tr2s4.created)


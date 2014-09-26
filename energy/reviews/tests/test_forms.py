# from django.core.urlresolvers import reverse
from django.test import TestCase

from reviews.models import Supplier, Review
# from reviews.views import SupplierListView, SupplierReviewListView, create_review
from reviews.forms import ReviewForm

class CreateReviewFormTestCase(TestCase):
    def setUp(self):
        self.ts1 = Supplier.objects.get_or_create(name="Test Supplier 1")[0]

    def test_valid_data(self):
        form = ReviewForm({
            'author': 'test author',
            'rating': 5,
            'content': "This is an awesome supplier!"
        })
        self.assertTrue(form.is_valid())
        test_review = form.save(commit=False)
        test_review.supplier = self.ts1
        test_review.save()
        self.assertEqual(test_review.author, 'test author')
        self.assertEqual(test_review.rating, 5)
        self.assertEqual(test_review.content, 'This is an awesome supplier!')
        self.assertEqual(test_review.status, 'draft')
        self.assertIs(test_review.supplier, self.ts1)

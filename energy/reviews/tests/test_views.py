from django.core.urlresolvers import reverse
from django.test import TestCase

from reviews.models import Supplier, Review
from reviews.views import SupplierListView, SupplierReviewListView, create_review

def create_supplier(name):
    """ Creates a new Supplier, with the given name """
    return Supplier.objects.create(name=name)

class SupplierListViewTestCase(TestCase):
    def test_empty_supplier_list_view(self):
        """ Show message when no suppliers are available """
        response = self.client.get(reverse('reviews:suppliers'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No suppliers are available")
        self.assertQuerysetEqual(response.context['object_list'], [])


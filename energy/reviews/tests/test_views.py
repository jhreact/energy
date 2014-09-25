from django.core.urlresolvers import reverse
from django.test import TestCase

from reviews.models import Supplier, Review
from reviews.views import SupplierListView, SupplierReviewListView, create_review

def create_supplier(name):
    """ Creates a new Supplier, with the given name """
    return Supplier.objects.get_or_create(name=name)[0]

class SupplierListViewTestCase(TestCase):
    def test_empty_supplier_list_view(self):
        """ Show message when no suppliers are available """
        response = self.client.get(reverse('reviews:suppliers'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No suppliers are available")
        self.assertQuerysetEqual(response.context['object_list'], [])

    def test_one_supplier_list_view(self):
        """ Supplier should display on the Suppliers page"""
        create_supplier("Supplier B")
        response = self.client.get(reverse('reviews:suppliers'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<title>Suppliers</title>")
        self.assertQuerysetEqual(response.context['object_list'], ['<Supplier: Supplier B>'])

    def test_suppliers_are_alphabetical_list_view(self):
        """ Supplier should display on the Suppliers page"""
        create_supplier("Supplier B")
        create_supplier("Supplier A")
        response = self.client.get(reverse('reviews:suppliers'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['object_list'], ['<Supplier: Supplier A>', '<Supplier: Supplier B>'])


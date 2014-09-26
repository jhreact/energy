from django.core.urlresolvers import reverse
from django.test import TestCase

from reviews.models import Supplier, Review
from reviews.views import SupplierListView, SupplierReviewListView, create_review

def create_supplier(name):
    """ Returns a new Supplier, with the given name """
    return Supplier.objects.get_or_create(name=name)[0]

def create_review(supplier, author, rating, content):
    """
    Returns a new Review, with the given supplier, author, rating, and content
    """
    return Review.objects.get_or_create(supplier=supplier, author=author,
            rating=rating, content=content)[0]

class BadUrlsViewTest(TestCase):
    def test_slash(self):
        """ Requests to / should 404 """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)


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

    def test_supplier_has_link_to_supplier_reviews(self):
        """ Supplier should link to reviews page"""
        create_supplier("Supplier A")
        response = self.client.get(reverse('reviews:suppliers'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<a href="/reviews/supplier-a/">Supplier A</a>')

    def test_suppliers_are_alphabetical_list_view(self):
        """ Supplier should display on the Suppliers page"""
        create_supplier("Supplier B")
        create_supplier("Supplier A")
        response = self.client.get(reverse('reviews:suppliers'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['object_list'], ['<Supplier: Supplier A>', '<Supplier: Supplier B>'])


class SupplierReviewListViewTestCase(TestCase):
    def test_supplier_review_unknown_slug(self):
        """ Should 404 if the slug is unknown"""
        response = self.client.get(reverse('reviews:supplier_reviews', kwargs={'slug': 'fake-slug'}))
        self.assertEqual(response.status_code, 404)

    def test_empty_supplier_review_list_view(self):
        """ Show message when no reviews are available for this supplier"""
        s1 = create_supplier("Supplier A")
        response = self.client.get(reverse('reviews:supplier_reviews', kwargs={'slug': s1.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are currently no reviews for this supplier")
        self.assertQuerysetEqual(response.context['object_list'], [])

    def test_supplier_review_list_view_has_correct_title(self):
        """ Make sure supplier review list has correct title"""
        s1 = create_supplier("Supplier A")
        response = self.client.get(reverse('reviews:supplier_reviews', kwargs={'slug': s1.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<title>{}</title>'.format(s1.name))

    def test_supplier_review_list_view_has_create_link(self):
        """ Make sure supplier review list has a create link """
        s1 = create_supplier("Supplier A")
        response = self.client.get(reverse('reviews:supplier_reviews', kwargs={'slug': s1.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<a href="/reviews/{}/write">Write a review for {}</a>'.format(s1.slug, s1.name))

    def test_supplier_with_only_draft_reviews(self):
        """ Shouldn't show reviews if they are unpublished """
        s1 = create_supplier("Supplier A")
        r1 = create_review(s1, "author 1", 1, "review 1 for supplier A")
        r2 = create_review(s1, "author 2", 2, "review 2 for supplier A")
        response = self.client.get(reverse('reviews:supplier_reviews', kwargs={'slug': s1.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are currently no reviews for this supplier")
        self.assertQuerysetEqual(response.context['object_list'], [])

    def test_reviews_are_most_recent_first(self):
        """ Most recent reviews should be first """
        s1 = create_supplier("Supplier A")
        r1 = create_review(s1, "author 1", 1, "review 1 for supplier A")
        r2 = create_review(s1, "author 2", 2, "review 2 for supplier A")
        r3 = create_review(s1, "author 3", 3, "review 3 for supplier A")
        r1.status="published"
        r1.save()
        r3.status="published"
        r3.save()
        response = self.client.get(reverse('reviews:supplier_reviews', kwargs={'slug': s1.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "review 1 for supplier A")
        self.assertContains(response, "review 3 for supplier A")
        self.assertQuerysetEqual(response.context['object_list'], ["<Review: {}>".format(str(r3)), "<Review: {}>".format(str(r1))])

class CreateReviewTestCase(TestCase):
    def test_create_review_unknown_slug(self):
        """ Create review should 404 if the slug is unknown"""
        response = self.client.get(reverse('reviews:create_review', kwargs={'slug': 'fake-slug'}))
        self.assertEqual(response.status_code, 404)



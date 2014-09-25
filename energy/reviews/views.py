from django.views.generic import ListView, CreateView

from .models import Supplier, Review

class SupplierListView(ListView):
    model = Supplier

    def get_queryset(self):
        return Supplier.objects.order_by('name')


class SupplierReviewListView(ListView):
    model = Review

    def get_queryset(self):
        slug = self.kwargs.get('slug', None)
        return Review.objects.published.filter(supplier__slug=slug).order_by('-created')


class SupplierReviewCreateView(CreateView):
    model = Review
    # slug = self.kwargs.get('slug', None)

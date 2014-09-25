from django.views.generic import ListView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import Supplier, Review

class SupplierListView(ListView):
    model = Supplier

    def get_queryset(self):
        return Supplier.objects.order_by('name')


class SupplierReviewListView(ListView):
    model = Review

    def get_queryset(self):
        slug = self.kwargs.get('slug', None)
        return Review.objects.published().filter(supplier__slug=slug).order_by('-created')

    def get_context_data(self, **kwargs):
        context = super(SupplierReviewListView, self).get_context_data(**kwargs)
        context['supplier'] = get_object_or_404(Supplier, slug=self.kwargs.get('slug'))
        return context

class SupplierReviewCreateView(CreateView):
    model = Review
    # slug = self.kwargs.get('slug', None)

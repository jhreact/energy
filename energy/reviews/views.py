from django.views.generic import ListView, CreateView
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import Supplier, Review
from .forms import ReviewForm

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

def create_review(request, slug):
    supplier = get_object_or_404(Supplier, slug=slug)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.supplier = supplier
            new_review.save()
            return HttpResponseRedirect(reverse('reviews:suppliers'))
    else:
        form = ReviewForm()
    return render(request, 'reviews/review_form.html', {'supplier': supplier, 'form': form})


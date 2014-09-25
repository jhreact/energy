from django.forms import ModelForm

from .models import Supplier, Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ('author', 'rating', 'content')

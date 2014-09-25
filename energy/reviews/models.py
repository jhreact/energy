from datetime import datetime

from django.db import models
from django.template.defaultfilters import slugify

class TimeStampedModel(models.Model):
    """
    Abstract base class model with auto-updating created and last modified fields
    """
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Supplier(TimeStampedModel):
    """ Model representing a Supplier """
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        # Only gen slug when creating object, so it doesn't change
        if not self.id:
            self.slug = slugify(self.name)
        super(Supplier, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class PublishedReviewManager(models.Manager):
    use_for_related_fields = True

    def published(self, *args, **kwargs):
        return self.filter(status='published', *args, **kwargs)

class Review(TimeStampedModel):
    """ Model representing a Review """
    RATING_CHOICES = [(rating, rating) for rating in range(1, 6)]
    STATUS_CHOICES = [(state, state) for state in ('draft', 'published')]

    supplier = models.ForeignKey(Supplier)
    rating = models.PositiveIntegerField(choices=RATING_CHOICES)
    author = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='draft')
    content = models.TextField()

    objects = PublishedReviewManager()

    def __str__(self):
        return "{}: {}".format(self.supplier.name, self.created.strftime('%Y-%m-%d %X'))

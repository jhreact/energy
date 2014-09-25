from django.conf.urls import patterns, include, url

from .views import SupplierListView, SupplierReviewListView, create_review

urlpatterns = patterns('',
    url(r'^$', SupplierListView.as_view(), name='suppliers'),
    url(r'^(?P<slug>[\w-]+)/$', SupplierReviewListView.as_view(), name='supplier_reviews'),
    url(r'^(?P<slug>[\w-]+)/write$', create_review, name='create_review'),
)

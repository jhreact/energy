from django.conf.urls import patterns, include, url

from .views import SupplierListView, SupplierReviewListView, SupplierReviewCreateView

urlpatterns = patterns('',
    url(r'^$', SupplierListView.as_view(), name='suppliers'),
    url(r'^(?P<slug>[\w-]+)/$', SupplierReviewListView.as_view(), name='supplier_reviews'),
    url(r'^(?P<slug>[\w-]+)/write$', SupplierReviewCreateView.as_view(), name='create_review'),
)

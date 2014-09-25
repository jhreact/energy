from django.conf.urls import patterns, include, url

from .views import SupplierListView, SupplierReviewListView, SupplierReviewCreateView

urlpatterns = patterns('',
    url(r'^$', SupplierListView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', SupplierReviewListView.as_view()),
    url(r'^(?P<slug>[\w-]+)/write$', SupplierReviewCreateView.as_view()),
)

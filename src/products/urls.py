from django.conf.urls import url

from .views import ProductListView, ProductDetailView, ProductFeaturedListView, ProductFeaturedDetailView

urlpatterns = [
    url(r'^$', ProductListView,name='list'),
    url(r'^featured/$', ProductFeaturedListView,name='f_list'),
    url(r'^featured/(?P<slug>[\w-]+)/$', ProductFeaturedDetailView,name='f_detail'),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailView,name='detail'),
]

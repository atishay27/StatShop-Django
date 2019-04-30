"""ecom2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include
from django.contrib import admin

# from products.views import ProductListView, ProductDetailView, ProductFeaturedListView, ProductFeaturedDetailView

from .views import home_page, contact_page, about_page, login_page, register_page, logout_page, password_change

urlpatterns = [
    url(r'^$', home_page,name='home'),
    url(r'^contact/$', contact_page,name='contact'),
    url(r'^about/$', about_page,name='about'),
    url(r'^login/$', login_page,name='login'),
    url(r'^logout/$', logout_page,name='logout'),
    url(r'^changepass/$', password_change,name='password_change'),
    url(r'^products/', include("products.urls",namespace='products')),
    url(r'^search/', include("search.urls",namespace='search')),
    # url(r'^products/$', ProductListView),
    # url(r'^products/(?P<slug>[\w-]+)/$', ProductDetailView),
    # # url(r'^products/(?P<slug>[\w-]+)/(?P<pk>\d+)/$', ProductDetailSlugView),
    # url(r'^featured/$', ProductFeaturedListView),
    # url(r'^featured/(?P<slug>[\w-]+)/$', ProductFeaturedDetailView),

    url(r'^register/$', register_page,name='register'),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

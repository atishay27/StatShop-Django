from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Product

def ProductFeaturedListView(request,slug=None, *args, **kwargs):
        instance = Product.objects.featured(slug)
        if instance is None:
            raise Http404("No Featured Product Available Currently")
        context = {
            'object_list' : instance
        }
        return render(request, "products/list.html", context)

def ProductFeaturedDetailView(request, slug=None, *args, **kwargs):
        instance = Product.objects.featured(slug)
        if instance is None:
            raise Http404("THIS IS NOT A FEATURED PRODUCT")

        context = {
            'object' : instance
        }
        return render(request, "products/featured-detail.html", context)


def ProductListView(request):
    queryset = Product.objects.all()
    context = {
        'object_list' : queryset
    }
    return render(request, "products/list.html", context)

def ProductDetailView(request, slug=None, *args, **kwargs):
    instance = Product.objects.get_by_slug(slug)
    if instance is None:
        raise Http404("Product Doesn't Exist")

    context = {
        'object' : instance
    }
    return render(request, "products/detail.html", context)

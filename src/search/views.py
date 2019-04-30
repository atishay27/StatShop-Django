from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product
# Create your views here.

def SearchProductView(request):
    query= request.GET.get('q')
    if query is not None:
        queryset = Product.objects.filter(title__icontains=query)
    else:
        queryset = Product.objects.none()
    context = {
        'object_list' : queryset
    }
    return render(request, "search/view.html", context)

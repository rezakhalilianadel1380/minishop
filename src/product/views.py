from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Product
# Create your views here.

class ProductListView(ListView):
    model = Product
    paginate_by = 30
    template_name = "shop-list.html"  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


    def get_queryset(self, *args, **kwargs):
        products=Product.objects.all()
        return products
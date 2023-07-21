from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Product
# Create your views here.

class ProductListView(ListView):
    model = Product
    paginate_by = 2
    template_name = "shop-list.html"  
    context_object_name = "product_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator=context['paginator']
        page_obj=context["page_obj"]
        page_obj.adjusted_elided_pages = paginator.get_elided_page_range(page_obj.number)
        context['page_obj']=page_obj
        return context


    def get_queryset(self, *args, **kwargs):
        products=Product.objects.all()
        return products
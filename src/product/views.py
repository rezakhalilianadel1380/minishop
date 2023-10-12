from django.shortcuts import render
from django.views.generic.list import ListView
from category.models import Category
from .models import Product

# from django.db import connections,reset_queries
# Create your views here.

class ProductListView(ListView):
    model = Product
    paginate_by = 10
    template_name = "shop-list.html"  
    context_object_name = "product_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request=self.request
        paginator=context['paginator']
        page_obj=context["page_obj"]
        page_obj.adjusted_elided_pages = paginator.get_elided_page_range(page_obj.number)
        context['page_obj']=page_obj
        categories=Category.objects.filter(depth=0,is_root=True)
        context['maincategories']=categories
        maincategory=request.GET.get('maincategory')
        if maincategory:
            sub_category=Category.objects.filter(sub_category__title_en=maincategory,depth=1)
            context['subcategory']=sub_category
        subcategory=request.GET.get('subcategory')
        if subcategory:
            tirdcategory=Category.objects.filter(sub_category__title_en=subcategory,depth=2)
            context['thirdcategory']=tirdcategory
        return context
    

    def get_queryset(self, *args, **kwargs):
        request=self.request
        products=Product.objects.all()
        
        maincategory=request.GET.get('maincategory')
        if maincategory:
            products=products.filter(category_1__title_en=maincategory,category_1__depth=0)
        subcategory=request.GET.get('subcategory')
        if subcategory:
            products=products.filter(category_2__title_en=subcategory,category_2__depth=1)
        thirdcategory=request.GET.get('thirdcategory')
        if thirdcategory:
            products=products.filter(category_3__title_en=thirdcategory,category_3__depth=2)
        return products
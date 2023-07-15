from django.contrib import admin
from .models import Product,ProductAttr,ProductGallery,ProductVarient,Size,Color
# Register your models here.



class ProductAttrInline(admin.TabularInline):
    model=ProductAttr
    can_delete=True

class ProcutGalleryInline(admin.TabularInline):
    model=ProductGallery
    can_delete=True

class ProductVarientInline(admin.TabularInline):
    model=ProductVarient
    can_delete=True


class ProductAdmin(admin.ModelAdmin):
    inlines = [
       ProductAttrInline,
       ProcutGalleryInline,
       ProductVarientInline,
    ]


admin.site.register(Product,ProductAdmin)
admin.site.register(Size)
admin.site.register(Color)

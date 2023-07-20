from django.core.validators import RegexValidator,MinValueValidator,MaxValueValidator
from django.db import models
from django.utils.text import slugify
from category.models import Category
from django.contrib.humanize.templatetags.humanize import intcomma
# Create your models here.

product_varient=(
    ("color","رنگ"),
    ("size","اندازه")
)

class Product(models.Model):
    title_fa=models.CharField(max_length=100,null=True)
    title_en=models.CharField(max_length=100,null=True)
    description=models.TextField()
    image=models.ImageField(upload_to = 'products/')
    slug_url=models.SlugField(max_length=100,unique=True, blank=True)
    product_varient=models.CharField(choices=product_varient,max_length=50,null=True,blank=True)
    category_1=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,related_name='rootcategory')
    category_2=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,related_name='secound_category')
    category_3=models.ForeignKey(Category,null=True,blank=True,on_delete=models.SET_NULL,related_name='third_category')
    category_4=models.ForeignKey(Category,null=True,blank=True,on_delete=models.SET_NULL,related_name='forth_category')

    def save(self, *args, **kwargs):
        self.slug_url = slugify(self.title_fa)
        super(Product, self).save(*args, **kwargs)

    def get_price_with_discount(self):
        varient=self.productvarient_set.filter(is_deafult=True).first()
        discount_percent=varient.dicount_percent
        varient_price=int(varient.price)
        total_price= varient_price - int(varient_price*(discount_percent/100))
        return intcomma(total_price)

    def get_price(self):
        varient=self.productvarient_set.filter(is_deafult=True).first()
        return intcomma(varient.price)

    def __str__(self) -> str:
        return self.title_fa

class ProductGallery(models.Model):
    image=models.ImageField(upload_to = 'products_gallery/')
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    title=models.CharField(max_length=20,null=True,blank=True)

    def __str__(self) -> str:
        return self.product_id.title_fa
    


class ProductAttr(models.Model):
    key=models.CharField(max_length=50)
    value=models.CharField(max_length=50)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.key

class Size(models.Model):
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title
    

class Color(models.Model):
    title_fa=models.CharField(max_length=20)
    title_en=models.CharField(max_length=20)
    hex_code=models.CharField(max_length=7,default="#ffffff",validators=[RegexValidator(regex="^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$")])


    def __str__(self) -> str:
        return self.title_fa


variant_types=(
    ('color','رنگ'),
    ('size','اندازه'),
)

class ProductVarient(models.Model):
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    size_id=models.ForeignKey(Size,on_delete=models.SET_NULL,null=True,blank=True)
    color_id=models.ForeignKey(Color,on_delete=models.SET_NULL,null=True,blank=True)
    weight=models.IntegerField(default=0,help_text="واحد به گرم میباشد")
    dicount_percent=models.IntegerField(default=0,validators=[MinValueValidator(0,'بازه اعداد باید بالاتر صفر باشد '),MaxValueValidator(100,"تخفیف بالاتر از عدد 100 مجاز نیست ")])
    price=models.DecimalField(max_digits=13,decimal_places=0)
    is_deafult=models.BooleanField(default=False)
    quantity=models.IntegerField(default=1,help_text="موجودیت")
    

    def  __str__(self) -> str:
        return self.product_id.title_fa
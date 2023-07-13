from django.db import models

# Create your models here.


class Category(models.Model):
    title_fa=models.CharField(max_length=50)
    title_en=models.CharField(max_length=50)
    sub_category=models.ForeignKey('category.Category',on_delete=models.CASCADE,null=True,blank=True)
    is_root=models.BooleanField(default=True)


    def __str__(self) -> str:
        return self.title_fa
    
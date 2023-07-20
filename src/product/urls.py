from django.urls import path,include
from .views import ProductListView

urlpatterns = [
    path('product/list',ProductListView.as_view()),
]


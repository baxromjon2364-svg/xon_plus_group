from django.urls import path
from . import views
from .views import index_view,all_products_view,product_detail_view
urlpatterns=[
    path('',index_view,name='home'),
    path('all_products',all_products_view, name='all_products'),
    path('uskunalar/<int:pk>/', views.product_detail_view, name='product_detail'),
]
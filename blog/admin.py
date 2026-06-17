from django.contrib import admin
from .models import Product,OrderRequest,CompletedProject
# Register your models here.
admin.site.register(Product)
admin.site.register(OrderRequest)
admin.site.register(CompletedProject)
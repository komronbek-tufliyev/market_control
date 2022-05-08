from django.contrib import admin
from .models import Product, Category, Business


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'farm_name', 'date_created', 'experied_date', 'price', 'amount', 'description', 'is_active', 'is_bestseller', 'is_featured']
    list_filter = ['category', 'is_active', 'is_bestseller', 'is_featured']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_created', 'description']
    list_filter = ['name']

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'email', 'phone', 'address', 'date_created', 'description', 'is_active']
    list_filter = ['name']


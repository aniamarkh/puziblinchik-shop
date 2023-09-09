from django.contrib import admin

from .models import Merch, Category


@admin.register(Merch)
class MerchAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'date', 'stock']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

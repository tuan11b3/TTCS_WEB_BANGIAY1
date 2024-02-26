from django.contrib import admin
from .models import Product


# specify field dis
class ShoeAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "discount",)

# Register your models here.
admin.site.register(Product, ShoeAdmin)
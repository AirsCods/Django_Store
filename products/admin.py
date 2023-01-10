from django.contrib import admin
from products import models

# Register your models here.
admin.site.register(models.ProductCategory)


@admin.register(models.Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('image', 'name', 'description', ('price', 'quantity'), 'category')
    readonly_fields = ('description',)
    search_fields = ('name', 'category')
    ordering = ('name', '-price')


class BasketAdmin(admin.TabularInline):
    model = models.Basket
    fields = ('product', 'quantity',)
    extra = 0

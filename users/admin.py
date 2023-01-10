from django.contrib import admin
from users import models
from products.admin import BasketAdmin


# Register your models here.

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name')
    # fields = ('')
    inlines = (BasketAdmin,)

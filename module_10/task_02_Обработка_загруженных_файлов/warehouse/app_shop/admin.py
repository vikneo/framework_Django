from django.contrib import admin
from app_shop.models import Shop


class ShopAdmin(admin.ModelAdmin):
    list_display = ['title', 'code', 'price']


admin.site.register(Shop, ShopAdmin)

from django.contrib import admin
from advertisements.models import Advertisement, Heading, UsersInfo


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'price_exch']
    list_filter = ['title']
    search_fields = ['descriptions']


class HeadingAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',]
    list_filter = ['name']


admin.site.register(Heading, HeadingAdmin)
admin.site.register(UsersInfo, UserInfoAdmin)

from django.contrib import admin

from app_news.models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'descriptions', 'created_at', 'get_activated', 'status']
    list_filter = ['title', 'created_at']
    list_display_links = ['created_at']
    list_editable = ['status']

    actions = ['mark_as_active', 'mark_as_not_active']

    def mark_as_active(self, request, queryset):
        queryset.update(status='a', activated=True)

    def mark_as_not_active(self, request, queryset):
        queryset.update(status='n', activated=False)

    def get_activated(self, request):
        if request.status.lower() == 'a':
            News.objects.filter(id=request.id).update(activated=True)
        else:
            News.objects.filter(id=request.id).update(activated=False)

        return News.objects.get(id=request.id).activated

    mark_as_active.short_description = 'Установить как Активно'
    mark_as_not_active.short_description = 'Установить как Неактивно'
    get_activated.short_description = 'Статус'


admin.site.register(News, NewsAdmin)

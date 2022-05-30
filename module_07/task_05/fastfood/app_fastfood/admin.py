from django.contrib import admin
from app_fastfood.models import Restaurant, Waiter


class WaiterIncline(admin.StackedInline):
    model = Waiter


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'city']
    list_filter = ['name']
    inlines = [WaiterIncline]


class WaiterAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'person_num', 'status_employ']
    list_filter = ['last_name', 'first_name']
    search_fields = ['last_name']

    actions = ['mark_as_accepted', 'mark_as_fired', 'mark_as_sick_list', 'mark_as_holiday']

    def mark_as_accepted(self, request, queryset):
        queryset.update(status_employ='a')

    def mark_as_fired(self, request, queryset):
        queryset.update(status_employ='f')

    def mark_as_sick_list(self, request, queryset):
        queryset.update(status_employ='s')

    def mark_as_holiday(self, request, queryset):
        queryset.update(status_employ='h')

    mark_as_accepted.short_description = 'Перевод в статус Принят'
    mark_as_fired.short_description = 'Перевод в статус Уволен'
    mark_as_sick_list.short_description = 'Перевод в статус Больничный'
    mark_as_holiday.short_description = 'Перевод в статус Отпуск'

    fieldsets = (
        ('Основные сведения', {
            'fields': ('last_name', 'first_name', 'second_name', 'city'),
        }),
        ('Биографические сведения', {
            'fields': ('age', 'sex', 'birth_date', 'education', 'country'),
            'description': 'Данные из биографии',
            'classes': ['collapse']
        }),
        ('Контакты для связи', {
            'fields': ('phone', 'mail_address'),
            'description': 'Обратная связь',
            'classes': ['collapse']
        }),
        ('Трудовая деятельность', {
            'fields': ('employment_date', 'person_num', 'salary'),
            'description': 'Трудоустройство'
        })
    )


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Waiter, WaiterAdmin)

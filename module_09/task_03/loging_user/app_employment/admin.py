from django.contrib import admin

from app_employment.models import Vacancy

from app_employment.models import Resume


class VacancyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['title']


class ResumeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['title']


admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Resume, ResumeAdmin)

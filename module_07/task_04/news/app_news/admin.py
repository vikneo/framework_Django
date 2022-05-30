from django.contrib import admin
from app_news.models import News, Commentaries


class CommentInline(admin.TabularInline):
    model = Commentaries


class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date', 'flag_news']
    list_filter = ['name', 'flag_news']
    inlines = [CommentInline]


class CommentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'comment']
    list_filter = ['user_name']


admin.site.register(News, NewsAdmin)
admin.site.register(Commentaries, CommentsAdmin)



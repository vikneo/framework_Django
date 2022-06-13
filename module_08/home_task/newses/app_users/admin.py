import re

from django.contrib import admin

from app_users.models import Comments


class CommentAdmin(admin.ModelAdmin):
    list_display = ['users', 'get_comments', 'news']
    list_filter = ['users']
    list_display_links = ['get_comments']

    actions = ['mark_as_delete']

    def get_comments(self, request):
        reduce = re.findall(r'.', request.comments)
        if len(reduce) > 15:
            request.comments = ''.join(reduce[i] for i in range(15)) + ' ...'
        return request.comments

    def mark_as_delete(self, request, queryset):
        queryset.update(comments='Удалено администратором')

    get_comments.short_description = 'Комментарий'
    mark_as_delete.short_description = 'Удалить комментарий'


admin.site.register(Comments, CommentAdmin)

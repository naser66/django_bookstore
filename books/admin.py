from django.contrib import admin

from .models import Book, Comment


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'author', )


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'text', 'datetime_create', 'recommend', 'is_active', )


admin.site.register(Book, BookAdmin)
admin.site.register(Comment, CommentAdmin)

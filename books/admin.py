from django.contrib import admin

from .models import Book, Comment
# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'text', 'datetime_create', )


admin.site.register(Book)
admin.site.register(Comment, CommentAdmin)

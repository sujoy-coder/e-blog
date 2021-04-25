from django.contrib import admin
from .models import Comment, Post

# register Post model
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    ordering = ('-date_posted',)
    readonly_fields  = ('date_posted',)
    list_display = ('title', 'user')

# register Comment model
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    ordering = ('-date_commented',)
    readonly_fields  = ('date_commented',)
    list_display = ('msg', 'user', 'post')
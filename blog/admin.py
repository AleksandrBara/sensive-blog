from django.contrib import admin
from blog.models import Post, Tag, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ('author', 'likes', 'tags')


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ('author', 'post')
    list_display = ('author', 'post', 'text')



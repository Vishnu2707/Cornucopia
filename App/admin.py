from django.contrib import admin

# Register your models here.
from .models import Post
from django.utils.html import format_html

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on', 'id', 'image')
    list_filter = ('status',)
    search_fields = ('title', 'content')

admin.site.register(Post, PostAdmin)



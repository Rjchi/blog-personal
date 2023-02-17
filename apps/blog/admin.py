from django.contrib import admin
from .models import Post

class BlogAdmin(admin.ModelAdmin):
    list_display =  ('id', 'title', 'category')

    list_display_links =  ('title', )

    list_per_page = 25

admin.site.register(Post, BlogAdmin)

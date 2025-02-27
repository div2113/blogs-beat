from django.contrib import admin
from .models import Blog
# Register your models here.

# admin.site.register(Blog)

class BlogAdmin(admin.ModelAdmin):
    list_display=["title","description","created_at","updated_at","image","like_count","user"]
    list_filter=["created_at","updated_at"]
    search_fields=["title","description","created_at","updated_at","image","like_count","user__username"]

admin.site.register(Blog,BlogAdmin)
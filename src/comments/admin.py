from django.contrib import admin
from .models import Comment
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display=["user","blog","content","created_at"]
    list_filter=["created_at"]
    search_fields=["user__username","blog__title","content"]

admin.site.register(Comment,CommentAdmin)
from django.contrib import admin
from .models import Comment
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display=["user","blog","content","created_at","blog_owner"]
    list_filter=["created_at"]
    search_fields=["user__username","blog__title","content"]

    def blog_owner(self,obj):
        return obj.blog.user.username
    blog_owner.admin_order_field='blog_user'  #allows sorting
    blog_owner.short_description='Blog Owner'   # Renames the column header

admin.site.register(Comment,CommentAdmin)
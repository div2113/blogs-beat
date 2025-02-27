from django.contrib import admin
from .models import Like
# Register your models here.

class LikeAdmin(admin.ModelAdmin):
    list_display=["user","blog"]
    list_filter=["user__username","blog__title"]
    search_fields=["user__username","blog__title"]


admin.site.register(Like,LikeAdmin)

from django.contrib import admin
from .models import Like
# Register your models here.

class LikeAdmin(admin.ModelAdmin):
    list_display=["user","blog"]
    list_filter=["user__username","blog__title"]
    search_fields=["user__username","blog__title"]

    def save_model(self, request, obj, form, change):
        if not change:
            if Like.objects.filter(user=obj.user,blog=obj.blog).exists():
                self.message_user(request,"This user already liked this blog.", level='ERROR')
                return
            obj.save()
            obj.blog.like_count += 1
            obj.blog.save()
        else:
            obj.save()

admin.site.register(Like,LikeAdmin)

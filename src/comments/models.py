from django.db import models
from django.contrib.auth.models import User
from blog.models import Blog

class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    content=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    

    class Meta:
        db_table="comments"

    def __str__(self):
        return self.content


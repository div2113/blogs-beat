from django.db import models
from django.contrib.auth.models import User
from blog.models import Blog

class Like(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)

    class Meta:
        db_table="likes"

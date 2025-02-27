from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title=models.CharField(max_length=150)
    description=models.CharField(max_length=255)
    image=models.ImageField(upload_to="blogs/")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    like_count=models.IntegerField(default=0)
    user=models.ForeignKey(User,on_delete=models.CASCADE)


    class Meta:
        db_table="blogs"

    def __str__(self):
        return self.title


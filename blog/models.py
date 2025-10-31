from django.db import models

from django.contrib.auth.models import User

class Post(models.Model):
    Title=models.CharField(max_length=200)
    content=models.TextField()
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updatd_at=models.DateTimeField(auto_now=True)


    def _str_(self):
        return self.title


from django.db import models
from django.contrib.auth.models import AbstractUser


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    avatar = models.ImageField(upload_to='user/avatar/', default='news/user/user.png')

    def __str__(self): return self.username


class Categoriy(AbstractBaseModel):
    name = models.CharField(max_length=70)
    
    def __str__(self): return self.name


class New(AbstractBaseModel):
    title = models.CharField(max_length=125)
    content = models.TextField(max_length=350)
    descriptions = models.TextField()
    img = models.ImageField(upload_to="news/")
    categoriy = models.ForeignKey(Categoriy, models.CASCADE)

    def __str__(self): return self.title


class Post(AbstractBaseModel):
    title = models.CharField(max_length=125)
    content = models.TextField(max_length=350)
    description = models.TextField()
    author = models.ForeignKey(User, models.CASCADE)

    def __str__(self): return self.title
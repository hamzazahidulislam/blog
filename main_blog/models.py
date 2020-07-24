from django.db import models

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,blank=True,null=True)
    image = models.ImageField(upload_to='post')
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='product')
    price = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='product')
    price = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):

        return self.name
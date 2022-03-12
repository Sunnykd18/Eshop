from django.db import models
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=150, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/products/')

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_product():
        return Product.objects.all()

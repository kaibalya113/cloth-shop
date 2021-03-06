from django.db import models
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default='', null=True, blank=True)
    image = models.ImageField(upload_to='uploads/products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    @staticmethod
    def getAllProducts():
        return Product.objects.all()

    @staticmethod
    def getAllProductsById(categoryId):
        if categoryId:
            return Product.objects.filter(category = categoryId)
        else:
            return Product.getAllProducts()

    @staticmethod
    def getProductById(productID):
        return Product.objects.filter(id__in = productID)
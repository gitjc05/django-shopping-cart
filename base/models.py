from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )
    sizes = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name
    
class UserItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name1 = models.CharField(max_length=200)
    user = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=200, null=True)

    
    def __str__(self):
        return self.product.name
    

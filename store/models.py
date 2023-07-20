from django.db import models

from users.models import User
from decimal import Decimal 


class Supplier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Season(models.Model):
    name = models.CharField(max_length=120, unique=True)
    description = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Drop(models.Model):
    name = models.CharField(max_length=120, unique=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=120, unique=True)
    sortno = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('decline', 'Decline'),
        ('approved', 'Approved'),
        ('processing', 'Processing'),
        ('complete', 'Complete'),
        ('bulk', 'Bulk'),
    )
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    design = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, null=True)
    season = models.ForeignKey(Season, on_delete=models.CASCADE, null=True)
    drop = models.ForeignKey(Drop, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)
    commission = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    created_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.product.name

    def save(self, *args, **kwargs):
        if not self.commission:
            self.commission = self.product.price * Decimal('0.05')  # Calculate 5% commission
        super().save(*args, **kwargs)

class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    courier_name = models.CharField(max_length=120)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.courier_name
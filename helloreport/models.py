from django.db import models
import uuid
from decimal import Decimal
from django.db.models import Avg, Sum



class Supplier(models.Model):
    supplier_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    company_name = models.CharField(max_length=100)
    status_choices = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )
    status = models.CharField(max_length=10, choices=status_choices)

    def __str__(self):
        return self.name

        
class Customers(models.Model):
    supplier_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    company_name = models.CharField(max_length=100)
    status_choices = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )
    status = models.CharField(max_length=10, choices=status_choices)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.CharField(max_length=100)
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    item_model = models.CharField(max_length=100)
    unit = models.CharField(max_length=50)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name

class Purchase(models.Model):
    purchase_no = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    date = models.DateField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_paid = models.DecimalField(max_digits=10, decimal_places=2)
    total_due = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
      
    status_choices = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )
    status = models.CharField(max_length=10, choices=status_choices)

    def save(self, *args, **kwargs):
        self.subtotal = self.purchase_price * self.quantity
        self.total_due = self.subtotal - self.total_paid
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.purchase_no)
    
    
    

class Sale(models.Model):
    quotation_no = models.CharField(max_length=20)
    quotation_date = models.DateField()
    quantity = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=20)

    # Foreign keys to Client and Product models
    customers = models.ForeignKey(Customers, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 

    def save(self, *args, **kwargs):
        # Calculate the subtotal before saving the Quotation instance
        self.subtotal = self.quantity * self.product.selling_price
        super(Sale, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.quotation_no} - {self.customers} - {self.product}"


# class ProfitReport(models.Model):
#     # Custom model for the profit report
#     total_purchase_subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     total_sale_subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     profit = models.DecimalField(max_digits=10, decimal_places=2, default=0)

#     @classmethod
#     def calculate_profit(cls):
#         # Calculate the total purchase subtotal
#         total_purchase_subtotal = Purchase.objects.aggregate(total_purchase_subtotal=Sum('subtotal'))['total_purchase_subtotal'] or 0

#         # Calculate the total sale subtotal
#         total_sale_subtotal = Sale.objects.aggregate(total_sale_subtotal=Sum('subtotal'))['total_sale_subtotal'] or 0

#         # Calculate the profit
#         profit = total_sale_subtotal - total_purchase_subtotal

#         return total_purchase_subtotal, total_sale_subtotal, profit
from django.db import models
from authentication.models import User
from datetime import timedelta
from datetime import datetime

#created a function for generating unique purchase order id
from .generate import generate_order_id


# Create your models here.
    
class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    vendor_code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)
    address = models.TextField()
    contact_details = models.TextField()
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    def __str__(self) -> str:
        return self.user.username


class PurchaseOrder(models.Model):
    STATUS = [
        ('pending', 'pending'),
        ('completed', 'completed'),
        ('canceled', 'canceled'),
    ]

    po_number = models.CharField(max_length=50, default=generate_order_id)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(null=True, blank=True)
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS, default='pending')
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)


    def save(self, *args, **kwargs):
        # If delivery_date is not set, calculate it based on order_date + 7 days
        if not self.delivery_date:
            self.delivery_date = datetime.now() + timedelta(days=7)
        
        
        super().save(*args, **kwargs)


class Performance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    def __str__(self) -> str:
        return self.vendor.user.username

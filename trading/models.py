from django.db import models

class Order(models.Model):
    order_id = models.CharField(max_length=255)
    transaction_type = models.CharField(max_length=10)
    symbol = models.CharField(max_length=10)
    quantity = models.IntegerField()
    price = models.FloatField()
    status = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

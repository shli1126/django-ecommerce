from django.conf import settings
from django.db import models


class Item(models.Model):
    RETURN_POLICY_CHOICES = [
        ("return_refund", "Eligible for return and refund"),
        ("return_partial_refund", "Eligible for return and partial refund"),
        ("no_return_refund", "Not eligible for return and refund"),
    ]
    title = models.CharField(max_length=100)
    price = models.FloatField()
    # -discount%
    discount = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    retailer = models.CharField(max_length=100, default="ecommerce")
    return_policy = models.CharField(
        max_length=100, choices=RETURN_POLICY_CHOICES, default="return_refund"
    )

    def __str__(self):
        return self.title


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Order(models.Model):
    # whos order
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # contain what items
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

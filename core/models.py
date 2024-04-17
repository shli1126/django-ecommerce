from django.conf import settings
from django.db import models
from django.utils import timezone


class Item(models.Model):
    RETURN_POLICY_CHOICES = [
        ("return_refund", "Eligible for return and refund"),
        ("return_partial_refund", "Eligible for return and partial refund"),
        ("no_return_refund", "Not eligible for return and refund"),
    ]
    CATEGORY_CHOICES = [
        ("general", "General"),
        ("clothing", "Clothing"),
        ("electronics", "Electronics"),
        ("books", "Books"),
        ("hone", "Home"),
        ("sport", "Sporting goods"),
        ("art", "Collections & arts"),
        ("motor", "Motors"),
        ("bussiness", "Bussiness & Industrial"),
    ]

    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    retailer = models.CharField(max_length=100, default="ecommerce")
    category = models.CharField(
        max_length=100, choices=CATEGORY_CHOICES, default="general"
    )
    return_policy = models.CharField(
        max_length=100, choices=RETURN_POLICY_CHOICES, default="return_refund"
    )

    def __str__(self):
        return self.title

'''
Order that has ordered = False can be seen as a shopping cart. 
OrderItem is the object in Order
'''
class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.title


#Order contain order items 
class Order(models.Model):
    # whos order
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    # contain what items
    items = models.ManyToManyField(OrderItem)
    ordered_date = models.DateTimeField(null=True, blank=True)
    ordered = models.BooleanField(default=False)
    # ordered_date is only set when the ordered is true
    def save(self, *args, **kwargs):
        if self.ordered and not self.ordered_date:
            self.ordered_date = timezone.now()
        super(Order, self).save(*args, **kwargs)
            
    def __str__(self):
        return self.user.username

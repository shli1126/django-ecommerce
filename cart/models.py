from django.db import models
from django.conf import settings
from core.models import Item


class CartItem(models.Model):
    cart = models.ForeignKey(
        "Cart", related_name="cart_items", on_delete=models.CASCADE
    )
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.name}"  # Make sure this uses `item.name`, not `product.name`


class Cart(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cart"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField(
        Item, through="CartItem", related_name="carts"
    )  # Specify through model

    def __str__(self):
        return f"Cart for {self.user.username}"

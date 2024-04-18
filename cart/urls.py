from django.urls import path
from .views import add_to_cart, delete_from_cart, get_all_items, update_quantity

app_name = "cart"
urlpatterns = [
    path("cart/get-all-items/", get_all_items, name="get-all-items"),
    path("cart/add-to-cart/<int:item_id>/", add_to_cart, name="add-to-cart"),
    path(
        "cart/delete-from-cart/<int:item_id>/",
        delete_from_cart,
        name="delete-from-cart",
    ),
    path(
        "cart/update-item-quantity/<int:item_id>/",
        update_quantity,
        name="update-quantity",
    ),
]

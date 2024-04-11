from django.urls import path
from .views import (
    item_list,
    item_detail,
    item_create,
    item_update,
    item_delete,
    add_to_cart
)

app_name = "core"
urlpatterns = [
    path("items/", item_list, name="item-list"),
    path("item/<int:pk>/", item_detail, name="item-detail"),
    path("item/create/", item_create, name="item-create"),
    path("item/update/<int:pk>/", item_update, name="item-update"),
    path("item/delete/<int:pk>/", item_delete, name="item-delete"),
    # path("cart/", CartView.as_view(), name="cart-detail"),
    path('add-to-cart/<int:item_id>/', add_to_cart, name='add-to-cart'),
]

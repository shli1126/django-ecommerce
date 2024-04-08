from django.urls import path
from .views import item_list, item_detail, item_create, item_update, item_delete

app_name = "core"
urlpatterns = [
    path("items", item_list, name="item-list"),
    path("item/<int:pk>/", item_detail, name="item-detail"),
    path('item/create/', item_create, name='item-create'),
    path('item/update/<int:pk>/', item_update, name='item-update'),
    path('item/delete/<int:pk>/', item_delete, name='item-delete'),
]

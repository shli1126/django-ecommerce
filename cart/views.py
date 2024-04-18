from django.shortcuts import render
from cart.models import Cart, CartItem
from core.models import Item
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.authentication import (
    SessionAuthentication,
    TokenAuthentication,
    BasicAuthentication,
)
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404



@api_view(["GET"])
@authentication_classes(
    [SessionAuthentication, TokenAuthentication, BasicAuthentication]
)
@permission_classes([IsAuthenticated])
def get_all_items(request):
    cart = get_object_or_404(Cart, user=request.user)
    items = CartItem.objects.filter(cart=cart)
    item_list = [{'item_id': item.id, 'item_name': item.item.title, 'quantity': item.quantity} for item in items]
    return Response({'items': item_list})




@api_view(["POST"])
@authentication_classes(
    [SessionAuthentication, TokenAuthentication, BasicAuthentication]
)
@permission_classes([IsAuthenticated])
def add_to_cart(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return Response(
        {
            "status": "item added to cart",
            "item_id": item_id,
            "quantity": cart_item.quantity,
        }
    )



@api_view(["DELETE"])
@authentication_classes(
    [SessionAuthentication, TokenAuthentication, BasicAuthentication]
)
@permission_classes([IsAuthenticated])
def delete_from_cart(request, item_id):
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        return Response({"error": "No cart found for this user"}, status=404)

    cart_item = get_object_or_404(CartItem, id=item_id, cart=cart)
    cart_item.delete()
    return Response({"status": "item deleted from cart", "item_id": item_id})

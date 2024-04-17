from django.shortcuts import render
from cart.models import Cart, CartItem
from core.models import Item
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated  
from django.shortcuts import get_object_or_404
from rest_framework import status


@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def add_to_cart(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item) 
 
    if not created:
        cart_item.quantity += 1  
        cart_item.save()

    return Response({'status': 'item added to cart', 'item_id': item_id, 'quantity': cart_item.quantity})

from rest_framework.response import Response
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token

@api_view(['POST', 'GET'])
def register(request):
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"detail": "GET method not allowed for registration."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
@api_view(['POST'])
def login(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


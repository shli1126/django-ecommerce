from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class CustomUser(AbstractBaseUser):
    BUYER = 'buyer'
    SELLER = 'seller'
    ROLE_CHOICES = [
        (BUYER, 'Buyer'),
        (SELLER, 'Seller'),
    ]
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    profile_image = models.ImageField(upload_to='profile_images/')
    bio = models.TextField()
    is_verified = models.BooleanField(default=False)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=BUYER)
    


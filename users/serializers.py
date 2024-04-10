from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate

User = get_user_model()
class UserRegistrationSerializer(serializers.ModelSerializer):
    # write_only to ensure is not included in any serialized output
    password = serializers.CharField(write_only=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True)  
    profile_image = serializers.ImageField(required=False, allow_null=True, use_url=True)
    
    class Meta:
        model = User
        fields = ('email', 'password', 'confirm_password', 'profile_image', 'bio', 'is_verified', 'role')
    
    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"confirm_password": "Password fields didn't match."})
        data.pop('confirm_password', None)
        return data

    def create(self, validated_data):
        print(validated_data)
        # ** to unpack
        user = User.objects.create_user(**validated_data)
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        try:
            user = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            raise serializers.ValidationError("The email is not registered")
        
        user = authenticate(username=data['email'], password=data['password'])
        if user and user.is_active:
            return user
        
        raise serializers.ValidationError("Incorrect Credentials")


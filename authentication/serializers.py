from .models import User
from vendor.models import Vendor, Performance
from rest_framework.serializers import ModelSerializer, ValidationError
import uuid


class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'is_superuser', 'email', 'is_vendor', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise ValidationError("Email already exists.")
        return value
    
    #overriding the create function for hashing the password
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        vendor_code = str(uuid.uuid4())[:8]
        instance.is_vendor = True
        if password is not None:
            instance.set_password(password)
        instance.save()

        # create vendor profile if the user is vendor
        # initially only giving user instance to vendor
        if instance.is_vendor == True:
            vendor = Vendor.objects.create(user=instance, vendor_code=vendor_code)
            Performance.objects.create(vendor = vendor)
        return instance
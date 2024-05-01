from rest_framework import serializers
from .models import *
from authentication.serializers import UserRegisterSerializer


class VendorSerializer(serializers.ModelSerializer):
    user = UserRegisterSerializer()

    class Meta:
        model = Vendor
        fields = '__all__'
        depth = 2
    
    def update(self, instance, validated_data):
        
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.contact_details = validated_data.get('contact_details', instance.contact_details)
        instance.on_time_delivery_rate = validated_data.get('on_time_delivery_rate', instance.on_time_delivery_rate)
        instance.quality_rating_avg = validated_data.get('quality_rating_avg', instance.quality_rating_avg)
        instance.average_response_time = validated_data.get('average_response_time', instance.average_response_time)
        instance.fulfillment_rate = validated_data.get('fulfillment_rate', instance.fulfillment_rate)
        instance.save()

        return instance


class PurchaseOrderSerializer(serializers.ModelSerializer):
    vendor = VendorSerializer()
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

class PurchaseOrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

class PerfomanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = '__all__'

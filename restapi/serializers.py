from restapi.models import Product1,Product4,Product2,Product3
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product1
        fields = "__all__"
        
# class Product2Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product2
#         fields = "__all__"
        
# class Product3Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product3
#         fields = "__all__"
        
# class Product4Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product4
#         fields = "__all__"
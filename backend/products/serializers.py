from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            "title",
            "content",
            "price",
            "sale_price",
            "my_discount",
        ]
    #! To create a function to call get_discount function and save that returned data inside variable named "my_discount", use get_variable_name. So we create a function in this serializer named get_my_discount
    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
        

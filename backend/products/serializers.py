from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
            view_name='product-detail',
            lookup_field='pk'
    )
    class Meta:
        model = Product
        fields = [
            'url',
            'edit_url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]
        
    def get_edit_url(self, obj):
        request = self.context.get('request') # self.request
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request) 
    #! To create a function to call get_discount function and save that returned data inside variable named "my_discount", use get_variable_name. So we create a function in this serializer named get_my_discount
    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
        

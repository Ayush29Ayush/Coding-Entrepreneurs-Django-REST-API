from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

# @api_view(["GET"])
# def api_home(request, *args, **kwargs):
#     """
#     DRF API View
#     """
#     model_data = Product.objects.all().order_by("?").first() # This will give a queryset
#     print("model_data => ",model_data)
#     data = {}
#     if model_data:
#         data = model_to_dict(model_data, fields=["id", "title", "price", "sale_price"]) # This will convert the queryset to a dictionary 
#         print("Data =>",data)
#     return Response(data) # This will return clean JSON type response

# @api_view(["GET"])
# def api_home(request, *args, **kwargs):
#     """
#     DRF API View
#     """
#     instance = Product.objects.all().order_by("?").first()
#     data = {}
#     if instance:
#         # data = model_to_dict(instance, fields=['id', 'title', 'price', 'sale_price'])
#         data = ProductSerializer(instance).data
#     return Response(data)

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        # print(instance)
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    model_data = Product.objects.all().order_by("?").first() # This will give a queryset
    print("model_data => ",model_data)
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=["id", "title", "price"]) # This will convert the queryset to a dictionary 
        print("Data =>",data)
    return Response(data) # This will return clean JSON type response

from rest_framework import generics


from .models import Product
from .serializers import ProductSerializer

#! RetrieveAPIView => Used for read-only endpoints to represent a single model instance. Provides a get method handler.
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk' ??


product_detail_view = ProductDetailAPIView.as_view()

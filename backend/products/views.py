from rest_framework import generics


from .models import Product
from .serializers import ProductSerializer

#! CreateAPIView => Used for create-only endpoints. Provides a post method handler.
#! ListCreateAPIView => Used for read-write endpoints to represent a collection of model instances. Provides get and post method handlers.
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)
        
product_list_create_view = ProductListCreateAPIView.as_view()

#! RetrieveAPIView => Used for read-only endpoints to represent a single model instance. Provides a get method handler.
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk' ??


product_detail_view = ProductDetailAPIView.as_view()


#! ListAPIView => Used for read-only endpoints to represent a collection of model instances. Provides a get method handler.
class ProductListAPIView(generics.ListAPIView):
    '''
    Not gonna use this method
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_list_view = ProductListAPIView.as_view()
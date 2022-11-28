from rest_framework import viewsets, mixins

from .models import Product
from .serializers import ProductSerializer


class ProductViewset(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'pk' # default

    def list(self, request, *args, **kwargs):
        print("Listando ")
        return super().list(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        print(args, kwargs)
        print("Listando por ID")
        return super().retrieve(request, *args, **kwargs)


class ProductGenericViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
    ):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'pk' # default

    def list(self, request, *args, **kwargs):
        print("Listando ")
        return super().list(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        print(args, kwargs)
        print("Listando por ID")
        return super().retrieve(request, *args, **kwargs)


#product_list = ProductGenericViewSet.as_view({'get': 'list'})
#product_detail = ProductGenericViewSet.as_view({'get': 'retrive'})

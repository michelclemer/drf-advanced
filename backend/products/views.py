from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import  get_object_or_404

from api.mixins import StaffEditorPermissionMixin, UserQuerySetMixin
from .models import Product
from .serializers import ProductSerializer



class ProductListCreateAPIView(
    UserQuerySetMixin,
    generics.ListCreateAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    allow_staff_view = False

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None:
            content = title

        serializer.save(content=content)
        #return super().perform_create(serializer)

    """ def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        
        request = self.request
        if not request.user.is_authenticated:
            return Product.objects.none()
        print(request.user)
        return qs.filter(user=request.user) """

        
product_list_create_view = ProductListCreateAPIView.as_view()



class ProductDetailAPIView(
    StaffEditorPermissionMixin,
    generics.RetrieveUpdateAPIView):
    '''
    
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def retrieve(self, request, *args, **kwargs):
        print(request.data)
        return super().retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        print(self.get_queryset())
        return self.update(request, *args, **kwargs)

product_detail_view = ProductDetailAPIView.as_view()


class ProductUpdateAPIView(
    StaffEditorPermissionMixin,
    generics.UpdateAPIView):
    '''
    
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


product_update_view = ProductUpdateAPIView.as_view()



class ProductDeleteAPIView(
    StaffEditorPermissionMixin,
    generics.DestroyAPIView):
    '''
    
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        
        super().perform_destroy(instance)


product_delete_view = ProductDeleteAPIView.as_view()




"""
class ProductListAPIView(generics.ListAPIView):
    '''
    
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def retrieve(self, request, *args, **kwargs):
        print(request.data)
        return super().retrieve(request, *args, **kwargs)


product_list_view = ProductListAPIView.as_view()
"""


class ProductMixinView(
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj
    
    def get_queryset(self):
        obj = super().get_queryset()
        print([i.title for i in obj])
        return obj

    def get(self, request, *args, **kwargs):
        pk  =  kwargs.get('pk')
        if pk:
            return self.retrieve(request, *args, **kwargs)

        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None:
            content = "This is a single view doing cool stuff"

        serializer.save(content=content)
        #return super().perform_create(serializer)

    def perform_update(self, serializer):

        return super().perform_update(serializer)
product_mixin_view = ProductMixinView.as_view()


@api_view(["GET", "POST",])
def produt_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    print(method)
    if method == 'GET':
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)

    elif method == 'POST':
        serializer = ProductSerializer(data=request.data) 
        if serializer.is_valid(raise_exception=True): # Informa o erro do model 
        
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content')
            if content is None:
                content = title

            serializer.save(content=content)
            return Response(serializer.data)
        
        return Response({"message": "Invalid data"})
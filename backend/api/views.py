import json
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from products.models import Product

from products.serializers import ProductSerializer

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    serializer = ProductSerializer(data=request.data) 
    if serializer.is_valid(raise_exception=True): # Informa o erro do model 
       
        print(serializer.data)
        return Response(serializer.data)
    
    return Response({"message": "Invalid data"})

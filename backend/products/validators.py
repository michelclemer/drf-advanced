from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Product


def validate_title(value):
       qs = Product.objects.filter(title__exact=value)
       if qs.exists():
            raise serializers.ValidationError(f"{value} os already a product name.")
       return value


unique_product_title = UniqueValidator(queryset=Product.objects.all())
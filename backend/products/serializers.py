from asyncore import write
import email
from rest_framework import serializers
from rest_framework.reverse import reverse
from api.serializers import UserSerializers

from .models import Product
from . import validators
class ProductSerializer(serializers.ModelSerializer):
    owner = UserSerializers(source='user', read_only=True)
    my_user_data = serializers.SerializerMethodField(read_only=True)
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk'
    )
    title = serializers.CharField(validators=[validators.unique_product_title])
    #name = serializers.CharField(source='user.email', read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'owner',
            'url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
            'edit_url',
            'my_user_data'
        ]
    
    def get_my_user_data(self, obj):
        return {
            "username": obj.user.username
        }

    def get_edit_url(self, objt):
        # return f"/api/products/{objt.pk}"
        request = self.context.get('request')
        if request is None:
            return None
        
        return reverse("product-edit", kwargs={'pk': objt.pk}, request=request)

    def get_my_discount(self, objt):
        if not hasattr(objt, 'id'):
            return None
        
        if not isinstance(objt, Product):
            return None
        return objt.get_discount()


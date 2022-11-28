
from rest_framework import serializers

from products.models import Product


class ProductInlineSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
        read_only=True
    )
    class Meta:
        model = Product
        fields = ("__all__")



class UserSerializers(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    prods = serializers.SerializerMethodField(read_only=True)
    password = serializers.CharField(read_only=True)
    
    def get_prods(self, obj):
        prod = obj.product_set.all()
        p = ProductInlineSerializer(prod, many=True, context=self.context)
        return p.data

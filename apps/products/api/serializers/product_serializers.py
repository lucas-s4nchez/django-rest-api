from rest_framework import serializers
from apps.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('state', 'created_date', 'updated_date', 'deleted_date')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'measure_unit': instance.measure_unit.description if instance.measure_unit is not None else '',
            'category': instance.category.description if instance.category is not None else '',
            # 'image': instance.image if instance.image != '' else ''
        }

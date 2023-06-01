from rest_framework import serializers
from apps.products.models import Category, MeasureUnit


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('state', 'created_date', 'updated_date', 'deleted_date')


class MeasureUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasureUnit
        exclude = ('state', 'created_date', 'updated_date', 'deleted_date')

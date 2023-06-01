from apps.base.api import GeneralListAPIView
from apps.products.api.serializers.general_serializers import CategorySerializer, MeasureUnitSerializer


class MeasureUnitListAPIView(GeneralListAPIView):
    serializer_class = MeasureUnitSerializer


class CategoryListAPIView(GeneralListAPIView):
    serializer_class = CategorySerializer

from rest_framework import viewsets

from apps.base.api import GeneralListAPIView
from apps.products.api.serializers.general_serializers import CategorySerializer, MeasureUnitSerializer


class MeasureUnitListAPIView(GeneralListAPIView):
    serializer_class = MeasureUnitSerializer


class CategoryListAPIView(GeneralListAPIView):
    serializer_class = CategorySerializer


class MeasureUnitViewset(viewsets.ModelViewSet):
    serializer_class = MeasureUnitSerializer
    queryset = MeasureUnitSerializer.Meta.model.objects.filter(state=True)

    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.filter(state=True)


class CategoryViewset(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = CategorySerializer.Meta.model.objects.filter(state=True)

    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.filter(state=True)

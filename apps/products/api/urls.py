from django.urls import path
from apps.products.api.views.general_views import MeasureUnitListAPIView, CategoryListAPIView

urlpatterns = [
    # path('measure_unit/', MeasureUnitListAPIView.as_view(), name='measure_unit'),
    # path('category/', CategoryListAPIView.as_view(), name='category'),
]

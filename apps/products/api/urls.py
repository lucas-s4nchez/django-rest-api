from django.urls import path
from apps.products.api.views.general_views import MeasureUnitListAPIView, CategoryListAPIView
from apps.products.api.views.products_views import ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('measure_unit/', MeasureUnitListAPIView.as_view(), name='measure_unit'),
    path('category/', CategoryListAPIView.as_view(), name='category'),
    path('', ProductListCreateAPIView.as_view(), name='products'),
    path('<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(),
         name='products_retrieve_update_destroy'),
]

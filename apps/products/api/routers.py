from rest_framework.routers import DefaultRouter

from apps.products.api.views.products_views import ProductViewSet
from apps.products.api.views.general_views import CategoryViewset, MeasureUnitViewset

router = DefaultRouter()

router.register(r'products', ProductViewSet, basename='products')
router.register(r'measure-unit', MeasureUnitViewset, basename='measure_unit')
router.register(r'category', CategoryViewset, basename='category')

urlpatterns = router.urls

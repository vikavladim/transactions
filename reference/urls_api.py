from rest_framework.routers import DefaultRouter
from .views_api import StatusViewSet, OperationTypeViewSet, CategoryViewSet, SubCategoryViewSet

router = DefaultRouter()
router.register(r'status', StatusViewSet, basename='status')
router.register(r'operation-types', OperationTypeViewSet, basename='operationtype')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'subcategories', SubCategoryViewSet, basename='subcategory')

urlpatterns = router.urls
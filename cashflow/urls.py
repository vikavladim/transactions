from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from reference import views_api as reference_views
from transactions import views_api as transaction_views

router = routers.DefaultRouter()
router.register(r'api/statuses', reference_views.StatusViewSet)
router.register(r'api/operation-types', reference_views.OperationTypeViewSet)
router.register(r'api/categories', reference_views.CategoryViewSet)
router.register(r'api/subcategories', reference_views.SubCategoryViewSet)
router.register(r'api/transactions', transaction_views.TransactionViewSet)

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('', include('transactions.urls', namespace='transactions')),
    path('reference/', include('reference.urls', namespace='reference')),
    path('', include(router.urls)),  # Include API URLs
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
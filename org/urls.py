from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ProviderViewSet, ProductViewSet, ContactsRetrieveUpdateAPIView

router = DefaultRouter()
router.register(r'provider', ProviderViewSet, basename='provider')
router.register(r'product', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    path('contacts/<pk>/', ContactsRetrieveUpdateAPIView.as_view())
]
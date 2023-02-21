
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.viewsets import ModelViewSet

from org.models import Organization, Product, Contact
from org.permissions import EmployeesPermissions
from org.serializers import ProviderSerializer, ProviderUpdateSerializer, ProductSerializer, ContactsSerializer


class ProviderViewSet(ModelViewSet):
    queryset = Organization.objects.all()
    default_serializer = ProviderSerializer
    serializer_classes = {
        'update': ProviderUpdateSerializer,
        'partial_update': ProviderUpdateSerializer,
    }
    ordering = ['id']
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter
    ]
    filterset_fields = ['contacts__country']
    permission_classes = [EmployeesPermissions]

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)

    def perform_destroy(self, instance):
        contacts = instance.contacts
        super().perform_destroy(instance)
        contacts.delete()


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [EmployeesPermissions]
    ordering = ['id']
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter
    ]


class ContactsRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = [EmployeesPermissions]
    ordering = ['id']
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter
    ]
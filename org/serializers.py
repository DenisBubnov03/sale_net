from rest_framework import serializers

from org.models import Product, Organization, Contact


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ProviderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True, required=False)
    contacts = ContactsSerializer(required=True)

    class Meta:
        model = Organization
        fields = '__all__'
        read_only_fields = ('id', 'debt', 'create_date')

    def create(self, validated_data):
        contacts = validated_data.pop("contacts")
        contact = Contact.objects.create(**contacts)
        provider = Organization.objects.create(contacts=contact, **validated_data)
        return provider


class ProviderUpdateSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)
    contacts = ContactsSerializer(read_only=True)

    class Meta:
        model = Organization
        fields = '__all__'
        read_only_fields = ('id', 'debt', 'create_date')

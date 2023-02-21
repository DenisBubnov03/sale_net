from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from org.models import Product, Contact, Organization


@admin.action(description='Очистить задолженность перед поставщиком')
def debt_clear(modeladmin, request, queryset):
    queryset.update(debt=0)


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = (
        'hierarchy',
        'title',
        'debt',
        'provider_link',
        'city'
    )
    list_display_links = (
        'title',
    )
    list_filter = (
        'hierarchy',
        'contacts__city'
    )
    actions = [debt_clear]

    @admin.display(description='Поставщик')
    def provider_link(self, obj):
        if obj.provider:
            link = reverse('admin:org_organization_change', args=(obj.provider.id,))
            return mark_safe(u'<a href="{0}">{1}</a>'.format(link, obj.provider))

    @admin.display(description='Город')
    def city(self, obj):
        return obj.contacts.city


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'model',
        'release_date'
    )
    list_filter = ('title',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'country',
        'city',
        'street',
        'house_number',
    )
    list_filter = ('email',)

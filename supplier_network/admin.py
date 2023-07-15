from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Factory, RetailsNetwork, IndividualEntrepreneur, Contact, Product


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    """
    Класс с кастомной настройкой админ-панели завод (Factory)
    """
    list_display = ('title', 'created')
    list_filter = ('contact__city',)


@admin.register(RetailsNetwork)
class RetailsNetworkAdmin(admin.ModelAdmin):
    """
    Класс с кастомной настройкой админ-панели розничная сеть (RetailsNetwork)
    """
    list_display = ('title', 'indebtedness', 'created', 'supplier_link')
    list_filter = ('contact__city',)
    actions = ['clear_indebtedness']

    def supplier_link(self, obj):
        if obj.factory:
            factory_link = reverse('admin:supplier_network_factory_change', args=[obj.factory.id])
            return format_html('<a href="{}">{}</a>', factory_link, obj.factory.title)
        elif obj.individual_entrepreneur:
            individual_link = reverse('admin:supplier_network_individualentrepreneur_change', args=[obj.individual_entrepreneur.id])
            return format_html('<a href="{}">{}</a>', individual_link, obj.individual_entrepreneur.title)
        else:
            return '-'

    supplier_link.short_description = 'Ссылка на поставщика'

    def clear_indebtedness(self, request, queryset):
        for obj in queryset:
            obj.indebtedness = 0
            obj.save()

    clear_indebtedness.short_description = 'Очистить задолженность'


@admin.register(IndividualEntrepreneur)
class IndividualEntrepreneurAdmin(admin.ModelAdmin):
    """
    Класс с кастомной настройкой админ-панели индивидуальный предприниматель (IndividualEntrepreneur)
    """
    list_display = ('title', 'indebtedness', 'created', 'supplier_link')
    list_filter = ('contact__city',)
    actions = ['clear_indebtedness']

    def supplier_link(self, obj):
        if obj.factory:
            factory_link = reverse('admin:supplier_network_factory_change', args=[obj.factory.id])
            return format_html('<a href="{}">{}</a>', factory_link, obj.factory.title)
        elif obj.retails_network:
            retails_link = reverse('admin:supplier_network_retailsnetwork_change', args=[obj.retails_network.id])
            return format_html('<a href="{}">{}</a>', retails_link, obj.retails_network.title)
        else:
            return '-'

    supplier_link.short_description = 'Ссылка на поставщика'

    def clear_indebtedness(self, request, queryset):
        for obj in queryset:
            obj.indebtedness = 0
            obj.save()

    clear_indebtedness.short_description = 'Очистить задолженность'


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Класс с кастомной настройкой админ-панели контакты (Contact)
    """
    list_display = ('email', 'country', 'city', 'street', 'house_number', 'factory', 'retails', 'individuals')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Класс с кастомной настройкой админ-панели продукты (Product)
    """
    list_display = ('title', 'model', 'release_date')


admin.site.site_header = 'Администрирование проекта Electronic Store'
admin.site.site_title = 'Администрирование проекта Electronic Store'

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from supplier_network import serializers, models
from supplier_network.permissions import IsActive


class FactoryViews(viewsets.ModelViewSet):
    """
    Представление для модели Factory (Завод)
    """
    queryset = models.Factory.objects.all()
    serializer_class = serializers.FactorySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ["contact__country"]
    permission_classes = [IsActive]


class RetailsNetworkViews(FactoryViews):
    """
    Представление для модели RetailsNetwork (Розничная сеть), наследуется от FactoryViews
    """
    queryset = models.RetailsNetwork.objects.all()
    serializer_class = serializers.RetailSerializer


class IndividualEntrepreneurViews(FactoryViews):
    """
    Представление для модели IndividualEntrepreneur (Индивидуальный предприниматель), наследуется от FactoryViews
    """
    queryset = models.IndividualEntrepreneur.objects.all()
    serializer_class = serializers.IndividualSerializer

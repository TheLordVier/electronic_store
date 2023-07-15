from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Contact, Product, Factory, RetailsNetwork, IndividualEntrepreneur


class ContactSerializer(serializers.ModelSerializer):
    """
    Сериализатор ContactSerializer служит для работы с моделью Contact (Контакты)
    """
    class Meta:
        model = Contact
        exclude = ("factory", "retails", "individuals")

    def validate(self, attrs):
        link_factory = attrs.get("factory")
        link_retails = attrs.get("retails")
        link_individuals = attrs.get("individuals")

        links_supplier = (link_factory, link_retails, link_individuals)

        if sum(map(lambda x: x is not None, links_supplier)) != 1:
            assert ValidationError({"error": "Адрес может быть только у одного поставщика"})

        return attrs


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор ProductSerializer служит для работы с моделью Product (Продукты)
    """
    class Meta:
        model = Product
        exclude = ("factory", "retails", "individuals")


class FactorySerializer(serializers.ModelSerializer):
    """
    Сериализатор FactorySerializer служит для работы с моделью Factory (Завод)
    """
    contact = ContactSerializer()
    products = ProductSerializer(many=True)

    class Meta:
        model = Factory
        fields = "__all__"
        read_only_fields = ("id", "created")

    def update(self, instance, validated_data):
        """
        Метод обновления данных модели Factory и связанных моделей
        """
        contact_data = validated_data.pop('contact', None)
        products_data = validated_data.pop('products', None)

        instance.title = validated_data.get('title', instance.title)
        instance.indebtedness = validated_data.get('indebtedness', instance.indebtedness)

        if contact_data:
            contact_serializer = ContactSerializer(instance.contact, data=contact_data, partial=True)
            if contact_serializer.is_valid():
                contact_serializer.save()
            else:
                raise serializers.ValidationError(contact_serializer.errors)

        if products_data:
            instance.products.clear()

            for product_data in products_data:
                product_serializer = ProductSerializer(data=product_data)
                if product_serializer.is_valid():
                    product = product_serializer.save()
                    instance.products.add(product)
                else:
                    raise serializers.ValidationError(product_serializer.errors)

        instance.save()
        return instance

    def create(self, validated_data):
        """
        Метод создания новой записи модели Factory и связанных моделей
        """
        contact = validated_data.pop("contact")
        products = validated_data.pop("products")

        with transaction.atomic():
            instance = self.Meta.model.objects.create(**validated_data)

            data = {}
            if self.Meta.model is Factory:
                data["factory"] = instance
            elif self.Meta.model is RetailsNetwork:
                data["retails"] = instance
            elif self.Meta.model is IndividualEntrepreneur:
                data["individuals"] = instance
            else:
                raise ValidationError({"error": "Ошибка сохранения поставщика"})

            Contact.objects.create(**contact, **data)

            for product in products:
                item = Product.objects.create(**product)
                instance.products.add(item)

        return instance


class RetailSerializer(FactorySerializer):
    """
    Сериализатор RetailSerializer служит для работы с моделью RetailsNetwork (Розничная сеть)
    """
    products = ProductSerializer(many=True)

    class Meta:
        model = RetailsNetwork
        fields = "__all__"
        read_only_fields = ("id", "created",)

    def update(self, instance, validated_data):
        """
        Метод обновления данных модели RetailsNetwork и связанных моделей
        Метод не даёт посредством API (PUT и PATCH) менять задолженность
        """
        validated_data.pop("indebtedness", None)  # Удаление поля "indebtedness" (задолженность) из validated_data

        return super().update(instance, validated_data)

    def create(self, validated_data):
        """
        Метод создания новой записи модели RetailsNetwork и связанных моделей
        """
        contact = validated_data.pop("contact")
        products_data = validated_data.pop("products")

        with transaction.atomic():
            instance = self.Meta.model.objects.create(**validated_data)

            data = {}
            if self.Meta.model is Factory:
                data["factory"] = instance
            elif self.Meta.model is RetailsNetwork:
                data["retails"] = instance
            elif self.Meta.model is IndividualEntrepreneur:
                data["individuals"] = instance
            else:
                raise ValidationError({"error": "Ошибка сохранения поставщика"})

            Contact.objects.create(**contact, **data)

            products = []
            for product_data in products_data:
                product_serializer = ProductSerializer(data=product_data)
                if product_serializer.is_valid():
                    product = product_serializer.save()
                    products.append(product)
                else:
                    raise serializers.ValidationError(product_serializer.errors)

            instance.products.set(products)

        return instance


class IndividualSerializer(RetailSerializer):
    """
    Сериализатор IndividualSerializer служит для работы с моделью IndividualEntrepreneur
    (Индивидуальный предприниматель)
    Пре
    """
    class Meta:
        model = IndividualEntrepreneur
        fields = "__all__"
        read_only_fields = ("id", "created",)

    def update(self, instance, validated_data):
        """
        Метод обновления данных модели IndividualEntrepreneur и связанных моделей
        Метод не даёт посредством API (PUT и PATCH) менять задолженность
        """
        validated_data.pop("indebtedness", None)  # Удаление поля "indebtedness" (задолженность) из validated_data

        return super().update(instance, validated_data)

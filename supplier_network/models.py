from django.core.validators import MinValueValidator
from django.db import models


class Supplier(models.Model):
    """
    Модель поставщика
    """
    class Meta:
        abstract = True

    title = models.CharField(verbose_name="Название", max_length=100)
    indebtedness = models.DecimalField(verbose_name="Задолженность",
                                       decimal_places=2,
                                       max_digits=25,
                                       default=0.00,
                                       validators=([MinValueValidator(0)]))
    created = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)

    def __str__(self):
        return self.title


class Factory(Supplier):
    """
    Модель завода
    """
    indebtedness = models.Empty()

    class Meta:
        verbose_name = "Завод"
        verbose_name_plural = "Заводы"


class RetailsNetwork(Supplier):
    """
    Модель розничной сети
    """
    factory = models.ForeignKey("Factory",
                                on_delete=models.PROTECT,
                                related_name="retailers",
                                blank=True,
                                null=True)

    individual_entrepreneur = models.ForeignKey("IndividualEntrepreneur",
                                                on_delete=models.PROTECT,
                                                related_name="retailers",
                                                blank=True,
                                                null=True)

    class Meta:
        verbose_name = "Розничная сеть"
        verbose_name_plural = "Розничные сети"


class IndividualEntrepreneur(Supplier):
    """
    Модель индивидуального предпринимателя
    """
    factory = models.ForeignKey("Factory",
                                on_delete=models.PROTECT,
                                related_name="individual_entrepreneurs",
                                blank=True,
                                null=True)

    retails_network = models.ForeignKey("RetailsNetwork",
                                        on_delete=models.PROTECT,
                                        related_name="individual_entrepreneurs",
                                        blank=True,
                                        null=True)

    class Meta:
        verbose_name = "Индивидуальный предприниматель"
        verbose_name_plural = "Индивидуальные предприниматели"


class Contact(models.Model):
    """
    Модель контакта
    """
    email = models.EmailField(verbose_name="Email")
    country = models.CharField(verbose_name="Страна", max_length=80)
    city = models.CharField(verbose_name="Город", max_length=80)
    street = models.CharField(verbose_name="Улица", max_length=100)
    house_number = models.PositiveSmallIntegerField(verbose_name="Номер дома")

    factory = models.OneToOneField("Factory", on_delete=models.CASCADE, null=True, blank=True)
    retails = models.OneToOneField("RetailsNetwork", on_delete=models.CASCADE, null=True, blank=True)
    individuals = models.OneToOneField("IndividualEntrepreneur", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return self.email


class Product(models.Model):
    """
    Модель продукта
    """
    title = models.CharField(verbose_name="Название продукта", max_length=100)
    model = models.CharField(verbose_name="Модель", max_length=150)
    release_date = models.DateTimeField(verbose_name='Дата выхода на рынок', auto_now_add=True)

    factory = models.ManyToManyField("Factory", blank=True, related_name="products")
    retails = models.ManyToManyField("RetailsNetwork", blank=True, related_name="products")
    individuals = models.ManyToManyField("IndividualEntrepreneur", blank=True, related_name="products")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.title

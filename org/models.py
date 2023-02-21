from django.core.exceptions import ValidationError
from django.db import models


class Product(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    title = models.CharField(max_length=60, verbose_name='Название товара')
    model = models.CharField(max_length=100, verbose_name='Модель товара')
    release_date = models.DateField(verbose_name='Дата выхода на рынок')

    def __str__(self):
        return self.title


class Contact(models.Model):
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    email = models.EmailField(max_length=254, unique=True)
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=200, verbose_name='Город')
    street = models.CharField(max_length=200, verbose_name='Улица')
    house_number = models.CharField(max_length=200, verbose_name='Номер дома')

    def __str__(self):
        return self.email


class Organization(models.Model):
    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

    hierarchy_level = (
        (0, 'завод'),
        (1, 'розничная сеть'),
        (2, 'индивидуальный предприниматель'),
    )
    title = models.CharField(max_length=100, unique=True, verbose_name='Название компании')
    hierarchy = models.SmallIntegerField(choices=hierarchy_level, verbose_name='уровень иерархии')
    contacts = models.OneToOneField(
        'org.Contact',
        on_delete=models.CASCADE,
        related_name='org',
        verbose_name='Контактные данные'
    )
    products = models.ManyToManyField(
        'org.Product',
        related_name='org',
        blank=True,
        verbose_name='Товар'
    )
    provider = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        related_name='trader',
        verbose_name='Поставщик',
        null=True,
        blank=True
    )
    debt = models.DecimalField(
        max_digits=25,
        decimal_places=2,
        verbose_name='Задолженность',
        default=0
    )
    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания'
    )

    def __str__(self):
        return self.title

    def clean(self):
        if self.provider:
            if self.provider.id == self.id:
                raise ValidationError('Организация не может быть своим поставщиком')

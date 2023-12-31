# Generated by Django 4.0.1 on 2023-07-13 18:46

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Завод',
                'verbose_name_plural': 'Заводы',
            },
        ),
        migrations.CreateModel(
            name='IndividualEntrepreneur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('indebtedness', models.DecimalField(decimal_places=2, default=0.0, max_digits=25, validators=[django.core.validators.MinValueValidator(0)])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('factory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='individual_entrepreneurs', to='supplier_network.factory')),
            ],
            options={
                'verbose_name': 'Индивидуальный предприниматель',
                'verbose_name_plural': 'Индивидуальные предприниматели',
            },
        ),
        migrations.CreateModel(
            name='RetailsNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('indebtedness', models.DecimalField(decimal_places=2, default=0.0, max_digits=25, validators=[django.core.validators.MinValueValidator(0)])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('factory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='retailers', to='supplier_network.factory')),
                ('individual_entrepreneur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='retailers', to='supplier_network.individualentrepreneur')),
            ],
            options={
                'verbose_name': 'Розничная сеть',
                'verbose_name_plural': 'Розничные сети',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=150)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('factory', models.ManyToManyField(blank=True, related_name='products', to='supplier_network.Factory')),
                ('individuals', models.ManyToManyField(blank=True, related_name='products', to='supplier_network.IndividualEntrepreneur')),
                ('retails', models.ManyToManyField(blank=True, related_name='products', to='supplier_network.RetailsNetwork')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.AddField(
            model_name='individualentrepreneur',
            name='retails_network',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='individual_entrepreneurs', to='supplier_network.retailsnetwork'),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(max_length=80)),
                ('city', models.CharField(max_length=80)),
                ('street', models.CharField(max_length=100)),
                ('house_number', models.PositiveSmallIntegerField()),
                ('factory', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='supplier_network.factory')),
                ('individuals', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='supplier_network.individualentrepreneur')),
                ('retails', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='supplier_network.retailsnetwork')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
    ]

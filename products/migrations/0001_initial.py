# Generated by Django 3.2.13 on 2023-01-08 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Category name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Category description')),
            ],
            options={
                'verbose_name': 'Product Category',
                'verbose_name_plural': "Product Category's",
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name product')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Product price')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Quantity')),
                ('image', models.ImageField(upload_to='products_images', verbose_name='Image')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productcategory', verbose_name='Product Category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': "Product's",
            },
        ),
    ]

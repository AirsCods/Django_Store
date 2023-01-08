from django.db import models


# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(verbose_name='Category name', max_length=128, unique=True)
    description = models.TextField(verbose_name='Category description', null=True, blank=True)

    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Category's"

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(verbose_name='Name product', max_length=256)
    description = models.TextField(verbose_name='Description', null=True, blank=True)
    price = models.DecimalField(verbose_name='Product price', max_digits=7, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='Quantity', default=0)
    image = models.ImageField(verbose_name='Image', upload_to='products_images')
    category = models.ForeignKey(verbose_name='Product Category', to=ProductCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Product's"

    def __str__(self):
        return f'Подукт: {self.name} | Категория: {self.category.name}'

from django.db import models

from users.models import User


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='Category name', max_length=128, unique=True)
    description = models.TextField(verbose_name='Category description', null=True, blank=True)

    class Meta:
        verbose_name = "Категория товаров"
        verbose_name_plural = "Категории товаров"

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
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return f'Подукт: {self.name} | Категория: {self.category.name}'


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)


class Basket(models.Model):
    user = models.ForeignKey(verbose_name='User', to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(verbose_name='Product name', to=Products, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(verbose_name='Quantity', default=0)
    created_timestamp = models.DateTimeField(verbose_name='Created time', auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def sum(self):
        return self.product.price * self.quantity

    class Meta:
        verbose_name = "Basket"
        verbose_name_plural = "Basket's"

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт: {self.product.name}'

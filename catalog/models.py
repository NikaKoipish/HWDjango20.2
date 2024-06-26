from django.db import models

from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.name} - {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='products/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='id')
    price = models.IntegerField(verbose_name='Цена за единицу')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')
    is_published = models.BooleanField(default=False, verbose_name='Признак публикации')

    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        return f'{self.category} {self.name} - {self.price}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('price',)
        permissions = [
            (
                "set_published_status",
                "Can publish product"
            ),
            (
                "edit_product_description",
                "Can edit product description"
            ),
            (
                "edit_product_category",
                "Can edit product category"
            )
        ]


class Contacts(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    phone = models.CharField(max_length=100, verbose_name='Телефон')
    message = models.CharField(max_length=100, verbose_name='Сообщение')
    email = models.EmailField(verbose_name='Электронная почта', **NULLABLE)

    def __str__(self):
        return f'{self.first_name} {self.email}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Version(models.Model):
    product = models.ForeignKey(Product, related_name='versions', on_delete=models.CASCADE, verbose_name='продукт')
    number = models.IntegerField(verbose_name='номер версии')
    name = models.CharField(max_length=50, verbose_name='название версии')
    is_active = models.BooleanField(default=False, verbose_name='признак активности версии')

    def __str__(self):
        return f'{self.name} ({self.number})'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'

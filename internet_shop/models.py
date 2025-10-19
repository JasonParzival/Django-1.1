from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.TextField("Название")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    description = models.TextField("Описание")
    quantity = models.IntegerField("Количество на складе")
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True, verbose_name="Категория")
    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        
    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.TextField("Название")
    description = models.TextField("Описание")
    
    class Meta:
        verbose_name = "Категория товара"
        verbose_name_plural = "Категории товаров"
        
    def __str__(self) -> str:
        return self.name
        
class Customer(models.Model):
    name = models.TextField("ФИО")
    address = models.TextField("Адрес")
    phone_number = models.TextField("Номер телефона")
    email = models.TextField("Электронная почта")
    
    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        
    def __str__(self) -> str:
        return self.name

class Order(models.Model):
    date = models.DateField("Дата заказа")
    status = models.TextField("Статус")
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE, null=True, verbose_name="Клиент")
    
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        
    def __str__(self) -> str:
        return str(self.date)

class OrderDetail(models.Model):
    order = models.ForeignKey("Order", on_delete=models.CASCADE, null=True, verbose_name="Заказ")
    product = models.ForeignKey("Product", on_delete=models.CASCADE, null=True, verbose_name="Продукт")
    quantity = models.IntegerField("Количество")
    
    class Meta:
        verbose_name = "Детали заказа"
        verbose_name_plural = "Детали заказов"
    
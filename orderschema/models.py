
import phonenumbers
from django.db import models
from django.contrib.auth.models import User




class Servicemod(models.Model):
    name = models.CharField("Название услуги", max_length=255)
    price = models.IntegerField("Цена")
    count = models.IntegerField("Количество")

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.name


class Usermod(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_phone = models.CharField("Телефон +7", unique=True, max_length=12, default='Мобильник')
    name_org = models.CharField("Название организации", max_length=255)
    address_org = models.CharField("Адрес организации", max_length=255)

    class Meta:
        verbose_name = "Пользователи услуг"
        verbose_name_plural = "Пользователи услуг"

    def __str__(self):
        return self.name_org



class Ordermod(models.Model):
    servicemod = models.ForeignKey(Servicemod, on_delete=models.CASCADE, null=True)
    usermod = models.ForeignKey(Usermod, on_delete=models.CASCADE, null=True)
    date_order = models.DateField("Дата заказа", blank=True, null=True)
    executed_order = models.BooleanField("Выполнен: да/нет", default=True)

    class Meta:
        verbose_name = "Зкаказ"
        verbose_name_plural = "Заказы"
        ordering = ["id"]

    def __str__(self):
        return self.usermod.name_org

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models


def user_directory_path(instance, filename):
    return "user_{0}/avatar/{1}".format(instance.username, filename)


def service_directory_path(instance, filename):
    return "user_{0}/picture/{1}".format(instance.owner.username, filename)


class Account(AbstractUser):
    email = models.EmailField('Электронная почта', unique=True)
    username = models.CharField('Имя пользователя', max_length=20, unique=True)
    password = models.CharField('Пароль', max_length=128)
    about = models.TextField('О себе', blank=True)
    reg_date = models.DateTimeField('Дата регистрации', auto_now_add=True)
    block = models.BooleanField('Заблокирован', default=False)
    orders = models.PositiveIntegerField('Количество заказов', default=0)
    avatar = models.ImageField('Аватар пользователя',
                               upload_to=user_directory_path,
                               default='default.png')
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    is_active = models.BooleanField('Статус аккаунта', default=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'


class Service(models.Model):
    title = models.CharField('Название услуги', max_length=128)
    price = models.DecimalField('Цена услуги', max_digits=11, decimal_places=2,
                                validators=[MinValueValidator(0.0099)])
    description = models.TextField('Описание услуги')
    date_created = models.DateTimeField('Дата создания', auto_now_add=True)
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    orders = models.PositiveIntegerField('Количество заказов', default=0)
    picture = models.ImageField('Картинка', upload_to=service_directory_path,
                                default='default.png')
    is_active = models.BooleanField('Статус услуги', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Order(models.Model):
    buyer = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField('Дата сделки', auto_now_add=True)

    def __str__(self):
        return str(self.date_created)

    def update_counter(self):
        self.service.owner.orders += 1
        self.service.orders += 1
        self.service.owner.save()
        self.service.save()

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

from django.contrib.auth.models import AbstractUser
from django.db import models


def user_directory_path(instance, filename):
    return "user_{0}/{1}".format(instance.username, filename)


class Account(AbstractUser):
    email = models.EmailField('Электронная почта', unique=True)
    username = models.CharField('Имя пользователя', max_length=20,
                                unique=True)
    password = models.CharField('Пароль', max_length=64)
    about = models.TextField('О себе', blank=True)
    reg_date = models.DateTimeField('Дата регистрации',
                                    auto_now_add=True)
    block = models.BooleanField('Заблокирован', default=False)
    orders = models.PositiveIntegerField('Количество заказов',
                                         default=0)
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

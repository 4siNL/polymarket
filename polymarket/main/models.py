from django.db import models


def user_directory_path(instance, filename):
    return "user_{0}/{1}".format(instance.username, filename)


# Create your models here.
class Account(models.Model):
    email = models.EmailField('Электронная почта', unique=True)
    username = models.CharField('Имя пользователя', max_length=20,
                                unique=True)
    password = models.CharField('Хеш пароля', max_length=64)
    about = models.TextField('О себе', blank=True)
    reg_date = models.DateTimeField('Дата регистрации',
                                    auto_now_add=True)
    status = models.BooleanField('Статус аккаунта', default=True)
    orders = models.PositiveIntegerField('Количество заказов',
                                         default=0)
    avatar = models.ImageField('Аватар пользователя',
                               upload_to=user_directory_path,
                               default='default.png')

    def __str__(self):
        return self.username

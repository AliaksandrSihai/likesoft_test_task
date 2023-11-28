from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    """ Модель для пользователя """

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    name = models.CharField(max_length=255, verbose_name='имя', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='почта')
    date_of_registry = models.DateTimeField(auto_now_add=True, verbose_name='дата регистрации')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'






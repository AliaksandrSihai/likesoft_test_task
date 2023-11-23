from django.db import models

from users.models import NULLABLE


class Author(models.Model):
    """ Модель для автора """
    name = models.CharField(max_length=255, verbose_name='имя')
    surname = models.CharField(max_length=255, verbose_name='фамилия')
    date_of_birth = models.DateField(verbose_name='дата рождения', **NULLABLE)

    def __str__(self):
        return self.surname

    class Meta:
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'


class Book(models.Model):
    """ Модель для книги """
    title = models.CharField(max_length=255, verbose_name='название')
    author = models.ForeignKey(to=Author, on_delete=models.SET_NULL, **NULLABLE)
    publish_year = models.DateField(verbose_name='дата публикации', **NULLABLE)
    isbn_number = models.PositiveIntegerField(verbose_name='isbn номер')
    description = models.TextField(verbose_name='краткое описание', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'

# Generated by Django 4.2.7 on 2023-11-23 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='имя')),
                ('surname', models.CharField(max_length=255, verbose_name='фамилия')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='дата рождения')),
            ],
            options={
                'verbose_name': 'автор',
                'verbose_name_plural': 'авторы',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='название')),
                ('publish_year', models.DateField(blank=True, null=True, verbose_name='дата публикации')),
                ('isbn_number', models.PositiveIntegerField(verbose_name='isbn номер')),
                ('description', models.TextField(blank=True, null=True, verbose_name='краткое описание')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.author')),
            ],
            options={
                'verbose_name': 'книга',
                'verbose_name_plural': 'книги',
            },
        ),
    ]

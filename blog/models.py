from django.db import models

class Category(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=100)
    slug = models.SlugField('Slug', max_length=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


# Create your models here.

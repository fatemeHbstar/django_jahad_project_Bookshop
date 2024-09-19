from django.db import models
from django.utils.text import slugify
# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)

    class Gender(models.TextChoices):
        MALE = 'M'
        FEMALE = 'F'

    gender = models.CharField(max_length=100, choices=Gender.choices)
    image_url = models.URLField(max_length=200, default='')
    year_of_birth = models.PositiveSmallIntegerField(default=0)


class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField(default='')
    rating = models.PositiveIntegerField(default=1)
    is_available = models.BooleanField(default=True)
    genre = models.CharField(default='', max_length=100)
    type = models.CharField(default='', max_length=100)
    image_url = models.URLField(max_length=200)
    slug = models.SlugField(default='', null=False, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.title) + ' ' + str(self.price))
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}---{self.price}'


class Tool(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField(default='')
    image_url = models.URLField(max_length=200, default='')
    is_available = models.BooleanField(default=True)
    type = models.CharField(default='', max_length=100)
    slug = models.SlugField(default='', null=False, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.name) + ' ' + str(self.price))
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}---{self.price}'

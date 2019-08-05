from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

from django.utils.translation import ugettext_lazy as _

from .managers import MyUserManager


class Author(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    room = models.CharField(max_length=100)
    phone = models.CharField(max_length=14)
    first_name = models.CharField(max_length=14)
    last_name = models.CharField(max_length=14)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name) + " (" + str(self.email) + ") "


class Category(models.Model):
    name = models.CharField(max_length=120)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return str(self.name)


class Ad(models.Model):
    name = models.CharField(max_length=120)
    descr = models.CharField(max_length=500)
    date = models.DateField(default=timezone.now)
    price = models.IntegerField(default=0)
    category = models.ForeignKey('Category', null=True, 
        related_name='ads_in_cat', on_delete=models.CASCADE)
    author = models.ForeignKey(Author, null=True,
        related_name='ads_by_author', on_delete=models.CASCADE)
    favorite_for = models.ManyToManyField('Author', verbose_name="Favorite for users",
        related_name='favorite_ads', blank=True)

    def save(self, *args, **kwargs):
        if self.category is None: 
            self.category_id = 1
        if self.author is None: 
            self.author_id = 1
        super(Ad, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return str(self.name)


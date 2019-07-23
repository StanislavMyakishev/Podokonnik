from django.contrib import admin

from .models import Author, Category, Ad

admin.site.register(Author)
admin.site.register(Ad)
admin.site.register(Category)
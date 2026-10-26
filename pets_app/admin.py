from django.contrib import admin
from .models import Pet, Category

# Register your models here.
admin.site.register(Category)
admin.site.register(Pet)
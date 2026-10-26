from django.db import models
from django.views.generic import ListView

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"
        


# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    age = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='pets', null=True, blank=True)
    image = models.ImageField(upload_to='pets/', blank=True, null=True)



    def __str__(self):
        category = self.category.name if self.category else "yo'q"
        return f"{self.name} ({self.species}, age:{self.age}) | {category}"
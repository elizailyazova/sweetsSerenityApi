from django.db import models
from categories.models import Category

class Dessert(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='desserts', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='desserts/')
    description = models.TextField()
    formula = models.TextField()
    nutrition = models.TextField()
    calories = models.TextField()
    freshness_date = models.TextField()

    def __str__(self):
        return self.name
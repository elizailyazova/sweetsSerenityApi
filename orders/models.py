from django.db import models
from django.contrib.auth.models import User
from desserts.models import Dessert
from branch.models import Branch
from djangoProject1 import settings


class Order(models.Model):
    number = models.AutoField(primary_key=True)
    dessert = models.ForeignKey(Dessert, related_name='orders', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    branch = models.ForeignKey(Branch, related_name='branch', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.number

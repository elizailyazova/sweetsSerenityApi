from django.db import models

class Branch(models.Model):
    adress = models.TextField(max_length=100)
    image = models.ImageField(upload_to='branch/')

    def __str__(self):
        return self.adress

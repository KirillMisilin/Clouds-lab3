from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=100)
    href = models.CharField(max_length=200, default='None')
    img = models.CharField(max_length=200, default='None')

    def __str__(self):
        return f'{self.name} {self.href}'
from django.db import models


class Expense(models.Model):
    name = models.CharField(max_length=100)
    tag = models.CharField(max_length=50)
    color = models.CharField(max_length=7)  # hex color

    def __str__(self):
        return self.name

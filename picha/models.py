from django.db import models
import datetime as dt

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

    def save_cat(self):
        self.save()

    def delete_cat(self):
        self.delete()

    def update_cat(self):
        self.update()

class Location(models.Model):
    name = models.CharField(max_length = 20)

    
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

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
    
    def update_location(self):
        self.update_location

    @classmethod
    def get_location(cls):
        location = cls.objects.all()
        return location

class Image(models.Model):
    
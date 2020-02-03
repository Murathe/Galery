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
    title = models.CharField(max_length = 20)
    content = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
    category_image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.title

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.update()

    @classmethod
    def search_by_category(cls, search_term):
        picha = cls.objects.filter(category__name__icontains=search_term)
        return picha
    
    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def get_image_by_id(cls):
        img_id = cls.objects.get(pk=id)
        return img_id
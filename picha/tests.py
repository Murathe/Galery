from django.test import TestCase
from .models import Editor,Article,tags

# Create your tests here.
class ImageTestCase(TestCase):
    def setUp(self):
        pass

    # New image
    self.new_image = Image(title='title1',
        description='Test image')
        self.new_image.save()

    # Creating a new location
        self.new_location = Location(name='nai')
        self.new_location.save()
    
    # Creating a new category
        self.new_category = Category(name='code')
        self.new_category.save()

    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()

class LocationTestClass(TestCase):

    """
    A test that checks for the behaviour of the image class
    """

    def setUp(self):
        pass

class CategoryTestClass(TestCase):
    """
    A test  that checks the functionality of the image class
    """

    def setUp(self):
        pass
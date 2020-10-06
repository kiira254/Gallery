from django.test import TestCase
from django.test import TestCase
from .models import Image,Categories
import datetime as dt

# Create your tests here.
class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new tag and saving it

        self.new_categories = categories(name = 'testing')
        self.new_category.save()

        self.new_image= Image(title = 'Test Article',post = 'This is a random test Post')
        self.new_image.save()

        self.new_image.categories.add(self.new_categories)

    def tearDown(self):
        categories.objects.all().delete()
        Image.objects.all().delete()

    def test_get_photos_today(self):
        today_photos = Image.todays_photos()
        self.assertTrue(len(today_photos)>0)

    def test_get_photos_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        photos_by_date = Image.days_photos(date)
        self.assertTrue(len(photos_by_date) == 0)
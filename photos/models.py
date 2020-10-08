from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.
# class Editor(models.Model):
    # first_name = models.CharField(max_length =30)
    # last_name = models.CharField(max_length =30)
    # email = models.EmailField()
    # phone_number = models.CharField(max_length = 10,blank =True)

    # def __str__(self):
    #     return self.first_name
    # class meta:
    #     ordering =['name']
    
    # def save_editor(self):
    #     self.save()

class Categories(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name


class Image(models.Model):
    Image = models.ImageField(upload_to = 'image/')
    Name = models.CharField(max_length =60)
    Description = models.TextField()
    # Categories= models.ManyToManyField(Categories)
    Location = models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name
    @classmethod
    def todays_photos(cls):
        today = dt.date.today()
        photos = cls.objects.filter(pub_date__date = today)
        return photos
    
    @classmethod
    def days_photos(cls,date):
        photos = cls.objects.filter(pub_date__date = date)
        return photos
    
    @classmethod
    def search_by_categories(cls,search_term):
        photos = cls.objects.filter(categories__icontains=search_term)
        return photos

    @classmethod
    def save_image (cls):
        photos=cls.objects.filter(Categories=Categories)


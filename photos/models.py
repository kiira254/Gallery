from django.db import models
import datetime as dt
from django.contrib.auth.models import User

class Categories(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Image_Location (models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
# image.location
# image.catagory
class Image(models.Model):
    Image = models.ImageField(upload_to = 'image/')
    Name = models.CharField(max_length =60)
    Description = models.TextField()
    categories= models.ForeignKey(Categories,on_delete=models.CASCADE)
    location = models.ForeignKey(Image_Location,on_delete=models.CASCADE)
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
    def search_by_Categories(cls,search_term):
        photos = cls.objects.filter(categories__icontains=search_term)
        return photos

    @classmethod
    def save_Image (cls):
        photos=cls.objects.filter(location__name='mombasa')
        # location=
        return photos

    @classmethod
    def delete_Image (cls):
        photos=cls.objects.filter()
        return photos

    @classmethod
    def update_Image (cls):
        photos=cls.objects.filter()
        return photos
    
    @classmethod
    def get_Image_by_id (cls):
        photos=cls.objects.filter(id=id)
        return photos

    @classmethod
    def Image_Location (cls):
        photos=cls.objects.filter(Image_Location=Image_Location)
        return photos


    




    

    

    


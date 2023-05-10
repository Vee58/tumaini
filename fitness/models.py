from django.db import models
    
class Contact(models.Model):
    name=models.CharField( max_length=20)
    email=models.EmailField()
    message=models.TextField() 

    def __str__(self):
        return self.name
    
class Enrollment (models.Model):
    name=models.CharField( max_length=20)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=12) # while using the char field we must input max lenth attribute
    message=models.TextField() 


    def __str__(self):
        return self.name


class Gallery(models.Model):
    title = models.CharField( max_length=25)
    image = models.ImageField(upload_to='gallery')

    def __int__(self):
         return self.id
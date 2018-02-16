from django.db import models

# Create your models here.
class User(models.Model):
    """ User Table for User Service"""
    Uid = models.BigAutoField(primary_key=True)
    FirstNamme = models.CharField(max_length = 20)
    LastName = models.CharField(max_length = 20)
    EmailId = models.EmailField(unique = True)
    Password = models.CharField(max_length = 256)
    MobileNumber = models.CharField(max_length= 20)
    DateCreated = models.DateTimeField()
    DateModified = models.DateTimeField()

    """String Function for All CharField in User Model"""
    def __str__(self):
        return "{0}|{1}".format(self.FirstName,self.LastName)

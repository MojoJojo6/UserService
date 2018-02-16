from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class User(AbstractBaseUser):
    """ User Table for User Service"""
    Uid = models.BigAutoField(primary_key=True)
    FirstNamme = models.CharField(max_length = 20)
    LastName = models.CharField(max_length = 20)
    EmailId = models.EmailField(unique = True)
    Password = models.CharField(max_length = 256)
    MobileNumber = models.CharField(max_length= 20)
    Role = models.IntegerField(choices=[(0,"Admin"),(1,"Faculty"),(2,"Student")])
    is_active = models.BooleanField()
    DateCreated = models.DateTimeField()
    DateModified = models.DateTimeField()

    USERNAME_FIELD = 'EmailId'
    REQUIRED_FIELDS = ['FirstName','LastName','EmailId','Password','MobileNumber','Role']

    def create_user(self):
        
    """String Function for All CharField in User Model"""
    def __str__(self):
        return "{0}|{1}".format(self.FirstName,self.LastName)



class UserCourses(models.Model):
    """
    UserCourses model
    """

    ucid = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete="cascade")
    course_id = models.BigIntegerField()
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField()

    def __str__(self):
        """
        string representation of the model
        :return:
        """
        return "UserCourses Model: {}, {}" .format(self.user, self.course_id)

    def __repr__(self):
        """
        representation of the model
        :return:
        """
        return "UserCourses Model: {}, {}" .format(self.user, self.course_id)

class FacultyCourses(models.Model):
    """
    FacultyCourses Model
    """
    ufid = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete="cascade")
    course_id = models.BigIntegerField()
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField()

    def __str__(self):
        """
        string representations of the model
        :return:
        """
        return "FacultyCourses Model: {}, {}" .format(self.user, self.course_id)

    def __repr__(self):
        """
        representation of the model
        :return:
        return "FacultyCourses Model: {}, {}" .format(self.user, self.course_id)
        """

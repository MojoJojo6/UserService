from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,BaseUserManager
)
class UserManager(BaseUserManager):
    def create_user(self,email_id,first_name = None,last_name = None,role = None,password=None,is_staff = False,is_admin = True,is_active = True):
        if not email_id:
            raise ValueError("Email Id is required")
        if not password:
            raise ValueError("Password is required")
        if not first_name:
            raise ValueError("First Name is required")
        if not last_name:
            raise ValueError("Last Name is required")
        if role is None:
            raise ValueError("Role is required")

        user_obj = self.model(
            email_id = self.normalize_email(email_id)
        )
        user_obj.first_name = first_name
        user_obj.last_name = last_name
        user_obj.role = role
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.set_password(password)
        user_obj.save(using=self.db)
        return user_obj
    def create_staffuser(self,email_id,first_name = None,last_name = None,role = None,password = None):
        user = self.create_user(
            email_id,
            password = password,
            first_name = first_name,
            last_name = last_name,
            role = role,
            is_staff = True
        )
        return user
    def create_superuser(self,email_id,first_name = None,last_name = None,role = None,password = None):
        user = self.create_user(
            email_id,
            password = password,
            first_name=first_name,
            last_name=last_name,
            role=role,
            is_staff=True,
            is_admin= True
        )
# Create your models here.
class User(AbstractBaseUser):
    """ User Table for User Service"""
    u_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    email_id = models.EmailField(max_length=255,unique = True)
    mobile_number = models.CharField(max_length= 20)
    role = models.IntegerField(choices=[(0,"Admin"),(1,"Faculty"),(2,"Student")])
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default = False)
    admin = models.BooleanField(default = False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email_id'
    REQUIRED_FIELDS = ['first_name','last_name','role']

    object = UserManager()

    def get_full_name(self):
        return "{0} {1}".format(self.first_name,self.last_name)
    def get_short_name(self):
        return self.first_name
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    """String Function for All CharField in User Model"""
    def __str__(self):
        return self.email_id



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

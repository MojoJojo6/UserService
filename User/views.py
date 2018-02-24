"""
The following Basic API endpoints will be exposed
User model:
1. get all users
2. get one user based on email
3. create one user with all required fields

UserCourses model:
1. get all courses for one user
2. get all users for one course
3. map course to user and vice versa. Basically to make an entry in the model

Faculty Course:
1. get all courses for one faculty user
2. get all faculty users for one course
3. map course to user and vice versa
"""

from django.shortcuts import  get_object_or_404
from django.shortcuts import get_list_or_404
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .models import User
from .models import UserCourses
from .models import FacultyCourses

from .api.serializer import UserSerializer
from .api.serializer import FacultyCoursesSerializer
from .api.serializer import UserCoursesSerializer


###############################################
# User
###############################################
class UserList(ListAPIView):
    """
    returns the list of all users.
    """
    def get_queryset(self):
        """
        returns the queryset
        :return:
        """
        return User.objects.all()

    def get_serializer_class(self):
        """
        returns the serializer class to be used
        :return:
        """
        return UserSerializer


class UserRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """
    returns information for specific users with email address, updates and deletes users with specific email addresses
    """
    multiple_lookup_fields = {"email_id"}

    def get_queryset(self):
        """
        return the queryset
        :return:
        """
        return User.objects.all()

    def get_serializer_class(self):
        """
        returns the serializer class
        :return:
        """
        return UserSerializer

    def get_object(self):
        """
        returns the object instance
        :return:
        """
        filter_dict = {}
        queryset = self.get_queryset()
        # self.queryset should always be used because self.queryset gets evaluated once and is cached for subsequent operations

        for field in self.multiple_lookup_fields:
            filter_dict[field] = self.kwargs[field]

        obj = get_object_or_404(queryset, **filter_dict)
        return obj


class UserCreate(CreateAPIView):
    """
    returns the list of all users or a specific user with the email address
    """
    def get_serializer_class(self):
        """
        returns the serializer class to be used
        :return:
        """
        return UserSerializer


###############################################
# UserCourses
###############################################
class UserCoursesList(ListAPIView):
    """
    returns list of all users
    """
    def get_queryset(self):
        """
        returns all users
        :return:
        """
        return UserCourses.objects.all()

    def get_serializer_class(self):
        """
        returns the serializer class
        :return:
        """
        return UserCoursesSerializer


class UserCoursesRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """
    returns a single user's courses or single course's users, updates and deletes usercourses
    """
    multiple_lookup_fields = {"email_id", "course_id"}

    def get_queryset(self):
        """
        return the queryset
        :return:
        """
        return UserCourses.objects.all()

    def get_serializer_class(self):
        """
        returns the serializer class
        :return:
        """
        return UserCoursesSerializer

    def get_object(self):
        """
        returns the object instance
        :return:
        """
        filter_dict = {}
        queryset = self.get_queryset()

        for field in self.multiple_lookup_fields:
            if field in self.kwargs.keys():
                filter_dict[field] = self.kwargs[field]

        obj = get_object_or_404(queryset, **filter_dict)
        return obj


class UserCoursesCreate(CreateAPIView):
    """
    creates a user
    """
    def get_serializer_class(self):
        """
        returns the serializer class to be used
        :return:
        """
        return UserCoursesSerializer


###############################################
# FacultyCourses
###############################################
class FacultyCoursesList(ListAPIView):
    """
    returns list of all users
    """
    def get_queryset(self):
        """
        returns all users
        :return:
        """
        return FacultyCourses.objects.all()

    def get_serializer_class(self):
        """
        returns the serializer class
        :return:
        """
        return FacultyCoursesSerializer


class FacultyCoursesRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """
    returns a single user's courses or single course's users, updates and deletes usercourses
    """
    multiple_lookup_fields = {"email_id", "course_id"}

    def get_queryset(self):
        """
        return the queryset
        :return:
        """
        return FacultyCourses.objects.all()

    def get_serializer_class(self):
        """
        returns the serializer class
        :return:
        """
        return FacultyCoursesSerializer

    def get_object(self):
        """
        returns the object instance
        :return:
        """
        filter_dict = {}
        queryset = self.get_queryset()

        for field in self.multiple_lookup_fields:
            if field in self.kwargs.keys():
                filter_dict[field] = self.kwargs[field]

        obj = get_object_or_404(queryset, **filter_dict)
        return obj


class FacultyCoursesCreate(CreateAPIView):
    """
    creates a faculty course
    """
    def get_serializer_class(self):
        """
        returns the serializer class to be used
        :return:
        """
        return FacultyCoursesSerializer

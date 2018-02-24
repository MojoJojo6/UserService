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

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.generics import ListAPIView

from .models import User
from .models import UserCourses
from .models import FacultyCourses

from .api.serializer import UserSerializer
from .api.serializer import FacultyCoursesSerializer
from .api.serializer import UserCoursesSerializer


class UserList(ListAPIView):
    """
    returns the list of all users or a specific user with the email address
    """
    def __init__(self):
        super()
        self.multiple_lookup_fields = {'email_id'}

    def get_serializer_class(self):
        """
        returns the serializer class to be used
        :return:
        """
        return UserSerializer

    def get_object(self):
        """
        returns the object instance
        :return:
        """
        filter = {}
        for field in self.multiple_lookup_fields:
            filter[field] = self.kwargs[field]

        obj = self.get_object_or_404(self.queryset, **filter)
        return obj

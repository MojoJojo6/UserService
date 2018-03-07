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
from rest_framework.response import Response

from django.shortcuts import  get_object_or_404
from rest_framework.generics import GenericAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.mixins import RetrieveModelMixin

from rest_framework.permissions import *

from .models import User
from .models import UserCourses
from .models import FacultyCourses

from .api.serializer import UserSerializer
from .api.serializer import UserCoursesSerializerList
from .api.serializer import FacultyCoursesSerializerList

from .api.serializer import UserCoursesSerializerCreate
from .api.serializer import FacultyCoursesSerializerCreate


###############################################
# User
###############################################
class UserList(ListAPIView):
    """
    returns the list of all users.
    """
    permission_classes = [IsAdminUser]

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
    permission_classes = [IsAdminUser]
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
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        """
        returns the serializer class to be used
        :return:
        """
        return UserSerializer


class UserFetch(RetrieveModelMixin, GenericAPIView):
    """
    returns true if a particular user exists
    """
    permission_classes = [AllowAny]

    def get_queryset(self):
        """
        return the queryset
        :return:
        """
        return User.objects.all()

    def get_serializer_class(self):
        """
        gets the serializer class to be used
        :return:
        """
        return UserSerializer

    def post(self, request, *args, **kwargs):
        """
        handle a post request
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        emailid = request.data["email_id"]
        password = request.data["password"]

        user = User.objects.get(email_id=emailid)
        if user:
            if user.check_password(password):
                request.user = user
                return Response("Found", status=200)

        return Response("Not Found", status=404)

    def get(self, request, *args, **kwargs):
        """
        handles a get request
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return Response(status=403)


###############################################
# UserCourses
###############################################
class UserCoursesList(ListAPIView):
    """
    returns list of all users
    """
    permission_classes = [IsAdminUser]

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
        return UserCoursesSerializerList


class UserCoursesSelect(ListAPIView):
    """
    returns a single user's courses or single course's users, updates and deletes usercourses
    """
    permission_classes = [IsAdminUser]
    multiple_lookup_fields = {"email_id", "course_id"}

    def get_queryset(self):
        """
        return the queryset
        :return:
        """
        if "email_id" in self.kwargs.keys():
            user = User.objects.filter(email_id=self.kwargs["email_id"])
            # this will only return one user
            return UserCourses.objects.filter(user=user[0])

        elif "course_id" in self.kwargs.keys():
            return UserCourses.objects.filter(course_id=self.kwargs["course_id"])

    def get_serializer_class(self):
        """
        returns the serializer class
        :return:
        """
        return UserCoursesSerializerList


class UserCoursesCreate(CreateAPIView):
    """
    creates a user
    """
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        """
        returns the serializer class to be used
        :return:
        """
        return UserCoursesSerializerCreate


class UserCoursesDelete(DestroyAPIView):
    """
    deletes list of users based on course ids
    """
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        """
        returns the serializer class
        :return:
        """
        return UserCoursesSerializerList

    def destroy(self, request, *args, **kwargs):
        """
        deletes multiple instances from the model
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        try:
            faculty_courses = UserCourses.objects.filter(**kwargs)
            for element in faculty_courses:
                print(element)
                element.delete()
            return Response("Successfully deleted")
        except Exception:
            raise Exception("LOL")


###############################################
# FacultyCourses
###############################################
class FacultyCoursesList(ListAPIView):
    """
    returns list of all users
    """
    permission_classes = [IsAdminUser]

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
        return FacultyCoursesSerializerList


class FacultyCoursesSelect(ListAPIView):
    """
    returns a single user's courses or single course's users, updates and deletes usercourses
    """
    permission_classes = [IsAdminUser]
    multiple_lookup_fields = {"email_id", "course_id"}

    def get_queryset(self):
        """
        return the queryset
        :return:
        """
        print (self.kwargs)

        if "email_id" in self.kwargs.keys():
            user = User.objects.filter(email_id=self.kwargs["email_id"])
            # this will only return one user
            return FacultyCourses.objects.filter(user=user[0])

        elif "course_id" in self.kwargs.keys():
            return FacultyCourses.objects.filter(course_id=int(self.kwargs["course_id"]))

    def get_serializer_class(self):
        """
        returns the serializer class
        :return:
        """
        return FacultyCoursesSerializerList


class FacultyCoursesCreate(CreateAPIView):
    """
    creates a faculty course
    """
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        """
        returns the serializer class to be used
        :return:
        """
        return FacultyCoursesSerializerCreate


class FacultyCoursesDelete(DestroyAPIView):
    """
    delete a faculty course
    """
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        """
        returns the serializer class
        :return:
        """
        return FacultyCoursesSerializerList

    def destroy(self, request, *args, **kwargs):
        """
        deletes multiple instances from the model
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        try:
            faculty_courses = FacultyCourses.objects.filter(**kwargs)
            for element in faculty_courses:
                print(element)
                element.delete()
            return Response("Successfully deleted")
        except Exception:
            raise Exception("LOL")
"""UserService URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""
1)users/ -> gives all the information for all the users
2)users/<email_id>/  -> gives all the user information based on email parameter 
3)user-create/ -> create all kinds of users ( future register function ) 

4)user-courses ->gives all the users and its enrolled course list
5)user-courses-emailid/<email_id> -> gives information of particular users (based on email_id) all enrolled courses 
6)user-courses-courseid/<course_id> -> gives information of particular users (based on course_id) all enrolled courses
7)user-course-create/ ->creates user-course mapping

8)faculty-courses/ -> gives all the FacultyUsers and its enrolled course list
9)faculty-course-emailid/ -> gives information of particular FacultyUsers (based on email_id) all enrolled courses
10)faculty-course-courseid/ -> gives information of particular users (based on course_id) all enrolled courses
11)faculty-courses-create/ -> creates faculty-course mapping

"""
from django.urls import path, re_path

from .views import UserList
from .views import UserRetrieveUpdateDestroy
from .views import UserCreate

from .views import UserCoursesList
from .views import UserCoursesSelect
from .views import UserCoursesCreate

from .views import FacultyCoursesList
from .views import FacultyCoursesSelect
from .views import FacultyCoursesCreate

urlpatterns = [
    path("users/", UserList.as_view()),
    path("users/<str:email_id>/", UserRetrieveUpdateDestroy.as_view()),
    path("user-create/", UserCreate.as_view()),

    path("user-courses/", UserCoursesList.as_view()),
    path("user-courses-emailid/<str:email_id>/", UserCoursesSelect.as_view()),
    path("user-courses-courseid/<str:course_id>/", UserCoursesSelect.as_view()),
    path("user-courses-create/", UserCoursesCreate.as_view()),

    path("faculty-courses/", FacultyCoursesList.as_view()),
    path("faculty-courses-emailid/<str:email_id>/", FacultyCoursesSelect.as_view()),
    path("faculty-courses-courseid/<str:course_id>/", FacultyCoursesSelect.as_view()),
    path("faculty-courses-create/", FacultyCoursesCreate.as_view())
]

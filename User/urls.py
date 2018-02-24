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
from django.urls import path, re_path

from .views import UserList
from .views import UserRetrieveUpdateDestroy
from .views import UserCreate

from .views import UserCoursesList
from .views import UserCoursesRetrieveUpdateDestroy
from .views import UserCoursesCreate

from .views import FacultyCoursesList
from .views import FacultyCoursesRetrieveUpdateDestroy
from .views import FacultyCoursesCreate

urlpatterns = [
    path("users/", UserList.as_view()),
    path("users/<str:email_id>/<str:mobile_number>", UserRetrieveUpdateDestroy.as_view()),
    path("user-create/", UserCreate.as_view()),

    path("user-courses/", UserCoursesList.as_view()),
    path("user-courses/<str:email_id>/", UserCoursesRetrieveUpdateDestroy.as_view()),
    path("user-courses-create/", UserCoursesCreate.as_view()),

    path("faculty-courses/", FacultyCoursesList.as_view()),
    path("faculty-courses/<str:email_id>/", FacultyCoursesRetrieveUpdateDestroy.as_view()),
    path("faculty-courses-create", FacultyCoursesCreate.as_view())
]

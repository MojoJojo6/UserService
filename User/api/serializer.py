from rest_framework import serializers
from ..models import User
from ..models import UserCourses
from ..models import FacultyCourses


class UserSerializer(serializers.ModelSerializer):
    """
    serializer for user model
    """
    id = serializers.IntegerField(required=False, read_only=True)
    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)
    email_id = serializers.EmailField(max_length=255)
    mobile_number = serializers.CharField(max_length=20, required=False)
    role = serializers.IntegerField()
    active = serializers.IntegerField()
    staff = serializers.IntegerField()
    admin = serializers.IntegerField()
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email_id', 'mobile_number', 'role', 'active', 'staff', 'admin']


class UserCoursesSerializer(serializers.ModelSerializer):
    """
    serializer for UserCourses model
    """
    id = serializers.IntegerField(required=False, read_only=True)
    user = UserSerializer(many=True)
    course_id = serializers.IntegerField()
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = UserCourses
        fields = ['id', 'user', 'course_id']


class FacultyCoursesSerializer(serializers.ModelSerializer):
    """
    serializer for FacultyCourses model
    """
    id = serializers.IntegerField(required=False, read_only=True)
    user = UserSerializer(many=True)
    course_id = serializers.IntegerField()
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = FacultyCourses
        fields = ['id', 'user', 'course_id']

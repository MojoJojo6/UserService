from rest_framework import serializers
from ..models import User
from ..models import UserCourses
from ..models import FacultyCourses


class UserSerializer(serializers.ModelSerializer):
    """
    serializer for user model
    """
    u_id = serializers.IntegerField(required=False, read_only=True)
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
        fields = ['u_id', 'first_name', 'last_name', 'email_id', 'mobile_number', 'role', 'active', 'staff', 'admin',
                  'date_created', 'date_modified']


class UserCoursesSerializer(serializers.ModelSerializer):
    """
    serializer for UserCourses model
    """
    id = serializers.IntegerField(required=False, read_only=True)
    # user = serializers.ManyRelatedField(queryset=User.objects.all(), many=True)
    # user = serializers.IntegerField()
    user = UserSerializer(many=True)
    course_id = serializers.IntegerField()
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        """
        for data creation
        :param validated_data:
        :return:
        """
        # since we are using the same serializer both for retrieving and creating FacultyCourses we are using this separate method
        # for creation
        if len(validated_data["user"]) != 1:
            raise ValueError("More than one user was entered")

        user_courses_dict = {
            'user': validated_data['user'][0],
            'course_id': validated_data['course_id']
        }
        return UserCourses.objects.create(**user_courses_dict)

    class Meta:
        model = UserCourses
        fields = ['id', 'user', 'course_id', 'date_created', 'date_modified']


class FacultyCoursesSerializer(serializers.ModelSerializer):
    """
    serializer for FacultyCourses model
    """
    id = serializers.IntegerField(required=False, read_only=True)
    # user = UserSerializer(many=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    # user = serializers.IntegerField()
    course_id = serializers.IntegerField()
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        """
        for data creation
        :param validated_data:
        :return:
        """
        # since we are using the same serializer both for retrieving and creating FacultyCourses we are using this separate method
        # for creation
        if len(validated_data["user"]) != 1:
            raise ValueError("More than one user was entered")

        faculty_courses_dict = {
            'user': validated_data['user'][0],
            'course_id': validated_data['course_id']
        }
        return FacultyCourses.objects.create(**faculty_courses_dict)


    class Meta:
        model = FacultyCourses
        fields = ['id', 'user', 'course_id', 'date_created', 'date_modified']

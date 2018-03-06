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
    password = serializers.CharField(max_length=255, write_only=True, required=True)
    mobile_number = serializers.CharField(max_length=20, required=False)
    role = serializers.ChoiceField(choices=User.roles)
    active = serializers.BooleanField(default=True)
    staff = serializers.BooleanField(default=False)
    admin = serializers.BooleanField(default=False)
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        fields = ['u_id', 'first_name', 'last_name', 'email_id', 'password', 'mobile_number', 'role', 'active', 'staff', 'admin',
                  'date_created', 'date_modified']


class UserCoursesSerializerCreate(serializers.ModelSerializer):
    """
    serializer for UserCourses model
    """

    id = serializers.IntegerField(required=False, read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    course_id = serializers.IntegerField()
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        """
        for data creation
        :param validated_data:
        :return:
        """
        # for creation

        user_courses_dict = {
            'user': validated_data['user'],
            'course_id': validated_data['course_id']
        }
        return UserCourses.objects.create(**user_courses_dict)

    class Meta:
        model = UserCourses
        fields = ['id', 'user', 'course_id', 'date_created', 'date_modified']


class UserCoursesSerializerList(serializers.ModelSerializer):
    """
    serializer for UserCourses model
    """
    id = serializers.IntegerField(required=False, read_only=True)
    user = UserSerializer()
    course_id = serializers.IntegerField()
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = UserCourses
        fields = ['id', 'user', 'course_id', 'date_created', 'date_modified']


class FacultyCoursesSerializerList(serializers.ModelSerializer):
    """
    serializer for FacultyCourses model
    """
    id = serializers.IntegerField(required=False, read_only=True)
    user = UserSerializer()
    course_id = serializers.IntegerField()
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = FacultyCourses
        fields = ['id', 'user', 'course_id', 'date_created', 'date_modified']


class FacultyCoursesSerializerCreate(serializers.ModelSerializer):
    """
    serializer for FacultyCourses model
    """
    id = serializers.IntegerField(required=False, read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    course_id = serializers.IntegerField()
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        """
        for data creation
        :param validated_data:
        :return:
        """
        # import ipdb
        # ipdb.set_trace()
        faculty_courses_dict = {
            'user': validated_data['user'],
            'course_id': validated_data['course_id']
        }
        return FacultyCourses.objects.create(**faculty_courses_dict)


    class Meta:
        model = FacultyCourses
        fields = ['id', 'user', 'course_id', 'date_created', 'date_modified']

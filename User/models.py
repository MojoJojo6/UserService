from django.db import models

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


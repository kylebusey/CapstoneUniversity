from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=50, blank=False, unique=True)
    first_name = models.CharField(max_length=25, blank=False)
    last_name = models.CharField(max_length=25, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_email(self):
        return self.email

    def get_name(self):
        return self.first_name + " " + self.last_name

class Course(models.Model):
    course_name = models.CharField(max_length=50)
    professor_name = models.CharField(max_length=50)
    number_of_credits = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.EmailField(max_length=50)
    description = models.TextField(max_length=200)
    available_seats = models.IntegerField()
    open = models.BooleanField('Open', default=True)

    def __str__(self):
        return f"{self.courseName}: {self.start_date}"

class UserType(models.Model):
    is_faculty = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        if self.is_faculty:
            return User.get_email(self.user) + " - is_faculty"
        else:
            return User.get_email(self.user) + " - is_student"
from django.db import models
import datetime
from course.models import Course
from django.core.exceptions import ValidationError


class Student(models.Model):

    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length = 20)
    registration_number = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 70)
    phone_number = models.CharField(max_length = 20)
    date_joined = models.DateField()
    courses = models.ManyToManyField(Course)
    image = models.ImageField(upload_to = "profiles" , blank= True)
    



    def __str__(self):
        return self.first_name +" "+ self.last_name

    def image_url(self):
        if self.image and hasattr(self.image, "url"):
            return self.image.url

    def full_name(self):
        return "{} {}".format(self.first_name,self.last_name)

    def get_age(self):
       today = datetime.date.today()
       return today.year - self.date_of_birth.year - ((today.month,today.day) < (self.date_of_birth.month, self.date_of_birth.day))
    age = property(get_age)
    
    def clean(self):
       age = self.age
       if age < 17 or age > 30:
           raise ValidationError("Sorry you can't create an account, Age must be at least 17 and below 30")
       return age




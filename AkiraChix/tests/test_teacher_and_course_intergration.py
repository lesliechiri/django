from django.test import TestCase
from teacher.models import Teacher
from course.models import Course
import datetime

class CourseTeacherTestCase(TestCase):
   def setUp(self):


    


       self.teacher_a = Teacher.objects.create(
           id="34862674",
           first_name = "Lelsie",
           last_name = "Chiri",
           date_of_birth = datetime.date(1995,11,29),
           gender = "female",
           registration_number  = "5858",
           email = "dianawantes@gmail.com",
           phone_number = "0703705309",
           date_joined = datetime.date.today(),
           number_of_children = 4,
           marital_status = "single",

           )
       self.teacher_b = Teacher.objects.create(
           first_name = "Samuel",
           last_name = "Kihara",
           date_of_birth = datetime.date(1992,7,23),
           gender = "male",
           registration_number  = "2351",
           email = "skkmuhu@yahoo.com",
           phone_number = "0722819544",
           date_joined = datetime.date.today(),
           number_of_children = 4,
           marital_status = "married"
           )
       self.python = Course.objects.create(
           name="Python",
           duration_of_course=9,
           start_date=datetime.date.today(),
           end_date=datetime.date.today(),
           description="backenddeveloper",
           )
       self.java = Course.objects.create(
           name="Java",
           duration_of_course=7,
           start_date=datetime.date.today(),
           end_date=datetime.date.today(),
           description="frontendeveloper",
           )
       self.design = Course.objects.create(
           name="Design",
           duration_of_course=5,
           start_date=datetime.date.today(),
           end_date=datetime.date.today(),
           description="designer",
           )
   def test_course_can_be_trained_by_a_teacher(self):
       self.python.teacher = self.teacher_a
       self.assertEqual(self.python.teacher, self.teacher_a)
   def test_many_courses_can_be_trained_by_one_trainer(self):
       self.python.teacher = self.teacher_b
       self.java.teacher = self.teacher_b
       self.assertEqual(self.java.teacher,self.python.teacher)

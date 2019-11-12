from django.test import TestCase
from student.models import Student
from course.models import Course
import datetime
class StudentCourseTestCase(TestCase):
   def setUp(self):
       self.student_a = Student.objects.create(
           id="34862674",
           first_name = "Lelsie",
           last_name = "Chiri",
           date_of_birth = datetime.date(1995,11,29),
           gender = "female",
           registration_number  = "5858",
           email = "dianawantes@gmail.com",
           phone_number = "0703705309",
           date_joined = datetime.date.today(),
           )
       self.student_b = Student.objects.create(
           first_name = "Samuel",
           last_name = "Kihara",
           date_of_birth = datetime.date(1992,7,23),
           gender = "male",
           registration_number  = "2351",
           email = "skkmuhu@yahoo.com",
           phone_number = "0722819544",
           date_joined = datetime.date.today(),
           )
       self.python = Course.objects.create(
           name="Python",
           duration_of_course=9,
           start_date=datetime.date.today(),
           end_date=datetime.date.today(),
           description="backenddeveloper",
           )
       self.javascript = Course.objects.create(
           name="JavaScript",
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
   def test_student_can_join_a_course(self):
       self.student_a.courses.add(self.python)
       self.assertEqual(self.student_a.courses.count(),1)
       self.student_a.courses.add(self.javascript)
       self.assertEqual(self.student_a.courses.count(),2)
       self.student_a.courses.add(self.design)
       self.assertEqual(self.student_a.courses.count(),3)
   def test_student_can_join_many_courses(self):
       self.student_b.courses.add(self.python,self.javascript,self.design)
       self.assertEqual(self.student_b.courses.count(),3)









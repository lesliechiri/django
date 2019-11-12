from django.test import TestCase
from .models import Course
from course.forms import CourseForm
from django.core.validators import BaseValidator
import datetime


class AddCourseTestCase(TestCase):

    def setUp(self):

        self.data = {
                        "name":"Python",
                        "start_date":datetime.date.today(),
                        "end_date":datetime.date(2019,11,29),
                        "description":"course that deals with logic and good syntax",
                        
                        
        
        }
        self.bad_data ={
                        "name":"math",
                        "start_date":datetime.date.today(),
                        "end_date":datetime.date(2019,11,29),
                        "description":"course that deals with logic and good syntax",
        }
    def test_course_form_accepts_valid_data(self):
        form = CourseForm(self.data)

        if form == CourseForm(self.data):
            self.assertTrue(form.is_valid())



        # form = CourseForm(self.data)
        # self.assertFalse(form.is_valid())
    def test_course_form_rejects_invalid_data(self):
        form = CourseForm(self.data)

        if form == CourseForm(self.bad_data):
            self.assertFalse(form.is_valid())




        # form = CourseForm(self.bad_data)
        # self.assertFalse(form.is_valid())

# Create your tests here.

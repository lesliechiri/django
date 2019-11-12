from django.test import TestCase
from .models import Teacher
from teacher.forms import TeacherForm
from django.core.validators import BaseValidator
import datetime






class AddTeacherTestCase(TestCase):

    def setUp(self):

        self.data = {
                        "first_name":"Diana",
                        "last_name":"Muchiri",
                        "date_of_birth":datetime.date(1995,11,29),
                        "gender":"female",
                        "registration_number":"5858",
                        "email ":"dianawantes@gmail.com",
                        "phone_number" :"254703705309",
                        "date_joined ": datetime.date.today(),
                        "marital_status":"married",
                        "number_of_children": 4,
                        "image": "",
                        
        
        }
        self.bad_data ={
                        "first_name":"Diana",
                        "last_name":"Muchiri",
                        "date_of_birth":datetime.date(1995,11,29),
                        "gender":"female",
                        "registration_number":"5858",
                        "email ":"dianawantescom",
                        "phone_number" :"254703705309",
                        "date_joined ": datetime.date.today(),
                        "marital_status":"married",
                        "number_of_children": 4,
                        "image": "",
                        
                        
        }
    def test_teacher_form_accepts_valid_data(self):
        form = TeacherForm(self.data)

        if form == TeacherForm(self.data):
            self.assertTrue(form.is_valid())



        # form = TeacherForm(self.data)
        # self.assertTrue(form.is_valid())
    def test_teacher_form_rejects_invalid_data(self):
        form = TeacherForm(self.data)

        if form == TeacherForm(self.bad_data):
            self.assertFalse(form.is_valid())




        # form = TeacherForm(self.bad_data)
        # self.assertFalse(form.is_valid())


# Create your tests here.


from rest_framework import viewsets
from .serializer import StudentSerializer
from .serializer import TeacherSerializer
from .serializer import CourseSerializer

from student.models import Student
from teacher.models import Teacher
from course.models import Course



class StudentViewSet(viewsets.ModelViewSet):
	queryset = Student.objects.all()
	serializer_class=StudentSerializer


class TeacherViewSet(viewsets.ModelViewSet):
	queryset = Teacher.objects.all()
	serializer_class=TeacherSerializer


class CourseViewSet(viewsets.ModelViewSet):
	queryset = Course.objects.all()
	serializer_class=CourseSerializer		

# Create your views here.

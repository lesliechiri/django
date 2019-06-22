from django.shortcuts import render
from .forms import StudentForm
from .models import Student


def add_student(request):
	if request.method == "POST":
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save()
		else:
			form = StudentForm()

	return render(request,"add_student.html",{"form":form})				
	

def list_students(request):
	students = Student.objects.all()
	return render(request,"all_students.html",{"students":students})		



def HomePageView(request):
    model = Student
    template_name = 'home.html'
# Create your views here.

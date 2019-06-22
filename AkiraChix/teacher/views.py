from django.shortcuts import render
from .forms import TeacherForm
from .models import Teacher

def add_teacher(request):
	if request.method == "POST":
		form = TeacherForm(request.POST)
		if form.is_valid():
			form.save()
		else:
			form = TeacherForm()

	return render(request,"add_teacher.html",{"form":form})	



def list_teachers(request):
	teachers = Teacher.objects.all()
	return render(request,"all_teachers.html",{"teachers":teachers})		
	

# Create your views here.

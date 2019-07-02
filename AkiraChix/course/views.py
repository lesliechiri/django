from django.shortcuts import render
from .forms import CourseForm
from .models import Course
from django.shortcuts import redirect





def add_course(request):

	if request.method == "POST":
		form = CourseForm(request.POST)	
		if form.is_valid():
			form.save()
			return redirect("list_courses")
	else:
			form = CourseForm()

	return render(request,"add_course.html",{"form":form})				
	


def list_courses(request):
	courses = Course.objects.all()
	return render(request,"all_courses.html",{"courses":courses})		


def course_details(request,pk):
	course = Course.objects.get(pk=pk)
	return render(request,"course_details.html",{"course":course})



def edit_course(request,pk):
	course = Course.objects.get(pk=pk)
	if request.method == "POST":
		form = CourseForm(request.POST,instance=course)
		if form.is_valid:
			form.save()
			return redirect("list_courses")

	else:
			form = CourseForm(instance=course)

	return render(request,"edit_course.html",{"form":form})								



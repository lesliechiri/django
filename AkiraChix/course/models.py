from django.db import models
from teacher.models import Teacher


class Course(models.Model):

	name = models.CharField(max_length = 50)
	duration_of_course = models.SmallIntegerField()
	start_date = models.DateField()
	end_date = models.DateField()
	description = models.TextField()
	teacher = models.ForeignKey(Teacher,null = True, on_delete = models.CASCADE)


	def __str__(self):
		return self.name
	

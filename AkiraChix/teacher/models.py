from django.db import models

class Teacher(models.Model):

	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	date_of_birth = models.DateField()
	gender = models.CharField(max_length = 20)
	registration_number = models.CharField(max_length = 20)
	email = models.EmailField(max_length = 70)
	phone_number = models.CharField(max_length = 20)
	date_joined = models.DateField()
	marital_status = models.CharField(max_length = 15)
	number_of_children = models.IntegerField()
	image = models.ImageField(upload_to = "profiles", blank = True)


	def __str__(self):
		return self.first_name+ " " +self.last_name


	def image_url(self):
		if self.image and hasattr(self.image, "url"):
			return self.image.url

	
	


# Create your models here.

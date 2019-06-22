from django import forms
from.models import Student
from django.core.files.images import get_image_dimensions
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


    def clean_image(self):
        image = self.cleaned_data['image']  
    
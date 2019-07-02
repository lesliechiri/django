from django import forms
from.models import Teacher
from django.core.files.images import get_image_dimensions
class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"
    


    def clean_image(self):
        image = self.cleaned_data['image']  
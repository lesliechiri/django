from django.urls import path
from .views import add_student
from .views import list_students

from .views import HomePageView


urlpatterns = [
path("add/",add_student, name = "add_student"), path("view",HomePageView, name='home'),path("list/",list_students,name = "list_students")]
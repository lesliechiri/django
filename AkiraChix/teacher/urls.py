from django.urls import path
from .views import add_teacher
from .views import list_teachers
urlpatterns = [
path("add/",add_teacher, name = "add_teacher"),path("list/",list_teachers,name = "list_teachers")]
from django.urls import path, include
from .views import index, delete_student, update_student, update

urlpatterns = [
    path("", index, name="index"),
    path("delete/<int:roll>", delete_student, name="delete"),
    path("update_student/<int:roll>", update_student, name="update_student"),
    path("update/<int:roll>", update, name="update"),
]

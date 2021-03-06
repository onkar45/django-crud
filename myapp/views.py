from django.shortcuts import render, redirect
from .models import Student

def index(request):
    if request.method == "POST":
        roll = request.POST["roll_number"]
        email = request.POST["email_id"]
        name = request.POST["name"]
        mobile_number = request.POST["mobile_number"]
        address = request.POST["address"]
        student = Student(name=name, roll_number=roll, email_id=email, mobile_number=mobile_number, address=address)
        student.save()

    students = Student.objects.all()
    context = {
        "students": students
    }
    return render(request, "index.html", context)


def delete_student(request, roll):
    student = Student.objects.get(roll_number=roll)
    student.delete()
    return redirect(index)

def update_student(request, roll):
    student = Student.objects.get(roll_number=roll)
    context = {
        "student": student
    }
    return render(request, "update_student.html", context)

def update(request, roll):
    if request.method == "POST":
        student = Student.objects.get(roll_number=roll)
        student.name = request.POST.get("name")
        student.roll_number = request.POST.get("roll_number")
        student.mobile_number = request.POST.get("mobile_number")
        student.address = request.POST.get("address")
        student.email_id = request.POST.get("email_id")
        student.save()
    return redirect(index)
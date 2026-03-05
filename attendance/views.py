from django.shortcuts import render, redirect
from .models import Student

def register_student(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        if name:
            Student.objects.create(name=name)
        return redirect("register_student")  # refresh page after submit

    return render(request, "attendance/register_student.html")

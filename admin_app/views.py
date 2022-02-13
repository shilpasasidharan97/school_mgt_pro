from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request,'dashboard.html')

def admin_home(request):
    return render(request,'admin_home.html')

def student_details(request):
    return render(request,'studentdetails.html')
def newstudent(request):
    return render(request,'newstudent.html')

def teacher_details(request):
    return render(request,'teacherdetails.html')

def newstaff(request):
    return render(request,'newstaff.html')

def staffattandance(request):
    return render(request,'staffattandance.html')

def one(request):
    return render(request,'1.html')
from django.shortcuts import render,redirect
from .forms import StudentRegistrationForm
from .models import Student,Company,PlacementDrive,Application
from datetime import date
# Create your views here.
def home(request):
    return render(request,'home.html')
def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudentRegistrationForm()
    return render(request,'register.html',{'form': form})
def dashboard(request):
    student=Student.objects.get(student_id=1)
    return render(request,'dashboard.html',{'student':student})
def companies(request):
    company_list=Company.objects.all()
    return render(request,'companies.html',{'companies':company_list})
def  drives(request):
    drive_list=PlacementDrive.objects.all()
    return render(request,'drives.html',{'drives':drive_list})
def apply_drive(request,drive_id):
    if request.method=='POST':
        student=Student.objects.get(student_id=1)
        drive=PlacementDrive.objects.get(drive_id=drive_id)
        if student.cgpa >= drive.minimum_cgpa:
        
         Application.objects.get_or_create(
        student=student,
        drive=drive,
        defaults={
            'application_date': date.today(),
            'status': 'Applied'
        }
    )
        return redirect('drives')
def application_status(request):
        student = Student.objects.get(student_id=1)
        applications = Application.objects.filter(student=student).select_related('drive','drive__Company')
        return render(request,'application_status.html',{'applications':applications})

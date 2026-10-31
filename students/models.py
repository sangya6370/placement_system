from django.db import models

# Create your models here.
class Student(models.Model):
    student_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=255)
    branch=models.CharField(max_length=50)
    cgpa=models.DecimalField(max_digits=3,decimal_places=2)
    graduation_year=models.IntegerField()
    class Meta:
        db_table='student'
class Company(models.Model):
    Company_id=models.AutoField(primary_key=True)
    Company_name=models.CharField(max_length=100)
    location=models.CharField(max_length=100,blank=True)
    website=models.CharField(max_length=255,blank=True)
    class Meta:
        db_table='company'
class PlacementDrive(models.Model):
    drive_id=models.AutoField(primary_key=True)
    Company=models.ForeignKey(Company,on_delete=models.CASCADE,db_column='company_id')
    job_role=models.CharField(max_length=100)
    package_lpa=models.DecimalField(max_digits=5,decimal_places=2)
    deadline=models.DateField()
    class Meta:
        db_table='placement_drive'
class Application(models.Model):
    application_id=models.AutoField(primary_key=True)
    student=models.ForeignKey(Student,on_delete=models.CASCADE,db_column='student_id')
    drive=models.ForeignKey(PlacementDrive,on_delete=models.CASCADE,db_column='drive_id')
    application_date=models.DateField()
    status=models.CharField(max_length=30,default='Applied')
    class Meta:
        db_table='application'
        
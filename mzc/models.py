from django.db import models

# Create your models here.
GENDER_CHOICE=(
    ('M','MALE'),
    ('F','FEMALE'),
    ('O','OTHERS')
)
INTEGER_CHOICES= [tuple([x,x]) for x in range(1,32)]
class Students(models.Model):
    name=models.CharField(max_length=50)
    rollno=models.CharField(max_length=10)
    course=models.CharField(max_length=10)
    address=models.TextField()
    todays_date= models.CharField(max_length=50,choices=INTEGER_CHOICES,default='1')
class Faculty(models.Model):
    faculty_Name=models.CharField(max_length=50)
    faculty_ID=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    gender=models.CharField(max_length=5,choices=GENDER_CHOICE,default='M')
    years_experience=models.CharField(max_length=50)


    
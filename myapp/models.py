
from django.db import models

from django.contrib.auth.models import AbstractUser
class Myuser(AbstractUser):
    phone_no = models.CharField(max_length=20,default=0)
    address = models.CharField(max_length=200, default="null")
    expert_status=models.BooleanField(default=False)

class FresherRegisterTable(models.Model):
        fresher_id = models.OneToOneField(Myuser, on_delete=models.CASCADE)
        full_name = models.CharField(max_length=100)

        state = models.CharField(max_length=100)
        city = models.CharField(max_length=100)
        gender = models.CharField(max_length=100)
        dob = models.DateField()
        college = models.CharField(max_length=100)
        degree = models.CharField(max_length=100)
        specialization = models.CharField(max_length=200)

class ExpertRegisterTable(models.Model):
    user_id = models.OneToOneField(Myuser, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    gender= models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    post = models.CharField(max_length=200)
    experience = models.CharField(max_length=200)
#
#
class CompanyRegisterTable(models.Model):
    user_id = models.OneToOneField(Myuser, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    state= models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    additional_information = models.CharField(max_length=200)

class Company_Jobs(models.Model):
    company_id=models.ForeignKey(CompanyRegisterTable,on_delete=models.CASCADE)
    job_name=models.CharField(max_length=100)
    job_details=models.CharField(max_length=200)
    qualification=models.CharField(max_length=100)
    experience=models.CharField(max_length=100)
    salry=models.FloatField(default=0)
class Applied_jobs(models.Model):
    applied_user=models.ForeignKey(Myuser,on_delete=models.CASCADE)
    applied_job=models.ForeignKey(Company_Jobs,on_delete=models.CASCADE)
    applied_date=models.DateField()
    status=models.IntegerField(default=0)

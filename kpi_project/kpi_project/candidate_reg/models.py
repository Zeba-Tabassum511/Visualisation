from django.db import models

# Create your models here.


class Candidate(models.Model):

    Fullname = models.CharField(max_length=50,null=True, blank=True)
    Email_id = models.EmailField(max_length=25,null=True, blank=True)
    Employee_id = models.CharField(max_length=50,null=True, blank=True)
    Designation = models.CharField(max_length=30,null=True, blank=True)
    Domain = models.CharField(max_length=20,null=True, blank=True)
    Password = models.CharField(max_length=20,null=True, blank=True)

    class Meta:
        db_table = "Employee_table" 

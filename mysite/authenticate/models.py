from django.db import models

# Create your models here.
class stud(models.Model):
    id=models.AutoField(primary_key=True)
    sname=models.CharField(max_length=50)
    saddress=models.CharField(max_length=50)
    smobile=models.CharField(max_length=50)
from django.db import models

# Create your models here.

class Signup(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(primary_key=True,unique=True)
    mobile=models.IntegerField(default=0)
    password=models.CharField(max_length=30)
    Repassword=models.CharField(max_length=30)
    @staticmethod
    def get_all():
        return Signup.objects.all()
    
    

class Query(models.Model):
    qname=models.CharField(max_length=1000)
    qemail=models.EmailField()
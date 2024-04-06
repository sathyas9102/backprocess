# import email
# from .models import password
from django.db import models

# Create your models here.
class register(models.Model):
    username=models.CharField(max_length=50)
    f_name=models.CharField(max_length=50)
    l_name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    # pass2=models.CharField(max_length=50)
    
    # def register(self):
    #     self.save()
    
def login(request):
     Email=request.POST['email']
     password=request.POST['password']
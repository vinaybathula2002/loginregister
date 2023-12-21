from django.db import models
class regmodel(models.Model):
    First_name= models.CharField(max_length=10)
    Last_name=models.CharField(max_length=10)
    User_name=models.CharField(max_length=10)
    Password=models.CharField(max_length=10)
    Cpassword=models.CharField(max_length=10)
    Email_id=models.EmailField(max_length=20)
    Mobno=models.IntegerField()

    def __str__(self):
        return self.User_name
# Create your models here.

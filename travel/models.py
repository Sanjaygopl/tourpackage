
from django.db import models
from django.template.defaultfilters import upper
from django.contrib.auth.models import User

class Profile(models.Model):
     user  = models.OneToOneField(User, on_delete=models.CASCADE)
     def __str__(self):
          return self.user.username

# Create your models here.
class Explores(models.Model):
     title = models.CharField(max_length=200)
     destination = models.CharField(max_length=200)
     image = models.ImageField(upload_to='img')
     duration = models.IntegerField()
     price = models.FloatField()
     expiry = models.DateField()
     approved = models.BooleanField(default=False)
     user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

     def __str__(self):
          return "%s" %(self.destination)
     class Meta:
          db_table="travel"

class Venreg(models.Model):
     username = models.CharField(max_length=200)
     email = models.EmailField(max_length=200)
     password = models.CharField(max_length=200)

     def __str__(self):
          return "%s" %(self.Email)
     class Meta:
          db_table="vendorregistration"
class Venlog(models.Model):
     username = models.CharField(max_length=200)
     password = models.CharField(max_length=200)

     def __str__(self):
          return "%s" %(self.password)
     class Meta:
          db_table="vendorlogin"
class Usereg(models.Model):
     username = models.CharField(max_length=200)
     email = models.EmailField(max_length=200)
     password = models.CharField(max_length=200)


     def __str__(self):
          return "%s" %(self.Email)
     class Meta:
          db_table="userregistration"
class Uselog(models.Model):
     username = models.CharField(max_length=200)
     password = models.CharField(max_length=200)


     def __str__(self):
          return "%s" %(self.password)
     class Meta:
          db_table="userlogin"

from django.db import models

class client_data(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=11)
    email=models.CharField(max_length=400)
    message=models.TextField(blank=True,null=True)
    def __str__(self):
     return self.name
class company(models.Model):
   location=models.CharField(max_length=200)
   phone=models.CharField(max_length=200)
   email=models.CharField(max_length=200)
   linkin=models.CharField(max_length=200)
   facebook=models.CharField(max_length=200)
   twitter=models.CharField(max_length=200)
   instgram=models.CharField(max_length=200)

class services(models.Model):
   title=models.CharField(max_length=200)
   image=models.ImageField()
   desceiption=models.TextField()
   def __str__(self):
      return self.title
class Locations(models.Model):
   title=models.CharField(max_length=200)
   image=models.ImageField()
   desceiption=models.TextField()
